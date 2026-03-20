.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

2. TTS mit Piper und OpenAI
========================================================

In der vorherigen Lektion haben wir **Espeak** und **Pico2Wave** erkundet, zwei einfache Offline-TTS-Engines auf dem Raspberry Pi.
Jetzt machen wir einen großen Schritt nach vorne und probieren zwei **fortschrittlichere TTS-Optionen** aus, die eine **höhere Sprachqualität** und mehr Flexibilität bieten:

* **Piper** — eine schnelle, auf neuronalen Netzen basierende TTS-Engine, die **vollständig offline** auf dem Raspberry Pi läuft.
* **OpenAI TTS** — ein Online-Dienst, der **sehr natürliche und menschenähnliche Stimmen** bietet, perfekt für ausdrucksstarke Sprache.

Diese Engines lassen Ihren Pironman 5 Pro MAX realistischer und lebensechter klingen. 🚀

----

.. _test_piper:

1. Piper testen
------------------

Piper ist eine **Offline-Neuronale-TTS-Engine**, d.h. Sie benötigen keine Internetverbindung, sobald das Modell installiert ist.
Es unterstützt mehrere **Sprachen** und **Stimmen** und ist damit eine leistungsstarke Option für eingebettete Sprachausgabe.

**Führen Sie das Programm aus**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_piper.py

* Beim ersten Ausführen wird das ausgewählte **Sprachmodell** automatisch heruntergeladen.
* Sie sollten dann hören, wie der Pironman 5 Pro MAX sagt: ``Hallo! Ich bin Piper TTS.``
* Sie können die Stimme oder Sprache wechseln, indem Sie ``set_model()`` mit einem anderen Modellnamen aufrufen.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Piper

  tts = Piper()

  # Unterstützte Sprachen auflisten
  print(tts.available_countrys())

  # Modelle für Deutsch (de_DE) auflisten
  print(tts.available_models('de_DE'))

  # Ein Sprachmodell festlegen (automatischer Download, falls nicht vorhanden)
  tts.set_model("de_DE-thorsten-low")

  # Etwas sagen
  tts.say("Hallo! Ich bin Piper TTS.")

**Code-Erklärung:**

* ``available_countrys()`` — Listet alle unterstützten Sprachen auf.
* ``available_models()`` — Listet verfügbare Modelle für eine bestimmte Sprache auf.
* ``set_model()`` — Legt das Sprachmodell fest. Wenn das Modell nicht installiert ist, wird es automatisch heruntergeladen.
* ``say()`` — Wandelt Text in Sprache um und gibt ihn sofort aus.

💡 **Tipp:** Probieren Sie verschiedene Modelle aus, um Geschwindigkeit, Klarheit und Akzente zu vergleichen. Einige Modelle sind leichter (schneller), während andere eine höhere Klangtreue haben.

----

2. OpenAI TTS testen
-------------------------------

**API-Schlüssel abrufen und speichern**

#. Gehen Sie zu |link_openai_platform| und melden Sie sich an. Klicken Sie auf der Seite **API keys** auf **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Füllen Sie die Details aus (Owner, Name, Project und Berechtigungen falls erforderlich), dann klicken Sie auf **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Sobald der Schlüssel erstellt wurde, kopieren Sie ihn sofort — Sie werden ihn nicht wieder sehen können. Wenn Sie ihn verlieren, müssen Sie einen neuen generieren.

   .. image:: img/llm_openai_copy.png

#. Erstellen Sie in Ihrem Projektordner (z.B.: ``/``) eine Datei namens ``secret.py``:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie Ihren Schlüssel wie folgt in die Datei ein:

   .. code-block:: python

       # secret.py
       # Speichern Sie hier Geheimnisse. Committen Sie diese Datei niemals in Git.
       OPENAI_API_KEY = "sk-xxx"

**Führen Sie das Programm aus**

.. code-block:: bash

  cd ~/sunfounder-voice-assistant/examples
  sudo python3 tts_openai.py

* Das Programm verbindet sich mit dem OpenAI-TTS-Dienst, und der Pironman 5 Pro MAX spricht mit **natürlicher, ausdrucksstarker Sprachausgabe**.
* Sie können **Sprachstile** ändern und **Anweisungen** hinzufügen, um Tonfall und Ausdruck zu steuern (z.B. traurig, dramatisch, verspielt).
* Dies macht OpenAI TTS ideal für interaktive Roboter, Geschichtenerzählen oder Lernassistenten.


**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import OpenAI_TTS
  from secret import OPENAI_API_KEY

  # Exportieren Sie Ihren OPENAI_API_KEY, bevor Sie das Skript ausführen
  # export OPENAI_API_KEY="sk-proj-xxxxxx"

  tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
  # tts.set_model('tts-1')
  tts.set_voice('alloy')
  tts.set_model('gpt-4o-mini-tts')

  msg = "Hallo! Ich bin OpenAI TTS."
  print(f"Sage: {msg}")
  tts.say(msg)

  msg = "mit Anweisungen kann ich Wörter traurig sagen"
  instructions = "sage es traurig"
  print(f"Sage: {msg}, mit Anweisung: '{instructions}'")
  tts.say(msg, instructions=instructions)

  msg = "oder etwas dramatisch sagen."
  instructions = "sage es dramatisch"
  print(f"Sage: {msg}, mit Anweisung: '{instructions}'")
  tts.say(msg, instructions=instructions)


