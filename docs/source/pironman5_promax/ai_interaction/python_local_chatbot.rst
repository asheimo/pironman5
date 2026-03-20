.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

6. Lokaler Sprach-Chatbot
===========================

In dieser Lektion kombinieren Sie alles, was Sie gelernt haben — **Spracherkennung (STT)**,
**Text-to-Speech (TTS)** und ein **lokales LLM (Ollama)** — um einen vollständig offline arbeitenden **Sprach-Chatbot** zu bauen,
der auf Ihrem Pironman 5 Pro MAX läuft.

Der Arbeitsablauf ist einfach:

#. **Hören** — Das Mikrofon nimmt Ihre Sprache auf und transkribiert sie mit **Vosk**.
#. **Denken** — Der Text wird an ein lokales **LLM** gesendet, das auf Ollama läuft (z.B. ``llama3.2:3b``).
#. **Sprechen** — Der Chatbot antwortet mithilfe von **Piper TTS** laut.

Dies erschafft einen **freihändig bedienbaren Konversationsroboter**, der in Echtzeit verstehen und antworten kann.

----

Vorbereitung
----------------

Stellen Sie sicher, dass Sie Folgendes vorbereitet haben:

* **Piper TTS** getestet (:ref:`test_piper`) und ein funktionierendes Sprachmodell ausgewählt.
* **Vosk STT** getestet (:ref:`test_vosk`) und das richtige Sprachpaket ausgewählt (z.B. ``de``).
* **Ollama** installiert (:ref:`download_ollama`) auf Ihrem Pi oder einem anderen Computer und ein Modell wie ``llama3.2:3b`` heruntergeladen (oder ein kleineres wie ``moondream:1.8b``, wenn der Speicher begrenzt ist).

----

Code ausführen
--------------

#. Öffnen Sie das Beispielskript:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano local_voice_chatbot.py

#. Aktualisieren Sie die Parameter nach Bedarf:

   * ``stt = Vosk(language="de")``: Ändern Sie dies, um es an Ihren Akzent/Ihr Sprachpaket anzupassen (z.B. ``de``, ``en-us``, ``es``).
   * ``tts.set_model("de_DE-thorsten-low")``: Ersetzen Sie dies mit dem Piper-Sprachmodell, das Sie in :ref:`test_piper` überprüft haben.
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Aktualisieren Sie sowohl ``ip`` als auch ``model`` entsprechend Ihrem eigenen Setup.

     * ``ip``: Wenn Ollama auf dem **gleichen Pi** läuft, verwenden Sie ``localhost``. Wenn Ollama auf einem anderen Computer in Ihrem LAN läuft, aktivieren Sie **Für Netzwerk freigeben** in Ollama und setzen Sie ``ip`` auf die LAN-IP dieses Computers.
     * ``model``: Muss exakt mit dem Modellnamen übereinstimmen, den Sie in Ollama heruntergeladen/aktiviert haben.

#. Führen Sie das Skript aus:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo python3 local_voice_chatbot.py

#. Nach dem Start sollten Sie Folgendes sehen/hören:

   * Der Bot begrüßt Sie mit einer gesprochenen Willkommensnachricht.
   * Er wartet auf Spracheingabe.
   * Vosk transkribiert Ihre Sprache in Text.
   * Der Text wird an Ollama gesendet, das eine Antwort zurückgibt.
   * Die Antwort wird bereinigt (Entfernung versteckter Gedankengänge) und von Piper laut ausgesprochen.
   * Stoppen Sie das Programm jederzeit mit ``Strg+C``.

----

Code
----

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.lm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

   # Spracherkennung initialisieren
   stt = Vosk(language="de")

   # TTS initialisieren
   tts = Piper()
   tts.set_model("de_DE-thorsten-low")

   # Anweisungen für das LLM
   INSTRUCTIONS = (
       "Du bist ein hilfreicher Assistent. Antworte direkt auf Deutsch. "
       "Füge KEINE versteckten Gedanken, Analysen oder Tags wie <think> hinzu."
   )
   WELCOME = "Hallo! Ich bin dein Sprach-Chatbot. Sprich, wenn du bereit bist."

   # Ollama-Verbindung initialisieren
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Hilfsfunktion: Entferne versteckte Gedankengänge
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
               print("\n🎤 Höre zu... (Drücke Strg+C zum Beenden)")

               # Endgültiges Transkript von Vosk sammeln
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[DU] {text}")
                   else:
                       print(f"[DU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Nichts erkannt. Versuche es erneut.")
                   time.sleep(0.1)
                   continue

               # Ollama mit Streaming abfragen
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Bereinigen und sprechen
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Entschuldigung, das habe ich nicht verstanden.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Stoppe...")
       finally:
           tts.say("Auf Wiedersehen!")
           print("Tschüss.")

   if __name__ == "__main__":
       main()

----

Code-Analyse
------------

**Importe und globales Setup**

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.lm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

Bindet die drei Subsysteme ein, die Sie zuvor gebaut haben:
**Vosk** für Speech-to-Text (STT), **Ollama** für das LLM und **Piper** für Text-to-Speech (TTS).



**STT (Vosk) initialisieren**

.. code-block:: python

   stt = Vosk(language="de")

Lädt das Vosk-Modell für Deutsch.
Ändern Sie den Sprachcode (z.B. ``en-us``, ``es``), um es an Ihr Sprachpaket für bessere Genauigkeit anzupassen.



**TTS (Piper) initialisieren**

