.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

4. Text-Vision-Gespräch mit Ollama
======================================================

In dieser Lektion lernen Sie, wie Sie **Ollama** verwenden, ein Werkzeug zum lokalen Ausführen großer Sprach- und Bildmodelle.
Wir zeigen Ihnen, wie Sie Ollama installieren, ein Modell herunterladen und den Pironman 5 Pro MAX damit verbinden.

Mit diesem Setup kann der Pironman 5 Pro MAX ein Kamerabild aufnehmen und das Modell wird **sehen und erzählen** —
Sie können beliebige Fragen zum Bild stellen, und das Modell wird in natürlicher Sprache antworten.

.. _download_ollama:

1. Ollama (LLM) installieren und Modell herunterladen
------------------------------------------------------------------------------

Sie können wählen, wo Sie **Ollama** installieren möchten:

* Auf Ihrem Raspberry Pi (lokaler Betrieb)
* Oder auf einem anderen Computer (Mac/Windows/Linux) im **gleichen lokalen Netzwerk**

**Empfohlene Modelle vs. Hardware**

Sie können jedes auf |link_ollama_hub| verfügbare Modell auswählen.
Modelle gibt es in verschiedenen Größen (3B, 7B, 13B, 70B...).
Kleinere Modelle laufen schneller und benötigen weniger Speicher, während größere Modelle eine bessere Qualität bieten, aber leistungsstarke Hardware erfordern.

In der folgenden Tabelle können Sie entscheiden, welche Modellgröße zu Ihrem Gerät passt.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Modellgröße
     - Min. benötigter RAM
     - Empfohlene Hardware
   * - ~3B Parameter
     - 8GB (16GB besser)
     - Raspberry Pi 5 (16GB) oder Mittelklasse-PC/Mac
   * - ~7B Parameter
     - 16GB+
     - Pi 5 (16GB, gerade nutzbar) oder Mittelklasse-PC/Mac
   * - ~13B Parameter
     - 32GB+
     - Desktop-PC / Mac mit viel RAM
   * - 30B+ Parameter
     - 64GB+
     - Workstation / Server / GPU empfohlen
   * - 70B+ Parameter
     - 128GB+
     - Hochleistungsserver mit mehreren GPUs

**Installation auf dem Raspberry Pi**

Wenn Sie Ollama direkt auf Ihrem Raspberry Pi ausführen möchten:

* Verwenden Sie ein **64-Bit-Raspberry-Pi-OS**
* Starke Empfehlung: **Raspberry Pi 5 (16GB RAM)**

Führen Sie die folgenden Befehle aus:

.. code-block:: bash

   # Ollama installieren
   curl -fsSL https://ollama.com/install.sh | sh

   # Ein leichtes Modell herunterladen (gut zum Testen)
   ollama pull llama3.2:3b

   # Schnellen Testlauf durchführen (tippen Sie 'hallo' und drücken Sie Enter)
   ollama run llama3.2:3b

   # API bereitstellen (Standard-Port 11434)
   # Tipp: setzen Sie OLLAMA_HOST=0.0.0.0, um Zugriff aus dem LAN zu ermöglichen
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installation auf Mac / Windows / Linux (Desktop-App)**

1. Laden Sie Ollama von |link_ollama| herunter und installieren Sie es.

   .. image:: img/llm_ollama_download.png

2. Öffnen Sie die Ollama-App, gehen Sie zum **Modellauswahl** und verwenden Sie die Suchleiste, um ein Modell zu finden. Geben Sie zum Beispiel ``llama3.2:3b`` ein (ein kleines und leichtes Modell für den Einstieg).

   .. image:: img/llm_ollama_choose.png

3. Nachdem der Download abgeschlossen ist, geben Sie etwas Einfaches wie "Hallo" im Chatfenster ein. Ollama beginnt automatisch mit dem Download, wenn Sie es zum ersten Mal verwenden.

   .. image:: img/llm_olama_llama_download.png

4. Gehen Sie zu **Einstellungen** → aktivieren Sie **Ollama für das Netzwerk freigeben**. Dadurch kann Ihr Raspberry Pi über das LAN eine Verbindung herstellen.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Wenn Sie einen Fehler sehen wie:

   ``Error: model requires more system memory ...``

   Das Modell ist für Ihren Computer zu groß.
   Verwenden Sie ein **kleineres Modell** oder wechseln Sie zu einem Computer mit mehr RAM.

2. Ollama testen
---------------------------------------

Sobald Ollama installiert und Ihr Modell bereit ist, können Sie es schnell mit einer einfachen Chatschleife testen.

**Führen Sie das Programm aus**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 llm_ollama.py

Jetzt können Sie direkt vom Terminal aus mit dem Pironman 5 Pro MAX chatten.

   * Sie können **jedes Modell** wählen, das auf |link_ollama_hub| verfügbar ist, aber kleinere Modelle (z.B. ``moondream:1.8b``, ``phi3:mini``) werden empfohlen, wenn Sie nur 8–16 GB RAM haben.
   * Stellen Sie sicher, dass das im Code angegebene Modell mit dem Modell übereinstimmt, das Sie bereits in Ollama heruntergeladen haben.
   * Geben Sie ``exit`` oder ``quit`` ein, um das Programm zu beenden.
   * Wenn Sie keine Verbindung herstellen können, stellen Sie sicher, dass Ollama läuft und dass sich beide Geräte im selben LAN befinden, falls Sie einen entfernten Host verwenden.

**Code**

