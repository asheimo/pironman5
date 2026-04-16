.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



4. Dialogue avec Vision Texte via Ollama
=========================================

Dans cette leçon, vous apprendrez à utiliser **Ollama**, un outil permettant d'exécuter localement de grands modèles de langage et de vision.
Nous allons vous montrer comment installer Ollama, télécharger un modèle et connecter le Pironman 5 Pro MAX à celui-ci.

Avec cette configuration, le Pironman 5 Pro MAX peut prendre une photo avec la caméra et le modèle **verra et racontera** —
vous pouvez poser n'importe quelle question sur l'image, et le modèle répondra en langage naturel.

.. _download_ollama:

1. Installer Ollama (LLM) et télécharger un modèle
-----------------------------------------------------------------

Vous pouvez choisir où installer **Ollama** :

* Sur votre Raspberry Pi (exécution locale)
* Ou sur un autre ordinateur (Mac/Windows/Linux) sur le **même réseau local**

**Modèles recommandés vs matériel**

Vous pouvez choisir n'importe quel modèle disponible sur |link_ollama_hub|.
Les modèles existent en différentes tailles (3B, 7B, 13B, 70B...).
Les modèles plus petits s'exécutent plus rapidement et nécessitent moins de mémoire, tandis que les modèles plus grands offrent une meilleure qualité mais nécessitent du matériel puissant.

Consultez le tableau ci-dessous pour déterminer quelle taille de modèle correspond à votre appareil.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Taille du modèle
     - RAM minimale requise
     - Matériel recommandé
   * - ~3B paramètres
     - 8 Go (16 Go mieux)
     - Raspberry Pi 5 (16 Go) ou PC/Mac milieu de gamme
   * - ~7B paramètres
     - 16 Go+
     - Pi 5 (16 Go, juste utilisable) ou PC/Mac milieu de gamme
   * - ~13B paramètres
     - 32 Go+
     - PC de bureau / Mac avec RAM élevée
   * - 30B+ paramètres
     - 64 Go+
     - Station de travail / Serveur / GPU recommandé
   * - 70B+ paramètres
     - 128 Go+
     - Serveur haut de gamme avec GPU multiples

**Installer sur Raspberry Pi**

Si vous souhaitez exécuter Ollama directement sur votre Raspberry Pi :

* Utilisez un **Raspberry Pi OS 64 bits**
* Fortement recommandé : **Raspberry Pi 5 (16 Go RAM)**

Exécutez les commandes suivantes :

.. code-block:: bash

   # Installer Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Télécharger un modèle léger (bon pour les tests)
   ollama pull llama3.2:3b

   # Test d'exécution rapide (tapez 'hi' et appuyez sur Entrée)
   ollama run llama3.2:3b

   # Servir l'API (port par défaut 11434)
   # Astuce : définissez OLLAMA_HOST=0.0.0.0 pour autoriser l'accès depuis le LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installer sur Mac / Windows / Linux (application de bureau)**

1. Téléchargez et installez Ollama depuis |link_ollama|

   .. image:: img/llm_ollama_download.png

2. Ouvrez l'application Ollama, allez dans le **Sélecteur de modèles** et utilisez la barre de recherche pour trouver un modèle. Par exemple, tapez ``llama3.2:3b`` (un modèle petit et léger pour commencer).

   .. image:: img/llm_ollama_choose.png

3. Une fois le téléchargement terminé, tapez quelque chose de simple comme « Hi » dans la fenêtre de chat, Ollama commencera automatiquement à le télécharger lors de la première utilisation.

   .. image:: img/llm_olama_llama_download.png

4. Allez dans **Paramètres** → activez **Exposer Ollama au réseau**. Cela permet à votre Raspberry Pi de s'y connecter via le LAN.

   .. image:: img/llm_olama_windows_enable.png

.. attention::

   Si vous voyez une erreur comme :

   ``Error: model requires more system memory ...``

   Le modèle est trop gros pour votre machine.
   Utilisez un **modèle plus petit** ou passez à un ordinateur avec plus de RAM.

2. Tester Ollama
------------------------------

Une fois Ollama installé et votre modèle prêt, vous pouvez le tester rapidement avec une boucle de chat minimale.

**Exécuter le programme**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 llm_ollama.py

Vous pouvez maintenant discuter avec le Pironman 5 Pro MAX directement depuis le terminal.

   * Vous pouvez choisir **n'importe quel modèle** disponible sur |link_ollama_hub|, mais les modèles plus petits (par exemple ``moondream:1.8b``, ``phi3:mini``) sont recommandés si vous n'avez que 8–16 Go de RAM.
   * Assurez-vous que le modèle que vous spécifiez dans le code correspond au modèle que vous avez déjà téléchargé dans Ollama.
   * Tapez ``exit`` ou ``quit`` pour arrêter le programme.
   * Si vous ne pouvez pas vous connecter, assurez-vous qu'Ollama est en cours d'exécution et que les deux appareils sont sur le même LAN si vous utilisez un hôte distant.

**Code**

