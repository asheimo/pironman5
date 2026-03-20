.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




Pan-Tilt-Kameramodul
===========================================


.. image:: img/pan_tilt.jpg
    :width: 600
    :align: center


.. note::

    Die Pironman-5-Serie enthält kein Kameramodul.
    Sie müssen eines selbst vorbereiten oder auf unserer offiziellen Website erwerben:

    * `AI Fusion Lab Kit <https://www.sunfounder.com/products/sunfounder-ai-fusion-lab-kit>`_

In diesem Abschnitt lernen Sie, wie Sie ein Pan-Tilt-Kameramodul mit zwei SG90-Servos einrichten und steuern, die direkt mit den GPIO-Pins verbunden werden. Am Ende dieses Abschnitts haben Sie ein vollständig installiertes und funktionsfähiges Pan-Tilt-Modul, das für Ihre Projekte bereit ist.

Hardware-Verbindung
-------------------------------------------

Stellen Sie vor dem Start sicher, dass Ihr Raspberry Pi ausgeschaltet ist.

**Verbindungsdiagramm:**


.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Gerät
     - GPIO-Pin
     - Physischer Pin
   * - Pan-Servo (Orange)
     - GPIO17
     - Pin 11
   * - Tilt-Servo (Orange)
     - GPIO18
     - Pin 12
   * - VCC (Rot)
     - 5V
     - Pin 2 oder 4
   * - GND (Braun)
     - GND
     - Pin 6, 9, 14, 20, 25, 30, 34, 39
   * - Kameramodul
     - CSI-Schnittstelle
     - An Kameraanschluss anschließen



.. warning::

    Während SG90-Servos während des Tests direkt vom 5V-Pin des Raspberry Pi mit Strom versorgt werden können, können längere Verwendung oder gleichzeitige Bewegung beider Servos zu Spannungsabfällen und Systeminstabilität führen. Erwägen Sie für längerfristige Projekte die Verwendung einer externen 5V-Stromversorgung (gemeinsame Masse mit dem Raspberry Pi sicherstellen).

**Schritt-für-Schritt-Verbindung:**

1. **Servos anschließen**:

   - Verbinden Sie das orangefarbene Signalkabel des Pan-Servos mit GPIO17 (physischer Pin 11)
   - Verbinden Sie das orangefarbene Signalkabel des Tilt-Servos mit GPIO18 (physischer Pin 12)
   - Verbinden Sie die roten VCC-Kabel beider Servos mit einem 5V-Pin (physischer Pin 2 oder 4)
   - Verbinden Sie die braunen GND-Kabel beider Servos mit einem beliebigen GND-Pin (z.B. physischer Pin 6)

2. **Kamera anschließen**:

   - Hebeln Sie vorsichtig die Plastikklammer des CSI-Kameraanschlusses hoch
   - Führen Sie das Kamera-Flachbandkabel mit den Metallkontakten vom Ethernet-Anschluss weg zeigend ein
   - Drücken Sie die Plastikklammer wieder herunter, um das Kabel zu sichern

Servo testen
-------------------------------------------

Bevor Sie das vollständige Pan-Tilt-Beispiel ausführen, testen wir jeden Servo einzeln, um sicherzustellen, dass sie korrekt funktionieren.

**1. GPIO und I2C aktivieren (falls erforderlich):**

.. code-block:: bash

    sudo raspi-config
    # Navigieren Sie zu: Schnittstellenoptionen -> I2C -> Aktivieren
    # Nach der Aktivierung neu starten

**2. Einfaches Servo-Testskript:**

Erstellen Sie eine Testdatei ``servo_test.py``:

.. code-block:: python

    #!/usr/bin/env python3
    # servo_test.py - Einfacher Servo-Test

    from gpiozero import Servo
    import time

    # Pan-Servo an GPIO17 testen
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    print("Teste Pan-Servo (GPIO17)...")
    print("Bewege in 0°-Position...")
    pan.value = -1  # 0°
    time.sleep(2)

    print("Bewege in 90°-Position...")
    pan.value = 0   # 90°
    time.sleep(2)

    print("Bewege in 180°-Position...")
    pan.value = 1   # 180°
    time.sleep(2)

    pan.close()
    print("Pan-Servo-Test abgeschlossen")

**3. Test ausführen:**

.. code-block:: bash

    python3 servo_test.py

Wenn sich der Servo gleichmäßig durch alle Positionen bewegt, wiederholen Sie den Test für den Tilt-Servo, indem Sie die Pinnummer auf 18 ändern.

Kamera testen
-------------------------------------------

**1. Kameraschnittstelle aktivieren:**

.. code-block:: bash

    sudo raspi-config
    # Navigieren Sie zu: Schnittstellenoptionen -> Kamera -> Aktivieren
    # Oder für neuere Systeme: Schnittstellenoptionen -> Legacy-Kamera -> Aktivieren
    sudo reboot

**2. Kameraaufnahme testen:**

Für Raspberry Pi OS Bullseye und neuer (mit libcamera):

.. code-block:: bash

    # Testfoto aufnehmen
    libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480

    # Kamerabildvorschau anzeigen
    libcamera-hello -t 0

