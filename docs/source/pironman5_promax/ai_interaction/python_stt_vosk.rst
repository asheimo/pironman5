
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

3. STT con Vosk (Offline)
==============================================

Vosk è un motore di riconoscimento vocale (STT) leggero che supporta molte lingue e funziona completamente **offline** su Raspberry Pi.
È necessario solo l'accesso a Internet una volta per scaricare un modello linguistico. Dopodiché, tutto funziona senza connessione di rete.

In questa lezione, installeremo e testeremo Vosk con un modello linguistico a scelta.

.. _test_vosk:

Testare Vosk
--------------------------

**Eseguire il programma**

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 stt_vosk_stream.py

La prima volta che esegui questo codice con una nuova lingua, Vosk:

* **Scaricherà automaticamente il modello linguistico** (di default, la versione piccola).
* **Stamperà l'elenco delle lingue supportate**.
* Inizierà **ad ascoltare** l'input audio attraverso il microfono.

Vedrai qualcosa del genere nel terminale:

.. code-block:: text

         vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
         ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
         Say something

Questo significa:

   * Il file del modello (``vosk-model-small-en-us-0.15``) è stato scaricato.
   * L'elenco delle lingue supportate è stato stampato.
   * Il sistema ora è in ascolto — pronuncia qualcosa nel microfono del Pironman 5 Pro MAX, e il testo riconosciuto apparirà nel terminale.

**Suggerimenti:**

* Tieni il microfono a circa **15–30 cm** di distanza per una migliore precisione.
* Scegli un **modello che corrisponda alla tua lingua e al tuo accento**.
* Utilizza un ambiente silenzioso per migliorare il riconoscimento.

**Codice**

.. code-block:: python

   from sunfounder_voice_assistant.stt import Vosk as STT

   stt = STT(language="en-us")

   while True:
      print("Say something")
      for result in stt.listen(stream=True):
         if result["done"]:
               print(f"final:   {result['final']}")
         else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

**Spiegazione del codice:**

* ``stt.listen(stream=True)`` — Avvia il riconoscimento vocale in streaming e produce risultati intermedi mentre parli.
* ``result["partial"]`` — Mostra il **testo riconosciuto in tempo reale** (aggiornato continuamente).
* ``result["final"]`` — Mostra la **frase finale riconosciuta** quando smetti di parlare.
* Il ciclo continua all'infinito, consentendo una **trascrizione in tempo reale a mani libere**.

Suggerimento: Questa modalità di streaming è perfetta per **assistenti vocali**, **controllo a comando**, o **trascrizione in diretta**.

Risoluzione dei Problemi
-------------------------

* **Nessun file o directory (durante l'esecuzione di `arecord`)**

  Potresti aver usato il numero di scheda/dispositivo sbagliato.
  Esegui:

  .. code-block:: bash

     arecord -l

  e sostituisci ``1,0`` con i numeri mostrati per il tuo microfono USB.

* **Il file registrato non ha suono**

  Apri il mixer e controlla il volume del microfono:

  .. code-block:: bash

     alsamixer

  * Premi **F6** per selezionare il tuo microfono USB.
  * Assicurati che **Mic/Capture** non sia disattivato (**[OO]** invece di **[MM]**).
  * Aumenta il livello con il tasto ↑.

* **Vosk non riconosce il parlato**

  * Assicurati che il **codice lingua** corrisponda al tuo modello (es., ``en-us`` per l'inglese, ``zh-cn`` per il cinese).
  * Tieni il microfono a 15–30 cm di distanza ed evita il rumore di fondo.
  * Parla chiaramente e lentamente.

* **Latenza elevata / riconoscimento lento**

  * Il download automatico predefinito è un **modello piccolo** (più veloce, ma meno preciso).
  * Se è ancora lento, chiudi altri programmi per liberare CPU.
