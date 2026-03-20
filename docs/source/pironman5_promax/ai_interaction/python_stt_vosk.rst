.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

3. STT mit Vosk (Offline)
==============================================

Vosk ist eine leichtgewichtige Speech-to-Text (STT)-Engine, die viele Sprachen unterstützt und vollständig **offline** auf dem Raspberry Pi läuft.
Sie benötigen nur einmal Internetzugang, um ein Sprachmodell herunterzuladen. Danach funktioniert alles ohne Netzwerkverbindung.

In dieser Lektion werden wir Vosk mit einem ausgewählten Sprachmodell installieren und testen.


.. _test_vosk:

Vosk testen
--------------------------

**Führen Sie das Programm aus**

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 stt_vosk_stream.py

Wenn Sie diesen Code zum ersten Mal mit einer neuen Sprache ausführen, wird Vosk:

* **Das Sprachmodell automatisch herunterladen** (standardmäßig die kleine Version).
* **Die Liste der unterstützten Sprachen ausgeben**.
* Beginnen, über das Mikrofon auf Audioeingabe zu **hören**.

Sie werden etwa Folgendes im Terminal sehen:

.. code-block:: text

         vosk-model-small-de-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
         ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
         Sag etwas

Das bedeutet:

   * Die Modelldatei (``vosk-model-small-de-0.15``) wurde heruntergeladen.
   * Die Liste der unterstützten Sprachen wurde ausgegeben.
   * Das System hört jetzt — sprechen Sie etwas in das Mikrofon des Pironman 5 Pro MAX, und der erkannte Text wird im Terminal angezeigt.

**Tipps:**

* Halten Sie das Mikrofon etwa **15–30 cm** entfernt für bessere Genauigkeit.
* Wählen Sie ein **Modell, das zu Ihrer Sprache und Ihrem Akzent passt**.
* Verwenden Sie eine ruhige Umgebung, um die Erkennung zu verbessern.

**Code**

.. code-block:: python

   from sunfounder_voice_assistant.stt import Vosk as STT

   stt = STT(language="de")

   while True:
      print("Sag etwas")
      for result in stt.listen(stream=True):
         if result["done"]:
               print(f"final:   {result['final']}")
         else:
               print(f"partial: {result['partial']}", end="\r", flush=True)


**Code-Erklärung:**

* ``stt.listen(stream=True)`` — Startet die Streaming-Spracherkennung und liefert während des Sprechens Zwischenergebnisse.
* ``result["partial"]`` — Zeigt den **Echtzeit-Erkennungstext** an (wird kontinuierlich aktualisiert).
* ``result["final"]`` — Zeigt den **endgültig erkannten Satz** an, wenn Sie aufhören zu sprechen.
* Die Schleife läuft kontinuierlich und ermöglicht eine **freihändige Echtzeit-Transkription**.

Tipp: Dieser Streaming-Modus ist perfekt für **Sprachassistenten**, **Befehlssteuerung** oder **Live-Transkription**.

Fehlerbehebung
-----------------

* **Keine solche Datei oder kein solches Verzeichnis (bei der Ausführung von `arecord`)**

  Möglicherweise haben Sie die falsche Karten-/Gerätenummer verwendet.
  Führen Sie Folgendes aus:

  .. code-block:: bash

     arecord -l

  und ersetzen Sie ``1,0`` durch die für Ihr USB-Mikrofon angezeigten Nummern.

* **Aufgenommene Datei hat keinen Ton**

  Öffnen Sie den Mixer und überprüfen Sie die Mikrofonlautstärke:

  .. code-block:: bash

     alsamixer

  * Drücken Sie **F6**, um Ihr USB-Mikrofon auszuwählen.
  * Stellen Sie sicher, dass **Mic/Capture** nicht stummgeschaltet ist (**[OO]** anstelle von **[MM]**).
  * Erhöhen Sie den Pegel mit ↑.

* **Vosk erkennt Sprache nicht**

  * Stellen Sie sicher, dass der **Sprachcode** mit Ihrem Modell übereinstimmt (z.B. ``de`` für Deutsch, ``en-us`` für Englisch).
  * Halten Sie das Mikrofon 15–30 cm entfernt und vermeiden Sie Hintergrundgeräusche.
  * Sprechen Sie klar und langsam.

* **Hohe Latenz / langsame Erkennung**

  * Der standardmäßige Autodownload ist ein **kleines Modell** (schneller, aber weniger genau).
  * Wenn es immer noch langsam ist, schließen Sie andere Programme, um CPU frei zu geben.