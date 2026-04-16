
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

6. Chatbot Vocale Locale
===========================

In questa lezione, combinerai tutto ciò che hai imparato — **riconoscimento vocale (STT)**,
**sintesi vocale (TTS)** e un **LLM locale (Ollama)** — per costruire un **chatbot vocale** completamente offline
che gira sul tuo Pironman 5 Pro MAX.

Il flusso di lavoro è semplice:

#. **Ascolta** — Il microfono cattura il tuo parlato e lo trascrive con **Vosk**.
#. **Pensa** — Il testo viene inviato a un **LLM** locale in esecuzione su Ollama (es., ``llama3.2:3b``).
#. **Parla** — Il chatbot risponde ad alta voce utilizzando **Piper TTS**.

Questo crea un **robot conversazionale a mani libere** in grado di comprendere e rispondere in tempo reale.

----

Prima di Iniziare
-----------------

Assicurati di aver preparato quanto segue:

* **Piper TTS** testato (:ref:`test_piper`) e scelto un modello vocale funzionante.
* **Vosk STT** testato (:ref:`test_vosk`) e scelto il pacchetto linguistico corretto (es., ``en-us``).
* **Ollama** installato (:ref:`download_ollama`) sul tuo Pi o su un altro computer, e scaricato un modello come ``llama3.2:3b`` (o uno più piccolo come ``moondream:1.8b`` se la memoria è limitata).

----

Eseguire il Codice
------------------

#. Apri lo script di esempio:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano local_voice_chatbot.py

#. Aggiorna i parametri come necessario:

   * ``stt = Vosk(language="en-us")``: Cambia questo per corrispondere al tuo accento/pacchetto linguistico (es., ``en-us``, ``zh-cn``, ``es``).
   * ``tts.set_model("en_US-amy-low")``: Sostituisci con il modello vocale Piper che hai verificato in :ref:`test_piper`.
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Aggiorna sia ``ip`` che ``model`` secondo la tua configurazione.

     * ``ip``: Se Ollama gira sullo **stesso Pi**, usa ``localhost``. Se Ollama gira su un altro computer nella tua LAN, abilita **Expose to network** in Ollama e imposta ``ip`` sull'indirizzo LAN di quel computer.
     * ``model``: Deve corrispondere esattamente al nome del modello che hai scaricato/attivato in Ollama.

#. Esegui lo script:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo python3 local_voice_chatbot.py

#. Dopo l'esecuzione, dovresti vedere:

   * Il bot ti saluta con un messaggio di benvenuto parlato.
   * Attende un input vocale.
   * Vosk trascrive il tuo parlato in testo.
   * Il testo viene inviato a Ollama, che restituisce in streaming una risposta.
   * La risposta viene pulita (rimuovendo il ragionamento nascosto) e pronunciata ad alta voce da Piper.
   * Ferma il programma in qualsiasi momento con ``Ctrl+C``.

----

Codice
------

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.llm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

   # Inizializza il riconoscimento vocale
   stt = Vosk(language="en-us")

   # Inizializza TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Istruzioni per l'LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Inizializza la connessione a Ollama
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utilità: pulisci il ragionamento nascosto
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
               print("\n🎤 Ascolto... (Premi Ctrl+C per fermare)")

               # Raccogli la trascrizione finale da Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[TU] {text}")
                   else:
                       print(f"[TU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Niente riconosciuto. Riprova.")
                   time.sleep(0.1)
                   continue

               # Interroga Ollama con streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Pulisci e parla
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Arresto in corso...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

Analisi del Codice
------------------

**Import e configurazione globale**

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.llm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

Importa i tre sottosistemi che hai costruito in precedenza:
**Vosk** per il riconoscimento vocale (STT), **Ollama** per l'LLM e **Piper** per la sintesi vocale (TTS).

**Inizializza STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Carica il modello Vosk per l'inglese americano.
Cambia il codice lingua (es., ``zh-cn``, ``es``) per corrispondere al tuo pacchetto vocale per una migliore precisione.

