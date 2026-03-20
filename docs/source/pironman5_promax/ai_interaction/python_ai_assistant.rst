.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _ai_voice_assistant_car:

7. KI-Sprachassistent
===========================

In dieser Lektion verwandeln Sie Ihren Pironman 5 Pro MAX in einen **sprachgesteuerten KI-Assistenten**.  
Mit dem bereitgestellten Code wird der Roboter: **auf ein Weckwort warten**, **Ihre Spracheingabe mit Vosk transkribieren**, sie an ein **OpenAI-LLM** senden und **mit Piper TTS** antworten.

----

Vorbereitung
----------------

Stellen Sie sicher, dass Sie Folgendes haben:

* :ref:`test_piper` — Die Piper-Stimme funktioniert (z. B. können Sie „Hallo“ abspielen).  
* :ref:`test_vosk` — Vosk STT funktioniert für Ihre Sprache (z. B. ``de``).  
* :ref:`py_online_llm` — Ihr **OpenAI-API-Schlüssel**, gespeichert in ``secret.py`` als ``OPENAI_API_KEY``.  
* Ein funktionierendes **Mikrofon** und **Lautsprecher** am Pironman 5 Pro MAX.  
* Eine stabile Netzwerkverbindung (das LLM ist online).

----

Beispiel ausführen
--------------------------------------------

.. code-block:: bash

   cd ~/sunfounder-voice-assistant/examples/
   sudo python3 voice_assistant.py

**Vom Code verwendete Konfiguration:**

* LLM: **OpenAI** (``gpt-4o-mini``)  
* TTS: **Piper** (``de_DE-thorsten-low``)  
* STT: **Vosk** (``de``)  
* Weckwort: ``"hallo buddy"``  
* Tastatureingabe: **aktiviert** (optionale manuelle Eingabe)  
* Bildmodus: **aktiviert** (``WITH_IMAGE=True``) — erfordert ein multimodales LLM, falls Sie später Bilder verwenden möchten

**Was passiert:**

1. Der Assistent zeigt eine Willkommensnachricht mit dem Wecksatz an.  
2. Er horcht auf **„hallo buddy“**.  
3. Nach dem Aufwachen wird Ihre Spracheingabe transkribiert (Vosk → Text).  
4. Der Text wird zur Antwortgenerierung an **OpenAI (gpt-4o-mini)** gesendet.  
5. Die Antwort wird mit **Piper** (``de_DE-thorsten-low``) ausgegeben.

**Beispielinteraktion**

.. code-block:: text

   Sie: Hallo Buddy
   Roboter: Hallo!

   Sie: Was ist die Hauptstadt von Italien?
   Roboter: Die Hauptstadt von Italien ist Rom.

Code
-----------------

.. code-block:: python

  from sunfounder_voice_assistant.voice_assistant import VoiceAssistant
  from sunfounder_voice_assistant.lm import OpenAI as LLM
  from secret import OPENAI_API_KEY as API_KEY

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Name des Roboters
  NAME = "Buddy"

  # Bildmodus aktivieren, erfordert die Einrichtung eines multimodalen Sprachmodells
  WITH_IMAGE = True

  # Modelle und Sprachen einstellen
  LLM_MODEL = "gpt-4o-mini"
  TTS_MODEL = "de_DE-thorsten-low"
  STT_LANGUAGE = "de"

  # Tastatureingabe aktivieren
  KEYBOARD_ENABLE = True

  # Weckwort aktivieren
  WAKE_ENABLE = True
  WAKE_WORD = [f"hallo {NAME.lower()}"]
  # Antwort auf Weckwort festlegen, leer lassen um zu deaktivieren
  ANSWER_ON_WAKE = "Hallo"

  # Willkommensnachricht
  WELCOME = f"Hallo, ich bin {NAME}. Wecke mich mit: " + ", ".join(WAKE_WORD)

  # Anweisungen festlegen
  INSTRUCTIONS = f"""
  Du bist ein hilfreicher Assistent namens {NAME}.
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

**Code-Erklärung:**

* ``OpenAI(..., model="gpt-4o-mini")`` — Verwendet **OpenAI** als einziges LLM in dieser Lektion.  
* ``NAME`` / ``WAKE_WORD`` — Personalisieren Sie den Assistenten („Buddy“, „hallo buddy“).  
* ``WITH_IMAGE=True`` — Aktiviert den Bildmodus im Assistenten (enthält hier keine Bild-E/A-Logik).  
* ``TTS_MODEL="de_DE-thorsten-low"`` — Piper-Stimme für Antworten.  
* ``STT_LANGUAGE="de"`` — Vosk-Sprache für die Erkennung.  
* ``KEYBOARD_ENABLE=True`` — Ermöglicht während der Fehlersuche optionale manuelle Texteingabe.  
* ``WELCOME`` / ``INSTRUCTIONS`` — Startnachricht und System-Prompt für die Assistenten-Persönlichkeit.  
* ``va.run()`` — Startet die Schleife: **Aufwachen → Zuhören → LLM → Sprechen**.


Wechsel zu anderen LLMs oder TTS
------------------------------------------------

Sie können mit nur wenigen Änderungen problemlos zu anderen LLMs, TTS oder STT-Sprachen wechseln:

* Unterstützte LLMs:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Überprüfen Sie die unterstützten Sprachen von **Piper TTS**.  
* :ref:`test_vosk` — Überprüfen Sie die unterstützten Sprachen von **Vosk STT**.  

Zum Wechseln ändern Sie einfach den Initialisierungsteil im Code:

.. code-block:: python

   from sunfounder_voice_assistant.lm import Gemini as LLM
   llm = LLM(api_key="IHR_SCHLÜSSEL", model="gemini-pro")

   # Modelle und Sprachen einstellen
   TTS_MODEL = "de_DE-thorsten-low"
   STT_LANGUAGE = "de"



----

Fehlerbehebung
-----------------------------

* **Roboter reagiert nicht auf Weckwort**

  - Überprüfen Sie, ob das Mikrofon funktioniert.  
  - Stellen Sie sicher, dass ``WAKE_ENABLE = True`` ist.  
  - Passen Sie das Weckwort an Ihre Aussprache an.  
  - Reduzieren Sie Hintergrundgeräusche und sprechen Sie deutlich.

* **Kein Ton vom Lautsprecher**

  - Überprüfen Sie den Namen des TTS-Modells (z. B. ``de_DE-thorsten-low``).  
  - Testen Sie Piper oder Espeak manuell.  
  - Überprüfen Sie Lautsprecheranschluss und Lautstärke.

* **API-Schlüssel-Fehler oder Zeitüberschreitung**

  - Überprüfen Sie Ihren Schlüssel in ``secret.py``.  
  - Stellen Sie sicher, dass Ihre Netzwerkverbindung stabil ist.  
  - Bestätigen Sie, dass das LLM-Modell unterstützt wird (z. B. ``gpt-4o-mini``).

* **Weckwort funktioniert, aber keine Antwort**

  - Überprüfen Sie, ob die STT-Sprache zu Ihrem Akzent passt.  
  - Stellen Sie sicher, dass das Modell korrekt heruntergeladen wurde.  
  - Versuchen Sie, Debug-Protokolle auszugeben, um zu bestätigen, dass STT läuft.

* **TTS funktioniert, aber keine LLM-Antwort**

  - Überprüfen Sie, ob der API-Schlüssel gültig ist.  
  - Überprüfen Sie Modellname und LLM-Einstellungen.  
  - Stellen Sie die Internetverbindung sicher.