.. code-block:: python

   from sunfounder_voice_assistant.lm import Ollama

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # Changez ceci par l'adresse IP de votre ordinateur, si vous l'exécutez sur votre pi, changez-le en localhost
   llm = Ollama(
      ip="localhost",
      model="llama3.2:3b"
   )

   # Définir combien de messages conserver
   llm.set_max_messages(20)
   # Définir les instructions
   llm.set_instructions(INSTRUCTIONS)
   # Définir le message de bienvenue
   llm.set_welcome(WELCOME)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # Réponse sans flux
      # response = llm.prompt(input_text)
      # print(f"response: {response}")

      # Réponse avec flux
      response = llm.prompt(input_text, stream=True)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")

3. Dialogue avec Vision via Ollama
--------------------------------------------------

Dans cette démo, la caméra du Pi prend une photo **chaque fois que vous tapez une question**.
Le programme envoie **votre texte tapé + la nouvelle photo** à un modèle de vision local via Ollama,
puis diffuse la réponse du modèle en anglais simple.
C'est une base minimale « voir et raconter » que vous pourrez ensuite étendre avec des vérifications de couleur/visage/QR.

**Avant de commencer**

#. Ouvrez l'application **Ollama** (ou exécutez le service) et assurez-vous qu'un **modèle capable de vision** est téléchargé.

   * Si vous avez suffisamment de mémoire (≥16 Go de RAM), vous pouvez essayer ``llava:7b``.
   * Si vous n'avez que **8 Go de RAM**, préférez un modèle plus petit comme ``moondream:1.8b`` ou ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Exécuter la démo**

#. Allez dans le dossier des exemples et exécutez le script :

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      python3 llm_ollama_with_image.py

#. Ce qui se passe lors de l'exécution :

   * Le programme affiche une ligne de bienvenue et attend votre saisie (``>>>``).
   * **Chaque fois que vous tapez quelque chose** (par exemple, « hello », « Y a-t-il du jaune ? », « Des visages ? », « Qu'y a-t-il sur le bureau ? »), il :

     * **capture une photo** depuis la caméra du Pi (enregistrée dans ``/tmp/llm-img.jpg``),
     * **envoie votre texte + la photo** au modèle de vision via Ollama,
     * **diffuse** la réponse du modèle dans le terminal.

   * Tapez ``exit`` ou ``quit`` pour terminer le programme.

**Code**

.. code-block:: python

   from sunfounder_voice_assistant.lm import Ollama
   from picamera2 import Picamera2
   import time

   '''
   Vous devez d'abord configurer ollama, voir llm_local.py

   Vous avez besoin d'au moins 8 Go de RAM pour exécuter le grand modèle multimodal llava:7b
   '''

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   llm = Ollama(
      ip="localhost",          # par exemple, "192.168.100.145" si distant
      model="llava:7b"         # remplacez par "moondream:1.8b" ou "granite3.2-vision:2b" pour 8 Go de RAM
   )

   # Définir combien de messages conserver
   llm.set_max_messages(20)
   # Définir les instructions
   llm.set_instructions(INSTRUCTIONS)
   # Définir le message de bienvenue
   llm.set_welcome(WELCOME)

   # Initialiser la caméra
   camera = Picamera2()
   config = camera.create_still_configuration(
      main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # Capturer l'image
      img_path = '/tmp/llm-img.jpg'
      camera.capture_file(img_path)

      # Réponse sans flux
      # response = llm.prompt(input_text, image_path=img_path)
      # print(f"response: {response}")

      # Réponse avec flux
      response = llm.prompt(input_text, stream=True, image_path=img_path)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")

Dépannage
---------

* **J'obtiens une erreur comme : `model requires more system memory ...`.**

  * Cela signifie que le modèle est trop gros pour votre appareil.
  * Utilisez un modèle plus petit comme ``moondream:1.8b`` ou ``granite3.2-vision:2b``.
  * Ou passez à une machine avec plus de RAM et exposez Ollama au réseau.

* **Le code ne peut pas se connecter à Ollama (connexion refusée).**

  Vérifiez les points suivants :

  * Assurez-vous qu'Ollama est en cours d'exécution (``ollama serve`` ou l'application de bureau est ouverte).
  * Si vous utilisez un ordinateur distant, activez **Exposer au réseau** dans les paramètres d'Ollama.
  * Vérifiez que ``ip="..."`` dans votre code correspond à la bonne adresse IP LAN.
  * Confirmez que les deux appareils sont sur le même réseau local.

* **Ma caméra Pi ne capture rien.**

  * Vérifiez que ``Picamera2`` est installé et fonctionne avec un simple script de test.
  * Vérifiez que le câble de la caméra est correctement connecté et activé dans ``raspi-config``.
  * Assurez-vous que votre script a la permission d'écrire sur le chemin cible (``/tmp/llm-img.jpg``).

* **La sortie est trop lente.**

  * Les modèles plus petits répondent plus rapidement, mais avec des réponses plus simples.
  * Vous pouvez réduire la résolution de la caméra (par exemple, 640×480 au lieu de 1280×720) pour accélérer le traitement d'image.
  * Fermez les autres programmes sur votre Pi pour libérer du CPU et de la RAM.