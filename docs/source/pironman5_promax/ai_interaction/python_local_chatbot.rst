.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



6. Chatbot Vocal Local
========================

Dans cette leçon, vous allez combiner tout ce que vous avez appris — **reconnaissance vocale (STT)**,
**synthèse vocale (TTS)** et un **LLM local (Ollama)** — pour construire un **chatbot vocal** entièrement hors ligne
qui fonctionne sur votre Pironman 5 Pro MAX.

Le flux de travail est simple :

#. **Écouter** — Le microphone capture votre discours et le transcrit avec **Vosk**.
#. **Penser** — Le texte est envoyé à un **LLM** local fonctionnant sur Ollama (par exemple, ``llama3.2:3b``).
#. **Parler** — Le chatbot répond à voix haute en utilisant **Piper TTS**.

Cela crée un **robot conversationnel mains libres** capable de comprendre et de répondre en temps réel.

----

Avant de commencer
------------------

Assurez-vous d'avoir préparé les éléments suivants :

* Testé **Piper TTS** (:ref:`test_piper`) et choisi un modèle vocal fonctionnel.
* Testé **Vosk STT** (:ref:`test_vosk`) et choisi le bon pack linguistique (par exemple, ``en-us``).
* Installé **Ollama** (:ref:`download_ollama`) sur votre Pi ou un autre ordinateur, et téléchargé un modèle comme ``llama3.2:3b`` (ou un plus petit comme ``moondream:1.8b`` si la mémoire est limitée).

----

Exécuter le code
----------------

#. Ouvrez le script d'exemple :

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano local_voice_chatbot.py

#. Mettez à jour les paramètres si nécessaire :

   * ``stt = Vosk(language="en-us")`` : Modifiez ceci pour correspondre à votre accent/pack linguistique (par exemple, ``en-us``, ``zh-cn``, ``es``).
   * ``tts.set_model("en_US-amy-low")`` : Remplacez par le modèle vocal Piper que vous avez vérifié dans :ref:`test_piper`.
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")`` : Mettez à jour à la fois ``ip`` et ``model`` selon votre propre configuration.

     * ``ip`` : Si Ollama fonctionne sur le **même Pi**, utilisez ``localhost``. Si Ollama fonctionne sur un autre ordinateur de votre LAN, activez **Exposer au réseau** dans Ollama et définissez ``ip`` sur l'adresse IP LAN de cet ordinateur.
     * ``model`` : Doit correspondre exactement au nom du modèle que vous avez téléchargé/activé dans Ollama.

#. Exécutez le script :

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo python3 local_voice_chatbot.py

#. Après l'exécution, vous devriez voir :

   * Le bot vous salue avec un message de bienvenue vocal.
   * Il attend une entrée vocale.
   * Vosk transcrit votre discours en texte.
   * Le texte est envoyé à Ollama, qui diffuse une réponse.
   * La réponse est nettoyée (suppression du raisonnement caché) et prononcée à voix haute par Piper.
   * Arrêtez le programme à tout moment avec ``Ctrl+C``.

----

Code
----

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.lm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

   # Initialiser la reconnaissance vocale
   stt = Vosk(language="en-us")

   # Initialiser la TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instructions pour le LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Initialiser la connexion Ollama
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utilitaire : supprimer le raisonnement caché
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 Écoute... (Appuyez sur Ctrl+C pour arrêter)")

               # Récupérer la transcription finale de Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f[VOUS] {text}")
                   else:
                       print(f"[VOUS] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Rien n'a été reconnu. Réessayez.")
                   time.sleep(0.1)
                   continue

               # Interroger Ollama avec streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Nettoyer et parler
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Arrêt en cours...")
       finally:
           tts.say("Goodbye!")
           print("Au revoir.")

   if __name__ == "__main__":
       main()

----

Analyse du code
---------------

**Importations et configuration globale**

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.lm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

Importe les trois sous-systèmes que vous avez construits précédemment :
**Vosk** pour la reconnaissance vocale (STT), **Ollama** pour le LLM, et **Piper** pour la synthèse vocale (TTS).

**Initialiser la STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Charge le modèle Vosk pour l'anglais américain.
Changez le code de langue (par exemple, ``zh-cn``, ``es``) pour correspondre à votre pack vocal pour une meilleure précision.

