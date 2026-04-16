.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Modulo Fotocamera Pan-Tilt
===========================================

.. image:: img/pan_tilt.jpg
    :width: 600
    :align: center

.. note::

    La serie Pironman 5 non include un modulo fotocamera.
    Devi procurartene uno da solo o acquistarlo dal nostro sito web ufficiale:

    * `AI Fusion Lab Kit <https://www.sunfounder.com/products/sunfounder-ai-fusion-lab-kit>`_

In questa sezione imparerai come configurare e controllare un modulo fotocamera Pan-Tilt utilizzando due servo SG90 collegati direttamente ai pin GPIO. Alla fine di questa sezione, avrai un modulo Pan-Tilt completamente installato e funzionante, pronto per i tuoi progetti.

Collegamento Hardware
-------------------------------------------

Prima di iniziare, assicurati che il tuo Raspberry Pi sia spento.

**Schema di Collegamento:**

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Dispositivo
     - Pin GPIO
     - Pin Fisico
   * - Servo Pan (Arancione)
     - GPIO17
     - Pin 11
   * - Servo Tilt (Arancione)
     - GPIO18
     - Pin 12
   * - VCC (Rosso)
     - 5V
     - Pin 2 o 4
   * - GND (Marrone)
     - GND
     - Pin 6, 9, 14, 20, 25, 30, 34, 39
   * - Modulo Fotocamera
     - Interfaccia CSI
     - Collega alla porta camera

.. warning::

    Sebbene i servo SG90 possano assorbire energia direttamente dal pin 5V del Raspberry Pi durante i test, un uso prolungato o il movimento simultaneo di entrambi i servo potrebbe causare cali di tensione e instabilità del sistema. Per progetti a lungo termine, considera l'uso di un alimentatore esterno da 5V (assicurando una terra comune con il Raspberry Pi).

**Collegamento Passo-Passo:**

1. **Collega i servo**:

   - Collega il filo del segnale arancione del servo Pan a GPIO17 (pin fisico 11)
   - Collega il filo del segnale arancione del servo Tilt a GPIO18 (pin fisico 12)
   - Collega i fili rossi VCC di entrambi i servo a un pin 5V (pin fisico 2 o 4)
   - Collega i fili marroni GND di entrambi i servo a qualsiasi pin GND (es., pin fisico 6)

2. **Collega la fotocamera**:

   - Solleva delicatamente il fermaglio di plastica sul connettore CSI della fotocamera
   - Inserisci il cavo a nastro della fotocamera con i contatti metallici rivolti lontano dalla porta Ethernet
   - Premi il fermaglio di plastica verso il basso per fissare il cavo

Testare il Servo
-------------------------------------------

Prima di eseguire l'esempio completo di Pan-Tilt, testiamo ciascun servo individualmente per assicurarci che funzionino correttamente.

**1. Abilita GPIO e I2C (se necessario):**

.. code-block:: bash

    sudo raspi-config
    # Naviga a: Interface Options -> I2C -> Enable
    # Riavvia dopo l'abilitazione

**2. Script di test semplice per servo:**

Crea un file di test ``servo_test.py``:

.. code-block:: python

    #!/usr/bin/env python3
    # servo_test.py - Test semplice del servo

    from gpiozero import Servo
    import time

    # Test del servo Pan su GPIO17
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    print("Testing Pan servo (GPIO17)...")
    print("Moving to 0° position...")
    pan.value = -1  # 0°
    time.sleep(2)

    print("Moving to 90° position...")
    pan.value = 0   # 90°
    time.sleep(2)

    print("Moving to 180° position...")
    pan.value = 1   # 180°
    time.sleep(2)

    pan.close()
    print("Pan servo test complete")

**3. Esegui il test:**

.. code-block:: bash

    python3 servo_test.py

Se il servo si muove agevolmente attraverso tutte le posizioni, ripeti il test per il servo Tilt cambiando il numero del pin in 18.

Testare la Fotocamera
-------------------------------------------

**1. Abilita l'interfaccia fotocamera:**

.. code-block:: bash

    sudo raspi-config
    # Naviga a: Interface Options -> Camera -> Enable
    # O per sistemi più recenti: Interface Options -> Legacy Camera -> Enable
    sudo reboot

**2. Test di acquisizione della fotocamera:**

Per Raspberry Pi OS Bullseye e versioni successive (usando libcamera):

.. code-block:: bash

    # Scatta una foto di test
    libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480

    # Anteprima del flusso della fotocamera
    libcamera-hello -t 0

Per sistemi più vecchi (usando raspistill):

