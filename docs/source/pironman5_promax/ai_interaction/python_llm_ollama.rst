
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

4. Conversazione Visiva Testuale con Ollama
=============================================

In questa lezione imparerai come utilizzare **Ollama**, uno strumento per eseguire localmente modelli linguistici e visivi di grandi dimensioni.
Ti mostreremo come installare Ollama, scaricare un modello e collegare Pironman 5 Pro MAX ad esso.

Con questa configurazione, Pironman 5 Pro MAX può scattare una foto con la fotocamera e il modello **vedrà e racconterà** —
puoi fare qualsiasi domanda sull'immagine e il modello risponderà in linguaggio naturale.

.. _download_ollama:

1. Installare Ollama (LLM) e Scaricare il Modello
----------------------------------------------------------------------------------

Puoi scegliere dove installare **Ollama**:

* Sul tuo Raspberry Pi (esecuzione locale)
* Oppure su un altro computer (Mac/Windows/Linux) nella **stessa rete locale**

**Modelli raccomandati vs hardware**

Puoi scegliere qualsiasi modello disponibile su |link_ollama_hub|.
I modelli hanno dimensioni diverse (3B, 7B, 13B, 70B...).
I modelli più piccoli sono più veloci e richiedono meno memoria, mentre i modelli più grandi offrono una qualità migliore ma necessitano di hardware potente.

Controlla la tabella qui sotto per decidere quale dimensione di modello si adatta al tuo dispositivo.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Dimensione del modello
     - RAM Minima Richiesta
     - Hardware Raccomandato
   * - ~3B parametri
     - 8GB (16GB meglio)
     - Raspberry Pi 5 (16GB) o PC/Mac di fascia media
   * - ~7B parametri
     - 16GB+
     - Pi 5 (16GB, appena utilizzabile) o PC/Mac di fascia media
   * - ~13B parametri
     - 32GB+
     - PC Desktop / Mac con alta RAM
   * - 30B+ parametri
     - 64GB+
     - Workstation / Server / GPU raccomandata
   * - 70B+ parametri
     - 128GB+
     - Server di fascia alta con GPU multiple

**Installare su Raspberry Pi**

Se vuoi eseguire Ollama direttamente sul tuo Raspberry Pi:

* Utilizza un **Raspberry Pi OS a 64 bit**
* Fortemente raccomandato: **Raspberry Pi 5 (16GB RAM)**

Esegui i seguenti comandi:

.. code-block:: bash

   # Installa Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Scarica un modello leggero (buono per i test)
   ollama pull llama3.2:3b

   # Test di esecuzione rapida (scrivi 'hi' e premi Invio)
   ollama run llama3.2:3b

   # Avvia l'API (porta predefinita 11434)
   # Suggerimento: imposta OLLAMA_HOST=0.0.0.0 per consentire l'accesso dalla LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installare su Mac / Windows / Linux (App Desktop)**

1. Scarica e installa Ollama da |link_ollama|

   .. image:: img/llm_ollama_download.png

2. Apri l'app Ollama, vai su **Model Selector** e utilizza la barra di ricerca per trovare un modello. Ad esempio, digita ``llama3.2:3b`` (un modello piccolo e leggero per iniziare).

   .. image:: img/llm_ollama_choose.png

3. Dopo il completamento del download, scrivi qualcosa di semplice come "Hi" nella finestra di chat. Ollama inizierà automaticamente a scaricarlo quando lo usi per la prima volta.

   .. image:: img/llm_olama_llama_download.png

4. Vai su **Settings** → attiva **Expose Ollama to the network**. Questo permette al tuo Raspberry Pi di connettersi ad esso tramite LAN.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Se vedi un errore come:

   ``Error: model requires more system memory ...``

   Il modello è troppo grande per la tua macchina.
   Utilizza un **modello più piccolo** o passa a un computer con più RAM.

2. Testare Ollama
------------------

Una volta installato Ollama e pronto il tuo modello, puoi testarlo rapidamente con un semplice ciclo di chat.

**Eseguire il programma**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 llm_ollama.py

Ora puoi chattare con Pironman 5 Pro MAX direttamente dal terminale.

   * Puoi scegliere **qualsiasi modello** disponibile su |link_ollama_hub|, ma i modelli più piccoli (es. ``moondream:1.8b``, ``phi3:mini``) sono raccomandati se hai solo 8–16GB di RAM.
   * Assicurati che il modello specificato nel codice corrisponda al modello che hai già scaricato in Ollama.
   * Digita ``exit`` o ``quit`` per fermare il programma.
   * Se non riesci a connetterti, assicurati che Ollama sia in esecuzione e che entrambi i dispositivi siano sulla stessa LAN se stai utilizzando un host remoto.

**Codice**