.. code-block:: python

   tts = Piper()
   tts.set_model("de_DE-thorsten-low")

Erstellt eine Piper-Engine und wählt eine bestimmte Stimme aus.
Wählen Sie ein Modell, das Sie in :ref:`test_piper` getestet haben. Stimmen mit geringerer Qualität sind schneller und verbrauchen weniger CPU.



**LLM-Anweisungen und Willkommenszeile**

.. code-block:: python

   INSTRUCTIONS = (
       "Du bist ein hilfreicher Assistent. Antworte direkt auf Deutsch. "
       "Füge KEINE versteckten Gedanken, Analysen oder Tags wie <think> hinzu."
   )
   WELCOME = "Hallo! Ich bin dein Sprach-Chatbot. Sprich, wenn du bereit bist."

Zwei wichtige UX-Entscheidungen:

* Halten Sie **Antworten kurz und direkt** (hilft bei der TTS-Klarheit).
* Verbieten Sie explizit versteckte "Chain-of-Thought"-Tags, um verrauschte Ausgaben zu reduzieren.



**Mit Ollama verbinden und Gesprächsumfang festlegen**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` nimmt an, dass der Ollama-Server auf demselben Pi läuft. Wenn er auf einem anderen LAN-Rechner läuft, geben Sie die **LAN-IP** dieses Computers ein und aktivieren Sie *Für Netzwerk freigeben* in Ollama.
* ``set_max_messages(20)`` behält einen kurzen Gesprächsverlauf. Verringern Sie dies, wenn Speicher/Latenz knapp sind.

**Versteckte Gedankengänge/Tags vor dem Sprechen entfernen**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Einige Modelle geben interne Tags aus (z.B. ``<think>…``).
Diese Funktion entfernt diese, so dass Ihre TTS **nur** die endgültige Antwort spricht.

**Tipp:** Wenn Sie andere Artefakte auf dem Bildschirm sehen (weil Sie rohe Token streamen), stellt diese Funktion bereits sicher, dass die **gesprochene** Ausgabe sauber bleibt.

**Hauptschleife: Einmal begrüßen, dann hören → denken → sprechen**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Begrüßt den Benutzer über Terminal und Lautsprecher. Geschieht einmal beim Start.

**Hören (Streaming-STT mit Live-Teilergebnissen)**

.. code-block:: python

   print("\n🎤 Höre zu... (Drücke Strg+C zum Beenden)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[DU] {text}")
       else:
           print(f"[DU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` liefert **partielle** Transkripte für sofortiges Feedback und ein **endgültiges** Transkript, wenn die Äußerung endet.
* Der endgültig erkannte Text wird in ``text`` gespeichert und einmal ausgegeben.

**Schutz:** Wenn nichts erkannt wurde, überspringen Sie den LLM-Aufruf:

.. code-block:: python

   if not text:
       print("[INFO] Nichts erkannt. Versuche es erneut.")
       time.sleep(0.1)
       continue

Dies vermeidet das Senden leerer Eingabeaufforderungen an das Modell (spart Zeit und Tokens).

**Denken (LLM) mit gestreamter Ausgabe**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Sendet das endgültige Transkript an das lokale LLM und **gibt Token aus, während sie eintreffen** für geringe Latenz.
* Gleichzeitig sammeln Sie die vollständige Antwort in ``reply_accum`` für die Nachbearbeitung.

**Hinweis:** Wenn Sie die rohen Token **nicht** anzeigen möchten, setzen Sie ``stream=False`` und geben Sie nur die endgültige Zeichenkette aus.

**Sprechen (zuerst bereinigen, dann einmal TTS)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Entschuldigung, das habe ich nicht verstanden.")

* Bereinigt den endgültigen Text, um versteckte Tags zu entfernen, und **spricht dann genau einmal**.
* Wenn TTS auf einen einzigen Durchlauf beschränkt bleibt, werden wiederholte Aufforderungen wie "[LLM] / [SAGEN]" vermieden.


**Beenden und Aufräumen**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stoppe...")
   finally:
       tts.say("Auf Wiedersehen!")
       print("Tschüss.")

Verwenden Sie **Strg+C** zum Stoppen. Der Bot sagt einen kurzen Abschiedsgruß, um ein sauberes Ende zu signalisieren.


----

Fehlerbehebung & FAQ
---------------------

* **Modell ist zu groß (Speicherfehler)**

  Verwenden Sie ein kleineres Modell wie ``moondream:1.8b`` oder führen Sie Ollama auf einem leistungsstärkeren Computer aus.

* **Keine Antwort von Ollama**

  Stellen Sie sicher, dass Ollama läuft (``ollama serve`` oder Desktop-App geöffnet). Bei Remote-Zugriff aktivieren Sie **Für Netzwerk freigeben** und überprüfen Sie die IP-Adresse.

* **Vosk erkennt Sprache nicht**

  Überprüfen Sie, ob Ihr Mikrofon funktioniert. Versuchen Sie bei Bedarf ein anderes Sprachpaket (``de``, ``en-us``, ``es`` etc.).

* **Piper ist stumm oder gibt Fehler aus**

  Bestätigen Sie, dass das ausgewählte Sprachmodell heruntergeladen und in :ref:`test_piper` getestet wurde.

* **Antworten zu lang oder themenfremd**

  Bearbeiten Sie ``INSTRUCTIONS``, um hinzuzufügen: **"Halte Antworten kurz und prägnant."**