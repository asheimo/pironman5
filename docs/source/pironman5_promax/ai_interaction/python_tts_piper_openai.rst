
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

2. TTS con Piper e OpenAI
========================================================

Nella lezione precedente, abbiamo esplorato **Espeak** e **Pico2Wave**, due semplici motori TTS offline su Raspberry Pi.
Ora facciamo un grande passo avanti e proviamo due **opzioni TTS più avanzate** che offrono **maggiore qualità vocale** e più flessibilità:

* **Piper** — un motore TTS veloce basato su reti neurali che funziona **completamente offline** su Raspberry Pi.
* **OpenAI TTS** — un servizio online che fornisce voci **molto naturali e simili a quelle umane**, perfetto per un parlato espressivo.

Questi motori faranno sì che il tuo Pironman 5 Pro MAX suoni più realistico e vivo. 🚀

----

.. _test_piper:

1. Testare Piper
------------------

Piper è un **motore TTS neurale offline**, il che significa che non hai bisogno di una connessione Internet una volta installato il modello.
Supporta molteplici **lingue** e **voci**, rendendolo un'opzione potente per la sintesi vocale su sistemi embedded.

**Eseguire il programma**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_piper.py

* La prima volta che lo esegui, il **modello vocale** selezionato verrà scaricato automaticamente.
* Dovresti quindi sentire il Pironman 5 Pro MAX dire: ``Hello! I'm Piper TTS.``
* Puoi cambiare voce o lingua chiamando ``set_model()`` con un nome di modello diverso.

**Codice**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Piper

  tts = Piper()

  # Elenca le lingue supportate
  print(tts.available_countrys())

  # Elenca i modelli per l'inglese (en_us)
  print(tts.available_models('en_us'))

  # Imposta un modello vocale (download automatico se non già presente)
  tts.set_model("en_US-amy-low")

  # Pronuncia qualcosa
  tts.say("Hello! I'm Piper TTS.")

**Spiegazione del codice:**

* ``available_countrys()`` — Elenca tutte le lingue supportate.
* ``available_models()`` — Elenca i modelli disponibili per una lingua specifica.
* ``set_model()`` — Imposta il modello vocale. Se il modello non è installato, verrà scaricato automaticamente.
* ``say()`` — Converte il testo in parlato e lo riproduce immediatamente.

💡 **Suggerimento:** Prova diversi modelli per confrontare velocità, chiarezza e accenti. Alcuni modelli sono più leggeri (più veloci), mentre altri hanno una fedeltà maggiore.

----

2. Testare OpenAI TTS
-------------------------------

**Ottieni e salva la tua chiave API**

#. Vai su |link_openai_platform| e accedi. Nella pagina **API keys**, clicca su **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Compila i dettagli (Owner, Name, Project, e permessi se necessari), poi clicca su **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una volta creata la chiave, copiala immediatamente — non potrai più vederla. Se la perdi, devi generarne una nuova.

   .. image:: img/llm_openai_copy.png

#. Nella tua cartella di progetto (ad esempio: ``/``), crea un file chiamato ``secret.py``:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Incolla la tua chiave nel file in questo modo:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Eseguire il programma**

.. code-block:: bash

  cd ~/sunfounder-voice-assistant/examples
  sudo python3 tts_openai.py

* Il programma si connetterà al servizio TTS di OpenAI, e il Pironman 5 Pro MAX parlerà utilizzando un'**uscita vocale naturale ed espressiva**.
* Puoi cambiare **stile di voce** e aggiungere **istruzioni** per controllare il tono e l'espressione (es., triste, drammatico, giocoso).
* Questo rende OpenAI TTS ideale per robot interattivi, narrazione o assistenti educativi.

**Codice**

.. code-block:: python

  from sunfounder_voice_assistant.tts import OpenAI_TTS
  from secret import OPENAI_API_KEY

  # Esporta la tua OPENAI_API_KEY prima di eseguire lo script
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

**Spiegazione del codice:**