.. code-block:: python

   from sunfounder_voice_assistant.llm import Ollama

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # Cambia questo con l'IP del tuo computer, se lo esegui sul pi, cambialo in localhost
   llm = Ollama(
      ip="localhost",
      model="llama3.2:3b"
   )

   # Imposta quanti messaggi conservare
   llm.set_max_messages(20)
   # Imposta le istruzioni
   llm.set_instructions(INSTRUCTIONS)
   # Imposta il messaggio di benvenuto
   llm.set_welcome(WELCOME)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # Risposta senza stream
      # response = llm.prompt(input_text)
      # print(f"response: {response}")

      # Risposta con stream
      response = llm.prompt(input_text, stream=True)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")

3. Conversazione Visiva con Ollama
---------------------------------------------------------

In questa demo, la fotocamera del Pi scatta una foto **ogni volta che digiti una domanda**.
Il programma invia **il testo digitato + la nuova foto** a un modello visivo locale tramite Ollama,
e poi trasmette in streaming la risposta del modello in inglese semplice.
Questa è una base minima "vedi e racconta" che potrai successivamente estendere con controlli di colore/volto/QR.

**Prima di Iniziare**

#. Apri l'app **Ollama** (o esegui il servizio) e assicurati che un modello **in grado di elaborare immagini** sia stato scaricato.

   * Se hai abbastanza memoria (≥16GB RAM), puoi provare ``llava:7b``.
   * Se hai solo **8GB RAM**, preferisci un modello più piccolo come ``moondream:1.8b`` o ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Eseguire la Demo**

#. Vai alla cartella degli esempi ed esegui lo script:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      python3 llm_ollama_with_image.py

#. Cosa succede quando viene eseguito:

   * Il programma stampa una riga di benvenuto e attende il tuo input (``>>>``).
   * **Ogni volta che digiti qualcosa** (es., "hello", "Is there yellow?", "Any faces?", "What is on the desk?"), esso:

     * **acquisisce una foto** dalla fotocamera del Pi (salvata in ``/tmp/llm-img.jpg``),
     * **invia il testo + la foto** al modello visivo tramite Ollama,
     * **restituisce in streaming** la risposta del modello al terminale.

   * Digita ``exit`` o ``quit`` per terminare il programma.

**Codice**

.. code-block:: python

   from sunfounder_voice_assistant.llm import Ollama
   from picamera2 import Picamera2
   import time

   '''
   Devi configurare ollama prima, vedi llm_local.py

   Servono almeno 8GB di RAM per eseguire llava:7b (modello multimodale di grandi dimensioni)
   '''

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   llm = Ollama(
      ip="localhost",          # es., "192.168.100.145" se remoto
      model="llava:7b"         # cambia in "moondream:1.8b" o "granite3.2-vision:2b" per 8GB di RAM
   )

   # Imposta quanti messaggi conservare
   llm.set_max_messages(20)
   # Imposta le istruzioni
   llm.set_instructions(INSTRUCTIONS)
   # Imposta il messaggio di benvenuto
   llm.set_welcome(WELCOME)

   # Inizializza la fotocamera
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

      # Acquisisci immagine
      img_path = '/tmp/llm-img.jpg'
      camera.capture_file(img_path)

      # Risposta senza stream
      # response = llm.prompt(input_text, image_path=img_path)
      # print(f"response: {response}")

      # Risposta con stream
      response = llm.prompt(input_text, stream=True, image_path=img_path)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")

Risoluzione dei Problemi
--------------------------------------------------------------

* **Ricevo un errore come: `model requires more system memory ...`.**

  * Ciò significa che il modello è troppo grande per il tuo dispositivo.
  * Utilizza un modello più piccolo come ``moondream:1.8b`` o ``granite3.2-vision:2b``.
  * Oppure passa a una macchina con più RAM ed esponi Ollama alla rete.

* **Il codice non riesce a connettersi a Ollama (connessione rifiutata).**

  Verifica quanto segue:

  * Assicurati che Ollama sia in esecuzione (``ollama serve`` o l'app desktop è aperta).
  * Se utilizzi un computer remoto, attiva **Expose to network** nelle impostazioni di Ollama.
  * Ricontrolla che ``ip="..."`` nel tuo codice corrisponda al corretto IP LAN.
  * Conferma che entrambi i dispositivi siano sulla stessa rete locale.

* **La mia fotocamera Pi non acquisisce nulla.**

  * Verifica che ``Picamera2`` sia installato e funzioni con un semplice script di test.
  * Controlla che il cavo della fotocamera sia collegato correttamente e abilitato in ``raspi-config``.
  * Assicurati che il tuo script abbia il permesso di scrivere nel percorso di destinazione (``/tmp/llm-img.jpg``).

* **L'output è troppo lento.**

  * I modelli più piccoli rispondono più velocemente, ma con risposte più semplici.
  * Puoi ridurre la risoluzione della fotocamera (es., 640×480 invece di 1280×720) per velocizzare l'elaborazione delle immagini.
  * Chiudi altri programmi sul tuo Pi per liberare CPU e RAM.