**Inizializza TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Crea un motore Piper e seleziona una voce specifica.
Scegli un modello che hai testato in :ref:`test_piper`. Le voci di qualità inferiore sono più veloci e usano meno CPU.

**Istruzioni LLM e messaggio di benvenuto**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Due scelte chiave di UX:

* Mantieni le **risposte brevi e dirette** (aiuta la chiarezza del TTS).
* Proibisci esplicitamente i tag di "catena di pensiero" nascosti per ridurre output rumorosi.

**Connetti a Ollama e imposta l'ambito della conversazione**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` assume che il server Ollama giri sullo stesso Pi. Se gira su un'altra macchina LAN, metti l'**IP LAN** di quel computer e abilita *Expose to network* in Ollama.
* ``set_max_messages(20)`` mantiene una breve cronologia conversazionale. Riduci questo valore se memoria/latenza sono limitate.

**Rimuovi ragionamento/tag nascosti prima di parlare**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Alcuni modelli possono emettere tag interni (es., ``<think>…``).
Questa funzione li rimuove in modo che il tuo TTS **pronunci solo** la risposta finale.

**Suggerimento:** Se vedi altri artefatti sullo schermo (perché trasmetti i token grezzi), questa funzione assicura già che l'output **parlato** rimanga pulito.

**Ciclo principale: saluta una volta, poi ascolta → pensa → parla**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Saluta l'utente tramite terminale e altoparlante. Accade una volta all'avvio.

**Ascolta (STT in streaming con parziali in tempo reale)**

.. code-block:: python

   print("\n🎤 Ascolto... (Premi Ctrl+C per fermare)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[TU] {text}")
       else:
           print(f"[TU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` produce trascrizioni **parziali** per un feedback immediato e una trascrizione **finale** quando l'enunciato termina.
* Il testo riconosciuto finale viene memorizzato in ``text`` e stampato una volta.

**Controllo:** Se non viene riconosciuto nulla, salti la chiamata all'LLM:

.. code-block:: python

   if not text:
       print("[INFO] Niente riconosciuto. Riprova.")
       time.sleep(0.1)
       continue

Questo evita di inviare prompt vuoti al modello (risparmia tempo e token).

**Pensa (LLM) con stampa in streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Invia la trascrizione finale all'LLM locale e **stampa i token mentre arrivano** per una bassa latenza.
* Nel frattempo, accumuli la risposta completa in ``reply_accum`` per l'elaborazione successiva.

**Nota:** Se preferisci **non mostrare** i token grezzi, imposta ``stream=False`` e stampa semplicemente la stringa finale.

**Parla (pulisci prima, poi TTS una volta)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Pulisce il testo finale per rimuovere i tag nascosti, poi **parla esattamente una volta**.
* Mantenere il TTS come un singolo passaggio evita ripetuti prompt come "[LLM] / [SAY]".

**Uscita e chiusura**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Arresto in corso...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Usa **Ctrl+C** per fermare. Il bot dice un breve addio per segnalare un'uscita pulita.

----

Risoluzione dei Problemi e FAQ
------------------------------

* **Il modello è troppo grande (errore di memoria)**

  Usa un modello più piccolo come ``moondream:1.8b`` o esegui Ollama su un computer più potente.

* **Nessuna risposta da Ollama**

  Assicurati che Ollama sia in esecuzione (``ollama serve`` o app desktop aperta). Se remoto, abilita **Expose to network** e controlla l'indirizzo IP.

* **Vosk non riconosce il parlato**

  Verifica che il microfono funzioni. Prova un altro pacchetto lingua (``zh-cn``, ``es`` ecc.) se necessario.

* **Piper silenzioso o errori**

  Conferma che il modello vocale scelto sia stato scaricato e testato in :ref:`test_piper`.

* **Risposte troppo lunghe o fuori tema**

  Modifica ``INSTRUCTIONS`` per aggiungere: **"Keep answers short and to the point."**
