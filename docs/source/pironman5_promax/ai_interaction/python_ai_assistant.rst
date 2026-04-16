
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _ai_voice_assistant_car:

7. Assistente Vocale AI
===========================

Questa lezione trasforma il tuo Pironman 5 Pro MAX in un **assistente AI incentrato sulla voce**.
Con il codice fornito, il robot: **attende una parola di attivazione**, **trascrive il tuo parlato** con Vosk, lo invia a un **LLM di OpenAI**, e **risponde vocalmente** utilizzando Piper TTS.

----

Prima di Iniziare
-----------------

Assicurati di avere:

* :ref:`test_piper` — La voce di Piper funziona (ad esempio, puoi riprodurre “Hello”).
* :ref:`test_vosk` — Vosk STT funziona per la tua lingua (es. ``en-us``).
* :ref:`py_online_llm` — La tua **chiave API OpenAI** salvata in ``secret.py`` come ``OPENAI_API_KEY``.
* Un **microfono** e un **altoparlante** funzionanti su Pironman 5 Pro MAX.
* Una connessione di rete stabile (LLM è online).

----

Eseguire l'Esempio
------------------

.. code-block:: bash

   cd ~/sunfounder-voice-assistant/examples/
   sudo python3 voice_assistant.py

**Configurazione utilizzata dal codice:**

* LLM: **OpenAI** (``gpt-4o-mini``)
* TTS: **Piper** (``en_US-ryan-low``)
* STT: **Vosk** (``en-us``)
* Parola di attivazione: ``"hey buddy"``
* Ingresso da tastiera: **abilitato** (inserimento manuale opzionale)
* Modalità immagine: **abilitata** (``WITH_IMAGE=True``) — richiede un LLM multimodale se decidi di usare immagini in seguito

**Cosa succede:**

1. L'assistente mostra un messaggio di benvenuto con la frase di attivazione.
2. Ascolta **“hey buddy”**.
3. Dopo l'attivazione, il tuo parlato viene trascritto (Vosk → testo).
4. Il testo viene inviato a **OpenAI (gpt-4o-mini)** per una risposta.
5. La risposta viene pronunciata con **Piper** (``en_US-ryan-low``).

**Esempio di interazione**

.. code-block:: text

   Tu: Hey Buddy
   Robot: Ciao!

   Tu: Qual è la capitale dell'Italia?
   Robot: La capitale dell'Italia è Roma.

Codice
-----------------

.. code-block:: python

  from sunfounder_voice_assistant.voice_assistant import VoiceAssistant
  from sunfounder_voice_assistant.llm import OpenAI as LLM
  from secret import OPENAI_API_KEY as API_KEY

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Nome del robot
  NAME = "Buddy"

  # Abilita immagine, necessita di un modello linguistico multimodale
  WITH_IMAGE = True

  # Imposta modelli e lingue
  LLM_MODEL = "gpt-4o-mini"
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

  # Abilita ingresso da tastiera
  KEYBOARD_ENABLE = True

  # Abilita parola di attivazione
  WAKE_ENABLE = True
  WAKE_WORD = [f"hey {NAME.lower()}"]
  # Imposta risposta alla parola di attivazione, lasciare vuoto per disabilitare
  ANSWER_ON_WAKE = "Ciao"

  # Messaggio di benvenuto
  WELCOME = f"Ciao, sono {NAME}. Svegliami con: " + ", ".join(WAKE_WORD)

  # Imposta istruzioni
  INSTRUCTIONS = f"""
  Sei un assistente utile, di nome {NAME}.
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

**Spiegazione del codice:**

* ``OpenAI(..., model="gpt-4o-mini")`` — Utilizza **OpenAI** come unico LLM in questa lezione.
* ``NAME`` / ``WAKE_WORD`` — Personalizza l'assistente (“Buddy”, “hey buddy”).
* ``WITH_IMAGE=True`` — Abilita la modalità immagine nell'assistente (nessuna logica di I/O immagine inclusa qui).
* ``TTS_MODEL="en_US-ryan-low"`` — Voce Piper utilizzata per le risposte.
* ``STT_LANGUAGE="en-us"`` — Lingua Vosk per il riconoscimento.
* ``KEYBOARD_ENABLE=True`` — Consente l'inserimento manuale opzionale di testo durante il debug.
* ``WELCOME`` / ``INSTRUCTIONS`` — Messaggio di avvio e personalità dell'assistente / prompt di sistema.
* ``va.run()`` — Avvia il ciclo: **attivazione → ascolto → LLM → risposta vocale**.

Passare ad Altri LLM o TTS
---------------------------

Puoi facilmente passare ad altri LLM, TTS o lingue STT con poche modifiche:

* LLM supportati:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Verifica le lingue supportate da **Piper TTS**.
* :ref:`test_vosk` — Verifica le lingue supportate da **Vosk STT**.

Per passare ad un altro, modifica semplicemente la parte di inizializzazione nel codice:

.. code-block:: python

   from sunfounder_voice_assistant.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Imposta modelli e lingue
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

----

Risoluzione dei Problemi
-----------------------------

* **Il robot non risponde alla parola di attivazione**

  - Verifica che il microfono funzioni.
  - Assicurati che ``WAKE_ENABLE = True``.
  - Regola la parola di attivazione in base alla tua pronuncia.
  - Riduci il rumore di fondo e parla chiaramente.

* **Nessun suono dall'altoparlante**

  - Verifica il nome del modello TTS (es. ``en_US-ryan-low``).
  - Testa manualmente Piper o Espeak.
  - Controlla la connessione dell'altoparlante e il volume.

* **Errore della chiave API o timeout**

  - Controlla la tua chiave in ``secret.py``.
  - Assicurati che la tua connessione di rete sia stabile.
  - Conferma che il modello LLM sia supportato (es. ``gpt-4o-mini``).

* **La parola di attivazione funziona ma nessuna risposta**

  - Verifica che la lingua STT corrisponda al tuo accento.
  - Assicurati che il modello sia stato scaricato correttamente.
  - Prova a stampare i log di debug per confermare che STT sia in esecuzione.

* **TTS funziona ma nessuna risposta dall'LLM**

  - Verifica che la chiave API sia valida.
  - Controlla il nome del modello e le impostazioni LLM.
  - Assicurati di avere connettività Internet.
