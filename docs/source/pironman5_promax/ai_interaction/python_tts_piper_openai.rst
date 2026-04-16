.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



2. TTS avec Piper et OpenAI
========================================================

Dans la leçon précédente, nous avons exploré **Espeak** et **Pico2Wave**, deux moteurs TTS hors ligne simples sur Raspberry Pi.
Maintenant, faisons un grand pas en avant et essayons deux **options TTS plus avancées** qui offrent une **meilleure qualité vocale** et plus de flexibilité :

* **Piper** — un moteur TTS rapide basé sur des réseaux de neurones qui fonctionne **complètement hors ligne** sur Raspberry Pi.
* **OpenAI TTS** — un service en ligne qui fournit des **voix très naturelles et humaines**, parfait pour une parole expressive.

Ces moteurs rendront votre Pironman 5 Pro MAX plus réaliste et vivant. 🚀

----

.. _test_piper:

1. Tester Piper
------------------

Piper est un **moteur TTS neuronal hors ligne**, ce qui signifie que vous n'avez pas besoin de connexion Internet une fois le modèle installé.
Il prend en charge plusieurs **langues** et **voix**, ce qui en fait une option puissante pour la parole embarquée.

**Exécuter le programme**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_piper.py

* La première fois que vous l'exécutez, le **modèle vocal** sélectionné sera téléchargé automatiquement.
* Vous devriez ensuite entendre le Pironman 5 Pro MAX dire : ``Hello! I'm Piper TTS.``
* Vous pouvez changer de voix ou de langue en appelant ``set_model()`` avec un nom de modèle différent.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Piper

  tts = Piper()

  # Lister les langues supportées
  print(tts.available_countrys())

  # Lister les modèles pour l'anglais (en_us)
  print(tts.available_models('en_us'))

  # Définir un modèle vocal (téléchargement automatique s'il n'est pas déjà présent)
  tts.set_model("en_US-amy-low")

  # Dire quelque chose
  tts.say("Hello! I'm Piper TTS.")

**Explication du code :**

* ``available_countrys()`` — Liste toutes les langues supportées.
* ``available_models()`` — Liste les modèles disponibles pour une langue spécifique.
* ``set_model()`` — Définit le modèle vocal. Si le modèle n'est pas installé, il sera téléchargé automatiquement.
* ``say()`` — Convertit le texte en parole et le lit immédiatement.

💡 **Astuce :** Essayez différents modèles pour comparer la vitesse, la clarté et les accents. Certains modèles sont plus légers (plus rapides), tandis que d'autres ont une fidélité plus élevée.

----

2. Tester OpenAI TTS
-------------------------------

**Obtenir et sauvegarder votre clé API**

#. Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Remplissez les détails (Propriétaire, Nom, Projet et autorisations si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devez en générer une nouvelle.

   .. image:: img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/``), créez un fichier appelé ``secret.py`` :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Collez votre clé dans le fichier comme ceci :

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Exécuter le programme**

.. code-block:: bash

  cd ~/sunfounder-voice-assistant/examples
  sudo python3 tts_openai.py

* Le programme se connectera au service TTS d'OpenAI, et le Pironman 5 Pro MAX parlera en utilisant une **sortie vocale naturelle et expressive**.
* Vous pouvez changer les **styles de voix** et ajouter des **instructions** pour contrôler le ton et l'expression (par exemple, triste, dramatique, enjoué).
* Cela rend OpenAI TTS idéal pour les robots interactifs, la narration ou les assistants éducatifs.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import OpenAI_TTS
  from secret import OPENAI_API_KEY

  # Exportez votre OPENAI_API_KEY avant d'exécuter le script
  # export OPENAI_API_KEY="sk-proj-xxxxxx"

  tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
  # tts.set_model('tts-1')
  tts.set_voice('alloy')
  tts.set_model('gpt-4o-mini-tts')

  msg = "Hello! I'm OpenAI TTS."
  print(f"Say: {msg}")
  tts.say(msg)

  msg = "with instructions, I can say word sadly"
  instructions = "say it sadly"
  print(f"Say: {msg}, with instructions: '{instructions}'")
  tts.say(msg, instructions=instructions)

  msg = "or say something dramaticly."
  instructions = "say it dramaticly"
  print(f"Say: {msg}, with instructions: '{instructions}'")
  tts.say(msg, instructions=instructions)

