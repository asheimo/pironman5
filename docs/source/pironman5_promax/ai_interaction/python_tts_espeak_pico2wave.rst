.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

1. TTS mit Espeak und Pico2Wave
=================================================

In dieser Lektion verwenden wir zwei integrierte Text-to-Speech (TTS)-Engines auf dem Raspberry Pi — **Espeak** und **Pico2Wave** — um den Pironman 5 Pro MAX zum Sprechen zu bringen.

Diese beiden Engines sind einfach und laufen offline, aber sie klingen recht unterschiedlich:

* **Espeak**: sehr leichtgewichtig und schnell, aber die Stimme ist roboterhaft. Sie können Geschwindigkeit, Tonhöhe und Lautstärke anpassen.
* **Pico2Wave**: erzeugt eine glattere und natürlichere Stimme als Espeak, bietet aber weniger Konfigurationsmöglichkeiten.

Sie werden den Unterschied in **Stimmqualität** und **Funktionen** hören.

----

1. Espeak testen
--------------------

Espeak ist eine leichtgewichtige TTS-Engine, die im Raspberry Pi OS enthalten ist.
Ihre Stimme klingt roboterhaft, ist aber hochgradig konfigurierbar: Sie können Lautstärke, Tonhöhe, Geschwindigkeit und mehr anpassen.

**Führen Sie das Programm aus**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_espeak.py

  * Sie sollten hören, wie der Pironman 5 Pro MAX sagt: "Hallo! Ich bin Espeak TTS."
  * Versuchen Sie, die Abstimmungsparameter im Code zu ändern, um zu experimentieren, wie sich ``amp``, ``speed``, ``gap`` und ``pitch`` auf den Klang auswirken.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Espeak

  # Espeak TTS-Instanz erstellen
  tts = Espeak()
  # Amplitude einstellen 0-200, Standard 100
  tts.set_amp(200)
  # Geschwindigkeit einstellen 80-260, Standard 150
  tts.set_speed(150)
  # Wortabstand einstellen 0-200, Standard 1
  tts.set_gap(1)
  # Tonhöhe einstellen 0-99, Standard 80
  tts.set_pitch(80)

  tts.say("Hallo! Ich bin Espeak TTS.")

**Code-Erklärung:**

* ``tts.set_amp()`` — Steuert die Lautstärke (0–200).
* ``tts.set_speed()`` — Passt die Sprechgeschwindigkeit an (80–260).
* ``tts.set_gap()`` — Legt den Wortabstand fest (0–200).
* ``tts.set_pitch()`` — Legt die Tonhöhe fest (0–99).
* ``tts.say()`` — Wandelt Text in Sprache um und gibt ihn aus.

💡 **Tipp:** Versuchen Sie, Tonhöhe und Geschwindigkeit zu erhöhen, damit der Roboter fröhlich klingt, oder sie zu senken, um ihn ernst klingen zu lassen.

----


2. Pico2Wave testen
---------------------

Pico2Wave erzeugt im Vergleich zu Espeak eine **natürlichere und menschlichere Stimme**.
Es ist sehr einfach zu bedienen, aber weniger flexibel — Sie können nur die **Sprache ändern**, nicht die Tonhöhe, Geschwindigkeit oder Lautstärke.
Das macht Pico2Wave zu einer guten Wahl, wenn Sie eine klare und fließende Sprache ohne viel Konfiguration wünschen.

**Führen Sie das Programm aus**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_pico2wave.py

* Sie sollten hören, wie der Pironman 5 Pro MAX sagt: "Hallo! Ich bin Pico2Wave TTS."
* Versuchen Sie, die Sprache zu ändern (z.B. ``es-ES`` für Spanisch) und hören Sie, wie sich die Stimme verändert.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Pico2Wave

  # Pico2Wave TTS-Instanz erstellen
  tts = Pico2Wave()

  # Sprache einstellen
  tts.set_lang('de-DE')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  # Kurzer Test
  tts.say("Hallo! Ich bin Pico2Wave TTS.")

**Code-Erklärung:**

* ``tts.set_lang()`` — Legt die Ausgabesprache für die Sprachsynthese fest.

  - ``en-US`` (Standard)
  - ``en-GB``
  - ``de-DE``
  - ``es-ES``
  - ``fr-FR``
  - ``it-IT``

* ``tts.say()`` — Wandelt den Text in Sprache um und gibt ihn sofort aus.


----

Fehlerbehebung
-------------------

* **Kein Ton bei der Ausführung von Espeak oder Pico2Wave**

  * Überprüfen Sie, ob Ihre Lautsprecher/Kopfhörer angeschlossen sind und die Lautstärke nicht stummgeschaltet ist.
  * Führen Sie einen schnellen Test im Terminal durch:

    .. code-block:: bash

       espeak "Hallo Welt"
       pico2wave -w test.wav "Hallo Welt" && aplay test.wav

  Wenn Sie nichts hören, liegt das Problem bei der Audioausgabe, nicht bei Ihrem Python-Code.

* **Espeak-Stimme klingt zu schnell oder zu roboterhaft**

  * Versuchen Sie, die Parameter in Ihrem Code anzupassen:

    .. code-block:: python

       tts.set_speed(120)   # langsamer
       tts.set_pitch(60)    # andere Tonhöhe

* **Zugriffsverweigerung bei der Ausführung des Codes**

  * Versuchen Sie, mit ``sudo`` auszuführen:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

Vergleich: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Eigenschaft
     - Espeak
     - Pico2Wave
   * - Stimmqualität
     - Roboterhaft, synthetisch
     - Natürlicher, menschlicher
   * - Sprachen
     - Standard Englisch
     - Weniger, aber gängige
   * - Anpassbar
     - Ja (Geschwindigkeit, Tonhöhe, etc.)
     - Nein (nur Sprache)
   * - Leistung
     - Sehr schnell, leichtgewichtig
     - Etwas langsamer, schwerer