**Initialiser la TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Crée un moteur Piper et sélectionne une voix spécifique.
Choisissez un modèle que vous avez testé dans :ref:`test_piper`. Les voix de qualité inférieure sont plus rapides et utilisent moins de CPU.

**Instructions LLM et message de bienvenue**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Deux choix clés pour l'expérience utilisateur :

* Garder les **réponses courtes et directes** (aide à la clarté de la TTS).
* Interdire explicitement les balises de « chaîne de pensée » cachées pour réduire les sorties bruitées.

**Se connecter à Ollama et définir le périmètre de conversation**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` suppose que le serveur Ollama fonctionne sur le même Pi. S'il fonctionne sur une autre machine du LAN, mettez l'**adresse IP LAN** de cet ordinateur et activez *Exposer au réseau* dans Ollama.
* ``set_max_messages(20)`` conserve un historique de conversation court. Réduisez ceci si la mémoire/la latence est limitée.

**Supprimer le raisonnement / balises cachés avant de parler**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Certains modèles peuvent émettre des balises de style interne (par exemple, ``<think>…``).
Cette fonction les supprime afin que votre TTS **ne prononce** que la réponse finale.

**Astuce :** Si vous voyez d'autres artefacts à l'écran (parce que vous diffusez des jetons bruts), cette fonction garantit déjà que la sortie **parlée** reste propre.

**Boucle principale : saluer une fois, puis écouter → penser → parler**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Saluer l'utilisateur via le terminal et le haut-parleur. Se produit une fois au démarrage.

**Écouter (STT en streaming avec partiels en direct)**

.. code-block:: python

   print("\n🎤 Écoute... (Appuyez sur Ctrl+C pour arrêter)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[VOUS] {text}")
       else:
           print(f"[VOUS] {result['partial']}", end="\r", flush=True)

* ``stream=True`` produit des transcriptions **partielles** pour un retour immédiat et une transcription **finale** lorsque l'énoncé se termine.
* Le texte reconnu final est stocké dans ``text`` et imprimé une fois.

**Garde :** Si rien n'a été reconnu, vous sautez l'appel LLM :

.. code-block:: python

   if not text:
       print("[INFO] Rien n'a été reconnu. Réessayez.")
       time.sleep(0.1)
       continue

Cela évite d'envoyer des invites vides au modèle (économie de temps et de jetons).

**Penser (LLM) avec impression en streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Envoie la transcription finale au LLM local et **imprime les jetons à leur arrivée** pour une faible latence.
* Pendant ce temps, vous accumulez la réponse complète dans ``reply_accum`` pour le post-traitement.

**Remarque :** Si vous préférez **ne pas** afficher les jetons bruts, définissez ``stream=False`` et imprimez simplement la chaîne finale.

**Parler (nettoyer d'abord, puis TTS une fois)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Nettoie le texte final pour supprimer les balises cachées, puis **parle exactement une fois**.
* Garder la TTS sur un seul passage évite les invites répétées comme « [LLM] / [SAY] ».

**Sortie et nettoyage**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Arrêt en cours...")
   finally:
       tts.say("Goodbye!")
       print("Au revoir.")

Utilisez **Ctrl+C** pour arrêter. Le bot dit un court au revoir pour signaler une sortie propre.

----

Dépannage et FAQ
----------------

* **Le modèle est trop gros (erreur de mémoire)**

  Utilisez un modèle plus petit comme ``moondream:1.8b`` ou exécutez Ollama sur un ordinateur plus puissant.

* **Pas de réponse d'Ollama**

  Assurez-vous qu'Ollama est en cours d'exécution (``ollama serve`` ou application de bureau ouverte). Si distant, activez **Exposer au réseau** et vérifiez l'adresse IP.

* **Vosk ne reconnaît pas la parole**

  Vérifiez que votre microphone fonctionne. Essayez un autre pack linguistique (``zh-cn``, ``es``, etc.) si nécessaire.

* **Piper silencieux ou erreurs**

  Confirmez que le modèle vocal choisi est téléchargé et testé dans :ref:`test_piper`.

* **Réponses trop longues ou hors sujet**

  Modifiez ``INSTRUCTIONS`` pour ajouter : **« Keep answers short and to the point. »**