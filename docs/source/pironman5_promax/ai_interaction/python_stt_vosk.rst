.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



3. STT avec Vosk (Hors ligne)
==============================================

Vosk est un moteur de reconnaissance vocale (STT) léger qui prend en charge de nombreuses langues et fonctionne entièrement **hors ligne** sur Raspberry Pi.
Vous n'avez besoin d'une connexion Internet qu'une seule fois pour télécharger un modèle linguistique. Après cela, tout fonctionne sans connexion réseau.

Dans cette leçon, nous allons installer et tester Vosk avec un modèle linguistique de votre choix.

.. _test_vosk:

Tester Vosk
--------------------------

**Exécuter le programme**

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 stt_vosk_stream.py

La première fois que vous exécutez ce code avec une nouvelle langue, Vosk va :

* **Télécharger automatiquement le modèle linguistique** (par défaut, la version petite).
* **Afficher la liste des langues supportées**.
* Commencer à **écouter** les entrées audio via le microphone.

Vous verrez quelque chose comme ceci dans le terminal :

.. code-block:: text

         vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
         ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
         Dites quelque chose

Cela signifie :

   * Le fichier modèle (``vosk-model-small-en-us-0.15``) a été téléchargé.
   * La liste des langues supportées a été affichée.
   * Le système écoute maintenant — dites quelque chose dans le microphone du Pironman 5 Pro MAX, et le texte reconnu apparaîtra dans le terminal.

**Conseils :**

* Gardez le microphone à environ **15–30 cm** pour une meilleure précision.
* Choisissez un **modèle qui correspond à votre langue et à votre accent**.
* Utilisez un environnement calme pour améliorer la reconnaissance.

**Code**

.. code-block:: python

   from sunfounder_voice_assistant.stt import Vosk as STT

   stt = STT(language="en-us")

   while True:
      print("Dites quelque chose")
      for result in stt.listen(stream=True):
         if result["done"]:
               print(f"final:   {result['final']}")
         else:
               print(f"partiel: {result['partial']}", end="\r", flush=True)

**Explication du code :**

* ``stt.listen(stream=True)`` — Démarre la reconnaissance vocale en streaming et produit des résultats intermédiaires pendant que vous parlez.
* ``result["partial"]`` — Affiche le **texte reconnu en temps réel** (mis à jour en continu).
* ``result["final"]`` — Affiche la **phrase finale reconnue** lorsque vous arrêtez de parler.
* La boucle s'exécute en continu, permettant une **transcription en temps réel mains libres**.

Astuce : Ce mode streaming est parfait pour les **assistants vocaux**, le **contrôle par commande vocale** ou la **transcription en direct**.

Dépannage
-----------------

* **Aucun fichier ou dossier de ce type (lors de l'exécution de `arecord`)**

  Vous avez peut-être utilisé le mauvais numéro de carte/périphérique.
  Exécutez :

  .. code-block:: bash

     arecord -l

  et remplacez ``1,0`` par les numéros affichés pour votre microphone USB.

* **Le fichier enregistré n'a pas de son**

  Ouvrez le mixer et vérifiez le volume du microphone :

  .. code-block:: bash

     alsamixer

  * Appuyez sur **F6** pour sélectionner votre microphone USB.
  * Assurez-vous que **Mic/Capture** n'est pas en sourdine (**[OO]** au lieu de **[MM]**).
  * Augmentez le niveau avec la flèche ↑.

* **Vosk ne reconnaît pas la parole**

  * Assurez-vous que le **code de langue** correspond à votre modèle (par exemple ``en-us`` pour l'anglais, ``zh-cn`` pour le chinois).
  * Gardez le microphone à 15–30 cm et évitez le bruit de fond.
  * Parlez clairement et lentement.

* **Latence élevée / reconnaissance lente**

  * Le téléchargement automatique par défaut est un **petit modèle** (plus rapide, mais moins précis).
  * Si c'est encore lent, fermez les autres programmes pour libérer du CPU.