* ``OpenAI_TTS()`` — Inizializza il motore TTS di OpenAI utilizzando la tua chiave API.
* ``set_model()`` — Seleziona il modello TTS (es., ``gpt-4o-mini-tts``).
* ``set_voice()`` — Sceglie una voce specifica (es., ``alloy``).
* ``say(text)`` — Converte il testo in parlato e lo riproduce.
* ``say(text, instructions=...)`` — Aggiunge **istruzioni di tono espressive**, permettendoti di controllare dinamicamente lo stile del parlato.

**Esempio:**

- “say it sadly” → tono morbido ed emotivo
- “say it dramatically” → pronuncia audace ed espressiva
- “say it excitedly” → tono entusiasta

----

Risoluzione dei Problemi
------------------------

* **Nessun modulo chiamato 'secret'**

  Ciò significa che ``secret.py`` non si trova nella stessa cartella del tuo file Python.
  Sposta ``secret.py`` nella stessa directory in cui esegui lo script, ad esempio:

  .. code-block:: bash

     ls ~/
     # Assicurati di vedere entrambi: secret.py e il tuo file .py

* **OpenAI: Chiave API non valida / 401**

  * Controlla di aver incollato la chiave completa (inizia con ``sk-``) e che non ci siano spazi o nuove righe extra.
  * Assicurati che il tuo codice la importi correttamente:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Conferma l'accesso alla rete sul tuo Pi (prova ``ping api.openai.com``).

* **OpenAI: Quota superata / errore di fatturazione**

  * Potrebbe essere necessario aggiungere un metodo di pagamento o aumentare la quota nel dashboard OpenAI.
  * Riprova dopo aver risolto il problema dell'account/fatturazione.

* **Piper: tts.say() viene eseguito ma nessun suono**

  * Assicurati che un modello vocale sia effettivamente presente:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Conferma che il nome del modello corrisponda esattamente nel codice:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Controlla il dispositivo di uscita audio/volume sul tuo Pi (``alsamixer``), e che gli altoparlanti siano collegati e accesi.

* **Errori ALSA / dispositivo audio (es., "Audio device busy" o "No such file or directory")**

  * Chiudi altri programmi che utilizzano l'audio.
  * Riavvia il Pi se il dispositivo rimane occupato.
  * Per l'uscita HDMI vs. jack per cuffie, seleziona il dispositivo corretto nelle impostazioni audio di Raspberry Pi OS.

* **Permesso negato durante l'esecuzione di Python**

  * Prova con ``sudo`` se il tuo ambiente lo richiede:

    .. code-block:: bash

       sudo python3 tts_piper.py

Confronto dei Motori TTS
-------------------------

.. list-table:: Confronto delle funzionalità: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Caratteristica
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Esecuzione su
     - Integrato su Raspberry Pi (offline)
     - Integrato su Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, necessita modello)
     - Cloud (online, necessita chiave API)
   * - Qualità della voce
     - Robotica
     - Più naturale di Espeak
     - Naturale (TTS neurale)
     - Molto naturale / simile a quella umana
   * - Controlli
     - Velocità, tono, volume
     - Controlli limitati
     - Scegli diverse voci/modelli
     - Scegli modello e voci
   * - Lingue
     - Molte (qualità variabile)
     - Insieme limitato
     - Molte voci/lingue disponibili
     - Migliore in inglese (le altre variano per disponibilità)
   * - Latenza / velocità
     - Molto veloce
     - Veloce
     - Tempo reale su Pi 4/5 con modelli "leggeri"
     - Dipendente dalla rete (di solito bassa latenza)
   * - Configurazione
     - Minima
     - Minima
     - Scarica modelli ``.onnx`` + ``.onnx.json``
     - Crea chiave API, installa client
   * - Ideale per
     - Test rapidi, prompt semplici
     - Voce offline leggermente migliore
     - Progetti locali con qualità superiore
     - Qualità massima, ricche opzioni vocali