Für ältere Systeme (mit raspistill):

.. code-block:: bash

    # Testfoto aufnehmen
    raspistill -o test.jpg -t 2000 -w 640 -h 480

    # Kamerabildvorschau anzeigen
    raspivid -t 0

**3. Foto überprüfen:**

.. code-block:: bash

    ls -l test.jpg
    # Bild öffnen (falls Sie eine GUI haben)
    xdg-open test.jpg

Pan-Tilt-Beispiel
-------------------------------------------

Kombinieren wir nun sowohl die Servosteuerung als auch die Kamerafunktionalität in einem vollständigen Pan-Tilt-Steuerungsprogramm. Dieses Beispiel ermöglicht es Ihnen, die Kamerarichtung mit den WSAD-Tasten zu steuern und mit der T-Taste Fotos aufzunehmen.

**1. Pan-Tilt-Steuerungsskript erstellen:**

.. code-block:: bash

    nano ptz_wsad_simple.py

Kopieren Sie den folgenden Code:

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # ptz_wsad_simple.py - Steuerung von PTZ mit WSAD-Tasten, ultraviolett einfache Version

    from gpiozero import Servo
    import os
    from datetime import datetime

    # Servos initialisieren
    # SG90-Parameter: min. Pulsbreite 0.5ms (0°), max. Pulsbreite 2.5ms (180°)
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
    tilt = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    # Startposition (Mitte)
    pan.value = 0
    tilt.value = 0

    print("\n=== SG90 PTZ-Steuerung ===")
    print("W: Hoch")
    print("S: Runter")
    print("A: Links")
    print("D: Rechts")
    print("T: Foto aufnehmen")
    print("C: Zentrieren")
    print("Q: Beenden")
    print("-" * 30)

    def take_photo():
        """Fotoaufnahmefunktion"""
        # Fotoverzeichnis erstellen, falls es nicht existiert
        photo_dir = "/home/pi/Pictures/ptz"
        os.makedirs(photo_dir, exist_ok=True)

        # Dateinamen mit Zeitstempel generieren
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{photo_dir}/ptz_{timestamp}.jpg"

        # Foto mit libcamera aufnehmen (für Raspberry Pi Bullseye und höher)
        # Alternative für ältere Systeme: raspistill verwenden
        os.system(f"libcamera-jpeg -o {filename} -t 1 --width 640 --height 480")

        # Alternativer Befehl für ältere Systeme:
        # os.system(f"raspistill -o {filename} -t 1 -w 640 -h 480")

        print(f"Foto gespeichert: {filename}")

    try:
        while True:
            # Benutzereingabe abfragen
            cmd = input("Befehl eingeben: ").lower().strip()

            if cmd == 'w':
                # Hoch bewegen (Tilt-Winkel erhöhen)
                tilt.value = min(1.0, tilt.value + 0.2)
                print(f"↑ Hoch ({tilt.value:.1f})")

            elif cmd == 's':
                # Runter bewegen (Tilt-Winkel verringern)
                tilt.value = max(-1.0, tilt.value - 0.2)
                print(f"↓ Runter ({tilt.value:.1f})")

            elif cmd == 'a':
                # Links bewegen (Pan-Winkel verringern)
                pan.value = max(-1.0, pan.value - 0.2)
                print(f"← Links ({pan.value:.1f})")

            elif cmd == 'd':
                # Rechts bewegen (Pan-Winkel erhöhen)
                pan.value = min(1.0, pan.value + 0.2)
                print(f"→ Rechts ({pan.value:.1f})")

            elif cmd == 't':
                # Foto aufnehmen
                take_photo()

            elif cmd == 'c':
                # PTZ zentrieren
                pan.value = 0
                tilt.value = 0
                print("PTZ zentriert")

            elif cmd == 'q':
                # Programm beenden
                print("Programm wird beendet")
                break

            else:
                print("Ungültiger Befehl, bitte W/S/A/D/T/C/Q verwenden")

    except KeyboardInterrupt:
        print("\nProgramm durch Benutzer unterbrochen")

    finally:
        # GPIO-Ressourcen freigeben
        pan.close()
        tilt.close()
        print("GPIO bereinigt")

**2. Skript ausführbar machen:**

.. code-block:: bash

    chmod +x ptz_wsad_simple.py

**3. Pan-Tilt-Controller ausführen:**

.. code-block:: bash

    python3 ptz_wsad_simple.py

**4. Kamera steuern:**

- Drücken Sie **W/S**, um nach oben/unten zu neigen
- Drücken Sie **A/D**, um nach links/rechts zu schwenken
- Drücken Sie **T**, um ein Foto aufzunehmen (gespeichert unter `/home/pi/Pictures/ptz/`)
- Drücken Sie **C**, um die Kamera zu zentrieren
- Drücken Sie **Q**, um zu beenden


**Kameraaufnahme:**

Das Skript verwendet ``libcamera-jpeg`` (für neuere Raspberry Pi OS-Versionen) zur Aufnahme von Fotos. Fotos werden automatisch mit Zeitstempeln gespeichert, um Überschreiben zu verhindern.