.. code-block:: python

   from sunfounder_voice_assistant.llm import Ollama

   INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
   WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

   # Ändern Sie dies auf Ihre Computer-IP, wenn Sie es auf Ihrem Pi ausführen, dann ändern Sie es auf localhost
   llm = Ollama(
      ip="localhost",
      model="llama3.2:3b"
   )

   # Festlegen, wie viele Nachrichten behalten werden sollen
   llm.set_max_messages(20)
   # Anweisungen festlegen
   llm.set_instructions(INSTRUCTIONS)
   # Willkommensnachricht festlegen
   llm.set_welcome(WELCOME)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # Antwort ohne Stream
      # response = llm.prompt(input_text)
      # print(f"response: {response}")

      # Antwort mit Stream
      response = llm.prompt(input_text, stream=True)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")


3. Bildgespräch mit Ollama
--------------------------

In dieser Demo macht die Pi-Kamera **jedes Mal ein Schnappschuss, wenn Sie eine Frage eingeben**.
Das Programm sendet **Ihren eingegebenen Text + das neue Foto** an ein lokales Bildmodell über Ollama
und gibt dann die Antwort des Modells in Klartext aus.
Dies ist eine minimale "Sehen & Erzählen"-Grundlage, die Sie später mit Farb-/Gesichts-/QR-Überprüfungen erweitern können.

**Vorbereitung**

#. Öffnen Sie die **Ollama**-App (oder führen Sie den Dienst aus) und stellen Sie sicher, dass ein **bildverarbeitendes Modell** heruntergeladen wurde.

   * Wenn Sie genügend Arbeitsspeicher haben (≥16 GB RAM), können Sie ``llava:7b`` ausprobieren.
   * Wenn Sie nur **8 GB RAM** haben, bevorzugen Sie ein kleineres Modell wie ``moondream:1.8b`` oder ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Demo ausführen**

#. Gehen Sie zum Beispielordner und führen Sie das Skript aus:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      python3 llm_ollama_with_image.py

#. Was passiert, wenn es läuft:

   * Das Programm gibt eine Willkommenszeile aus und wartet auf Ihre Eingabe (``>>>``).
   * **Jedes Mal, wenn Sie etwas eingeben** (z.B. "hallo", "Ist da Gelb?", "Irgendwelche Gesichter?", "Was ist auf dem Schreibtisch?"), passiert Folgendes:

     * Es **macht ein Foto** mit der Pi-Kamera (gespeichert unter ``/tmp/llm-img.jpg``),
     * **sendet Ihren Text + das Foto** an das Bildmodell über Ollama,
     * **gibt die Antwort** des Modells im Terminal aus.

   * Geben Sie ``exit`` oder ``quit`` ein, um das Programm zu beenden.

**Code**

.. code-block:: python

   from sunfounder_voice_assistant.llm import Ollama
   from picamera2 import Picamera2
   import time

   '''
   Sie müssen zuerst Ollama einrichten, siehe llm_local.py

   Sie benötigen mindestens 8 GB RAM, um das große multimodale Modell llava:7b auszuführen.
   '''

   INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
   WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

   llm = Ollama(
      ip="localhost",          # z.B. "192.168.100.145" wenn entfernt
      model="llava:7b"         # ändern zu "moondream:1.8b" oder "granite3.2-vision:2b" für 8GB RAM
   )

   # Festlegen, wie viele Nachrichten behalten werden sollen
   llm.set_max_messages(20)
   # Anweisungen festlegen
   llm.set_instructions(INSTRUCTIONS)
   # Willkommensnachricht festlegen
   llm.set_welcome(WELCOME)

   # Kamera initialisieren
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

      # Bild aufnehmen
      img_path = '/tmp/llm-img.jpg'
      camera.capture_file(img_path)

      # Antwort ohne Stream
      # response = llm.prompt(input_text, image_path=img_path)
      # print(f"response: {response}")

      # Antwort mit Stream
      response = llm.prompt(input_text, stream=True, image_path=img_path)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")


Fehlerbehebung
---------------


* **Ich erhalte einen Fehler wie: `model requires more system memory ...`.**

  * Das bedeutet, dass das Modell für Ihr Gerät zu groß ist.
  * Verwenden Sie ein kleineres Modell wie ``moondream:1.8b`` oder ``granite3.2-vision:2b``.
  * Oder wechseln Sie zu einem Computer mit mehr RAM und geben Sie Ollama für das Netzwerk frei.

* **Der Code kann keine Verbindung zu Ollama herstellen (Verbindung abgelehnt).**

  Überprüfen Sie Folgendes:

  * Stellen Sie sicher, dass Ollama läuft (``ollama serve`` oder die Desktop-App ist geöffnet).
  * Wenn Sie einen entfernten Computer verwenden, aktivieren Sie **Für Netzwerk freigeben** in den Ollama-Einstellungen.
  * Überprüfen Sie, ob die ``ip="..."`` in Ihrem Code mit der korrekten LAN-IP übereinstimmt.
  * Bestätigen Sie, dass sich beide Geräte im selben lokalen Netzwerk befinden.

* **Meine Pi-Kamera nimmt nichts auf.**

  * Überprüfen Sie, ob ``Picamera2`` installiert ist und mit einem einfachen Testskript funktioniert.
  * Stellen Sie sicher, dass das Kamerakabel richtig angeschlossen und in ``raspi-config`` aktiviert ist.
  * Stellen Sie sicher, dass Ihr Skript die Berechtigung hat, in den Zielpfad (``/tmp/llm-img.jpg``) zu schreiben.

* **Die Ausgabe ist zu langsam.**

  * Kleinere Modelle antworten schneller, aber mit einfacheren Antworten.
  * Sie können die Kameraauflösung verringern (z.B. 640×480 anstatt 1280×720), um die Bildverarbeitung zu beschleunigen.
  * Schließen Sie andere Programme auf Ihrem Pi, um CPU und RAM freizugeben.