**Explication du code :**

* ``OpenAI_TTS()`` — Initialise le moteur TTS OpenAI en utilisant votre clé API.
* ``set_model()`` — Sélectionne le modèle TTS (par exemple, ``gpt-4o-mini-tts``).
* ``set_voice()`` — Choisit une voix spécifique (par exemple, ``alloy``).
* ``say(text)`` — Convertit le texte en parole et le lit.
* ``say(text, instructions=...)`` — Ajoute des **instructions de ton expressives**, vous permettant de contrôler dynamiquement le style de parole.

**Exemple :**

- « say it sadly » → ton doux et émotionnel
- « say it dramatically » → expression audacieuse et dramatique
- « say it excitedly » → ton enthousiaste

----

Dépannage
-------------------

* **Pas de module nommé 'secret'**

  Cela signifie que ``secret.py`` n'est pas dans le même dossier que votre fichier Python.
  Déplacez ``secret.py`` dans le même répertoire où vous exécutez le script, par exemple :

  .. code-block:: bash

     ls ~/
     # Assurez-vous de voir les deux : secret.py et votre fichier .py

* **OpenAI : Clé API invalide / 401**

  * Vérifiez que vous avez collé la clé complète (commence par ``sk-``) et qu'il n'y a pas d'espaces ou de sauts de ligne supplémentaires.
  * Assurez-vous que votre code l'importe correctement :

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirmez l'accès réseau sur votre Pi (essayez ``ping api.openai.com``).

* **OpenAI : Quota dépassé / erreur de facturation**

  * Vous devrez peut-être ajouter un moyen de paiement ou augmenter le quota dans le tableau de bord OpenAI.
  * Réessayez après avoir résolu le problème de compte/facturation.

* **Piper : tts.say() s'exécute mais pas de son**

  * Assurez-vous qu'un modèle vocal est réellement présent :

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Confirmez que le nom de votre modèle correspond exactement dans le code :

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Vérifiez le périphérique/volume de sortie audio sur votre Pi (``alsamixer``), et que les haut-parleurs sont connectés et alimentés.

* **Erreurs ALSA / périphérique sonore (par exemple, « Audio device busy » ou « No such file or directory »)**

  * Fermez les autres programmes utilisant l'audio.
  * Redémarrez le Pi si le périphérique reste occupé.
  * Pour la sortie HDMI par rapport à la prise casque, sélectionnez le périphérique correct dans les paramètres audio de Raspberry Pi OS.

* **Permission refusée lors de l'exécution de Python**

  * Essayez avec ``sudo`` si votre environnement l'exige :

    .. code-block:: bash

       sudo python3 tts_piper.py

Comparaison des moteurs TTS
--------------------------------------------

.. list-table:: Comparaison des fonctionnalités : Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Élément
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Fonctionne sur
     - Intégré sur Raspberry Pi (hors ligne)
     - Intégré sur Raspberry Pi (hors ligne)
     - Raspberry Pi / PC (hors ligne, besoin du modèle)
     - Cloud (en ligne, besoin de clé API)
   * - Qualité vocale
     - Robotique
     - Plus naturelle qu'Espeak
     - Naturelle (TTS neuronal)
     - Très naturelle / humaine
   * - Contrôles
     - Vitesse, hauteur tonale, volume
     - Contrôles limités
     - Choisir différentes voix/modèles
     - Choisir modèle et voix
   * - Langues
     - Beaucoup (qualité variable)
     - Ensemble limité
     - Beaucoup de voix/langues disponibles
     - Meilleur en anglais (autres variables selon disponibilité)
   * - Latence / vitesse
     - Très rapide
     - Rapide
     - Temps réel sur Pi 4/5 avec modèles « low »
     - Dépend du réseau (généralement faible latence)
   * - Configuration
     - Minimale
     - Minimale
     - Télécharger les modèles ``.onnx`` + ``.onnx.json``
     - Créer une clé API, installer le client
   * - Idéal pour
     - Tests rapides, invites basiques
     - Voix hors ligne légèrement meilleure
     - Projets locaux avec meilleure qualité
     - Qualité la plus élevée, options vocales riches