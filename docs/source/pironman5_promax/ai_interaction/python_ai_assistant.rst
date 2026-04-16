
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _ai_voice_assistant_car:

7. Assistant Vocal IA
=======================

Cette leçon transforme votre Pironman 5 Pro MAX en **assistant IA axé sur la voix**.  
Avec le code fourni, le robot va : **attendre un mot de réveil**, **transcrire votre discours** avec Vosk, l'envoyer à un **LLM OpenAI**, et **répondre vocalement** en utilisant Piper TTS.

----

Avant de commencer
------------------

Assurez-vous d'avoir :

* :ref:`test_piper` — La voix Piper fonctionne (par exemple, vous pouvez lire « Hello »).  
* :ref:`test_vosk` — La STT Vosk fonctionne pour votre langue (par exemple, ``en-us``).  
* :ref:`py_online_llm` — Votre **clé API OpenAI** enregistrée dans ``secret.py`` sous le nom ``OPENAI_API_KEY``.  
* Un **microphone** et un **haut-parleur** fonctionnels sur le Pironman 5 Pro MAX.  
* Une connexion réseau stable (le LLM est en ligne).

----

Exécuter l'exemple
------------------

.. code-block:: bash

   cd ~/sunfounder-voice-assistant/examples/
   sudo python3 voice_assistant.py

**Configuration utilisée par le code :**

* LLM : **OpenAI** (``gpt-4o-mini``)  
* TTS : **Piper** (``en_US-ryan-low``)  
* STT : **Vosk** (``en-us``)  
* Mot de réveil : ``"hey buddy"``  
* Saisie clavier : **activée** (saisie manuelle optionnelle)  
* Mode image : **activé** (``WITH_IMAGE=True``) — nécessite un LLM multimodal si vous décidez d'utiliser des images plus tard

**Ce qui se passe :**

1. L'assistant affiche un message de bienvenue avec la phrase de réveil.  
2. Il écoute **« hey buddy »**.  
3. Après le réveil, votre discours est transcrit (Vosk → texte).  
4. Le texte est envoyé à **OpenAI (gpt-4o-mini)** pour obtenir une réponse.  
5. La réponse est vocalisée avec **Piper** (``en_US-ryan-low``).

**Exemple d'interaction**

.. code-block:: text

   Vous : Hey Buddy
   Robot : Bonjour !

   Vous : Quelle est la capitale de l'Italie ?
   Robot : La capitale de l'Italie est Rome.

Code
-----------------

.. code-block:: python

  from sunfounder_voice_assistant.voice_assistant import VoiceAssistant
  from sunfounder_voice_assistant.llm import OpenAI as LLM
  from secret import OPENAI_API_KEY as API_KEY

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Nom du robot
  NAME = "Buddy"

  # Activer l'image, nécessite un modèle de langage multimodal
  WITH_IMAGE = True

  # Définir les modèles et langues
  LLM_MODEL = "gpt-4o-mini"
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

  # Activer la saisie clavier
  KEYBOARD_ENABLE = True

  # Activer le mot de réveil
  WAKE_ENABLE = True
  WAKE_WORD = [f"hey {NAME.lower()}"]
  # Définir la réponse au réveil, laisser vide pour désactiver
  ANSWER_ON_WAKE = "Bonjour"

  # Message de bienvenue
  WELCOME = f"Bonjour, je suis {NAME}. Réveillez-moi avec : " + ", ".join(WAKE_WORD)

  # Définir les instructions
  INSTRUCTIONS = f"""
  Vous êtes un assistant utile, nommé {NAME}.
  """

  va = VoiceAssistant(
      llm,
      name=NAME,
      with_image=WITH_IMAGE,
      tts_model=TTS_MODEL,
      stt_language=STT_LANGUAGE,
      keyboard_enable=KEYBOARD_ENABLE,
      wake_enable=WAKE_ENABLE,
      wake_word=WAKE_WORD,
      answer_on_wake=ANSWER_ON_WAKE,
      welcome=WELCOME,
      instructions=INSTRUCTIONS,
  )

  if __name__ == "__main__":
      va.run()

**Explication du code :**

* ``OpenAI(..., model="gpt-4o-mini")`` — Utilise **OpenAI** comme seul LLM dans cette leçon.  
* ``NAME`` / ``WAKE_WORD`` — Personnalise l'assistant (« Buddy », « hey buddy »).  
* ``WITH_IMAGE=True`` — Active le mode image dans l'assistant (aucune logique d'entrée/sortie d'image incluse ici).  
* ``TTS_MODEL="en_US-ryan-low"`` — Voix Piper utilisée pour les réponses.  
* ``STT_LANGUAGE="en-us"`` — Langue Vosk pour la reconnaissance.  
* ``KEYBOARD_ENABLE=True`` — Permet une saisie manuelle optionnelle pendant le débogage.  
* ``WELCOME`` / ``INSTRUCTIONS`` — Message de démarrage et personnalité / instruction système de l'assistant.  
* ``va.run()`` — Démarre la boucle : **réveil → écoute → LLM → parole**.

Changer de LLM ou de TTS
------------------------

Vous pouvez facilement changer de LLM, de TTS ou de langue STT avec seulement quelques modifications :

* LLM supportés :

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Vérifiez les langues supportées par **Piper TTS**.  
* :ref:`test_vosk` — Vérifiez les langues supportées par **Vosk STT**.  

Pour changer, modifiez simplement la partie initialisation dans le code :

.. code-block:: python

   from sunfounder_voice_assistant.llm import Gemini as LLM
   llm = LLM(api_key="VOTRE_CLÉ", model="gemini-pro")

   # Définir les modèles et langues
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

----

Dépannage
-----------------------------

* **Le robot ne répond pas au mot de réveil**

  - Vérifiez que le microphone fonctionne.  
  - Assurez-vous que ``WAKE_ENABLE = True``.  
  - Ajustez le mot de réveil pour qu'il corresponde à votre prononciation.  
  - Réduisez le bruit de fond et parlez clairement.

* **Aucun son du haut-parleur**

  - Vérifiez le nom du modèle TTS (par exemple, ``en_US-ryan-low``).  
  - Testez Piper ou Espeak manuellement.  
  - Vérifiez la connexion du haut-parleur et le volume.

* **Erreur de clé API ou timeout**

  - Vérifiez votre clé dans ``secret.py``.  
  - Assurez-vous que votre connexion réseau est stable.  
  - Confirmez que le modèle LLM est supporté (par exemple, ``gpt-4o-mini``).

* **Le mot de réveil fonctionne mais pas de réponse**

  - Vérifiez que la langue STT correspond à votre accent.  
  - Assurez-vous que le modèle a été téléchargé correctement.  
  - Essayez d'afficher les journaux de débogage pour confirmer que la STT fonctionne.

* **La TTS fonctionne mais pas de réponse du LLM**

  - Vérifiez que la clé API est valide.  
  - Vérifiez le nom du modèle et les paramètres du LLM.  
  - Assurez-vous d'avoir une connexion Internet.