**Code-Erklärung:**

* ``OpenAI_TTS()`` — Initialisiert die OpenAI-TTS-Engine mit Ihrem API-Schlüssel.
* ``set_model()`` — Wählt das TTS-Modell aus (z.B. ``gpt-4o-mini-tts``).
* ``set_voice()`` — Wählt eine bestimmte Stimme aus (z.B. ``alloy``).
* ``say(text)`` — Wandelt den Text in Sprache um und gibt ihn aus.
* ``say(text, instructions=...)`` — Fügt **Anweisungen für den Ausdruck** hinzu, sodass Sie den Sprachstil dynamisch steuern können.

**Beispiel:**

- "sage es traurig" → sanfter, emotionaler Tonfall
- "sage es dramatisch" → kühne und ausdrucksstarke Darbietung
- "sage es aufgeregt" → enthusiastischer Tonfall

----

Fehlerbehebung
-------------------

* **Kein Modul namens 'secret'**

  Das bedeutet, dass sich ``secret.py`` nicht im selben Ordner wie Ihre Python-Datei befindet.
  Verschieben Sie ``secret.py`` in das gleiche Verzeichnis, in dem Sie das Skript ausführen, z.B.:

  .. code-block:: bash

     ls ~/
     # Stellen Sie sicher, dass Sie beide sehen: secret.py und Ihre .py-Datei

* **OpenAI: Ungültiger API-Schlüssel / 401**

  * Überprüfen Sie, ob Sie den vollständigen Schlüssel eingefügt haben (beginnt mit ``sk-``) und keine zusätzlichen Leerzeichen/Zeilenumbrüche vorhanden sind.
  * Stellen Sie sicher, dass Ihr Code ihn korrekt importiert:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Überprüfen Sie den Netzwerkzugriff auf Ihrem Pi (versuchen Sie ``ping api.openai.com``).

* **OpenAI: Kontingent überschritten / Abrechnungsfehler**

  * Möglicherweise müssen Sie im OpenAI-Dashboard eine Zahlungsmethode hinzufügen oder Ihr Kontingent erhöhen.
  * Versuchen Sie es erneut, nachdem Sie das Konto-/Abrechnungsproblem behoben haben.

* **Piper: tts.say() läuft, aber kein Ton**

  * Stellen Sie sicher, dass ein Sprachmodell tatsächlich vorhanden ist:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Bestätigen Sie, dass Ihr Modellname im Code genau übereinstimmt:

    .. code-block:: python

       tts.set_model("de_DE-thorsten-low")

  * Überprüfen Sie das Audioausgabegerät/die Lautstärke auf Ihrem Pi (``alsamixer``) und dass Lautsprecher angeschlossen und eingeschaltet sind.

* **ALSA / Soundgerät-Fehler (z.B. "Audio device busy" oder "No such file or directory")**

  * Schließen Sie andere Programme, die Audio verwenden.
  * Starten Sie den Pi neu, wenn das Gerät belegt bleibt.
  * Wählen Sie für HDMI- vs. Kopfhöreranschluss das richtige Gerät in den Audioeinstellungen des Raspberry Pi OS.

* **Zugriffsverweigerung bei der Ausführung von Python**

  * Versuchen Sie es mit ``sudo``, wenn Ihre Umgebung dies erfordert:

    .. code-block:: bash

       sudo python3 tts_piper.py

Vergleich der TTS-Engines
-------------------------

.. list-table:: Funktionsvergleich: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Eigenschaft
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Läuft auf
     - Integriert auf Raspberry Pi (offline)
     - Integriert auf Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, benötigt Modell)
     - Cloud (online, benötigt API-Schlüssel)
   * - Stimmqualität
     - Roboterhaft
     - Natürlicher als Espeak
     - Natürlich (neuronale TTS)
     - Sehr natürlich / menschenähnlich
   * - Steuerung
     - Geschwindigkeit, Tonhöhe, Lautstärke
     - Eingeschränkte Steuerung
     - Verschiedene Stimmen/Modelle wählbar
     - Modell und Stimmen wählbar
   * - Sprachen
     - Viele (Qualität variiert)
     - Begrenzte Auswahl
     - Viele Stimmen/Sprachen verfügbar
     - Am besten in Englisch (andere variieren je nach Verfügbarkeit)
   * - Latenz / Geschwindigkeit
     - Sehr schnell
     - Schnell
     - Echtzeit auf Pi 4/5 mit "low"-Modellen
     - Netzwerkabhängig (normalerweise geringe Latenz)
   * - Einrichtung
     - Minimal
     - Minimal
     - ``.onnx`` + ``.onnx.json`` Modelle herunterladen
     - API-Schlüssel erstellen, Client installieren
   * - Am besten geeignet für
     - Schnelltests, einfache Aufforderungen
     - Etwas bessere Offline-Stimme
     - Lokale Projekte mit besserer Qualität
     - Höchste Qualität, reichhaltige Stimmoptionen