.. code-block:: bash

    # Scatta una foto di test
    raspistill -o test.jpg -t 2000 -w 640 -h 480

    # Anteprima del flusso della fotocamera
    raspivid -t 0

**3. Verifica la foto:**

.. code-block:: bash

    ls -l test.jpg
    # Apri l'immagine (se hai un'interfaccia grafica)
    xdg-open test.jpg

Esempio Pan-Tilt
-------------------------------------------

Ora combiniamo il controllo del servo e la funzionalità della fotocamera in un programma completo di controllo Pan-Tilt. Questo esempio ti permette di controllare la direzione della fotocamera usando i tasti WSAD e scattare foto con il tasto T.

**1. Crea lo script di controllo Pan-Tilt:**

.. code-block:: bash

    nano ptz_wsad_simple.py

Copia il seguente codice:

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # ptz_wsad_simple.py - Controllo PTZ con tasti WSAD, versione ultra semplice

    from gpiozero import Servo
    import os
    from datetime import datetime

    # Inizializza i servo
    # Parametri SG90: larghezza impulso min 0.5ms (0°), larghezza impulso max 2.5ms (180°)
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
    tilt = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    # Posizione iniziale (centro)
    pan.value = 0
    tilt.value = 0

    print("\n=== Controllo PTZ SG90 ===")
    print("W: Su")
    print("S: Giù")
    print("A: Sinistra")
    print("D: Destra")
    print("T: Scatta foto")
    print("C: Centro")
    print("Q: Esci")
    print("-" * 30)

    def take_photo():
        """Funzione per scattare foto"""
        # Crea la directory delle foto se non esiste
        photo_dir = "/home/pi/Pictures/ptz"
        os.makedirs(photo_dir, exist_ok=True)

        # Genera nome file con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{photo_dir}/ptz_{timestamp}.jpg"

        # Scatta foto usando libcamera (per Raspberry Pi Bullseye e successivi)
        # Alternativa per sistemi più vecchi: usa raspistill
        os.system(f"libcamera-jpeg -o {filename} -t 1 --width 640 --height 480")

        # Comando alternativo per sistemi più vecchi:
        # os.system(f"raspistill -o {filename} -t 1 -w 640 -h 480")

        print(f"Foto salvata: {filename}")

    try:
        while True:
            # Ricevi input dall'utente
            cmd = input("Inserisci comando: ").lower().strip()

            if cmd == 'w':
                # Muovi su (aumenta angolo tilt)
                tilt.value = min(1.0, tilt.value + 0.2)
                print(f"↑ Su ({tilt.value:.1f})")

            elif cmd == 's':
                # Muovi giù (diminuisci angolo tilt)
                tilt.value = max(-1.0, tilt.value - 0.2)
                print(f"↓ Giù ({tilt.value:.1f})")

            elif cmd == 'a':
                # Muovi sinistra (diminuisci angolo pan)
                pan.value = max(-1.0, pan.value - 0.2)
                print(f"← Sinistra ({pan.value:.1f})")

            elif cmd == 'd':
                # Muovi destra (aumenta angolo pan)
                pan.value = min(1.0, pan.value + 0.2)
                print(f"→ Destra ({pan.value:.1f})")

            elif cmd == 't':
                # Scatta foto
                take_photo()

            elif cmd == 'c':
                # Centra il PTZ
                pan.value = 0
                tilt.value = 0
                print("PTZ centrato")

            elif cmd == 'q':
                # Esci dal programma
                print("Uscita dal programma")
                break

            else:
                print("Comando non valido, usa W/S/A/D/T/C/Q")

    except KeyboardInterrupt:
        print("\nProgramma interrotto dall'utente")

    finally:
        # Pulisci le risorse GPIO
        pan.close()
        tilt.close()
        print("GPIO puliti")

**2. Rendi eseguibile lo script:**

.. code-block:: bash

    chmod +x ptz_wsad_simple.py

**3. Esegui il controller Pan-Tilt:**

.. code-block:: bash

    python3 ptz_wsad_simple.py

**4. Controlla la fotocamera:**

- Premi **W/S** per inclinare su/giù
- Premi **A/D** per panoramica sinistra/destra
- Premi **T** per scattare una foto (salvata in `/home/pi/Pictures/ptz/`)
- Premi **C** per centrare la fotocamera
- Premi **Q** per uscire

**Acquisizione Fotocamera:**

Lo script usa ``libcamera-jpeg`` (per le versioni più recenti di Raspberry Pi OS) per acquisire le foto. Le foto vengono salvate automaticamente con timestamp per evitare sovrascritture.