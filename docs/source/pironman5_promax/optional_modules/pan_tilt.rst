.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Módulo de Cámara Pan-Tilt
===========================================

.. image:: img/pan_tilt.jpg
    :width: 600
    :align: center

.. note::

    La serie Pironman 5 no incluye un módulo de cámara.
    Necesita preparar uno usted mismo o comprarlo en nuestro sitio web oficial:

    * `AI Funsion Lab Kit <https://www.sunfounder.com/products/sunfounder-ai-fusion-lab-kit>`_

En esta sección, aprenderá cómo configurar y controlar un módulo de cámara Pan-Tilt usando dos servomotores SG90 conectados directamente a los pines GPIO. Al final de esta sección, tendrá un módulo Pan-Tilt completamente instalado y funcional listo para sus proyectos.

Conexión de Hardware
-------------------------------------------

Antes de comenzar, asegúrese de que su Raspberry Pi esté apagada.

**Diagrama de Conexión:**

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Dispositivo
     - Pin GPIO
     - Pin Físico
   * - Servo Pan (Naranja)
     - GPIO17
     - Pin 11
   * - Servo Tilt (Naranja)
     - GPIO18
     - Pin 12
   * - VCC (Rojo)
     - 5V
     - Pin 2 o 4
   * - GND (Marrón)
     - GND
     - Pin 6, 9, 14, 20, 25, 30, 34, 39
   * - Módulo de Cámara
     - Interfaz CSI
     - Conectar al puerto de la cámara

.. warning::

    Aunque los servos SG90 pueden obtener alimentación directamente del pin 5V de la Raspberry Pi durante las pruebas, el uso prolongado o el movimiento simultáneo de ambos servos puede causar caídas de voltaje e inestabilidad del sistema. Para proyectos a largo plazo, considere usar una fuente de alimentación externa de 5V (asegure una tierra común con la Raspberry Pi).

**Conexión Paso a Paso:**

1. **Conecte los servos**:

   - Conecte el cable de señal naranja del servo Pan a GPIO17 (pin físico 11)
   - Conecte el cable de señal naranja del servo Tilt a GPIO18 (pin físico 12)
   - Conecte los cables rojos VCC de ambos servos a un pin 5V (pin físico 2 o 4)
   - Conecte los cables marrones GND de ambos servos a cualquier pin GND (ej., pin físico 6)

2. **Conecte la cámara**:

   - Levante suavemente el clip de plástico en el conector CSI de la cámara
   - Inserte el cable plano de la cámara con los contactos metálicos mirando hacia afuera del puerto Ethernet
   - Presione el clip de plástico hacia abajo para asegurar el cable

Probar el Servo
-------------------------------------------

Antes de ejecutar el ejemplo completo de Pan-Tilt, probemos cada servo individualmente para asegurarnos de que funcionan correctamente.

**1. Habilitar GPIO e I2C (si es necesario):**

.. code-block:: bash

    sudo raspi-config
    # Navegue a: Interface Options -> I2C -> Enable
    # Reinicie después de habilitar

**2. Script simple de prueba de servo:**

Cree un archivo de prueba ``servo_test.py``:

.. code-block:: python

    #!/usr/bin/env python3
    # servo_test.py - Prueba simple de servo

    from gpiozero import Servo
    import time

    # Probar servo Pan en GPIO17
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    print("Probando servo Pan (GPIO17)...")
    print("Moviendo a posición 0°...")
    pan.value = -1  # 0°
    time.sleep(2)

    print("Moviendo a posición 90°...")
    pan.value = 0   # 90°
    time.sleep(2)

    print("Moviendo a posición 180°...")
    pan.value = 1   # 180°
    time.sleep(2)

    pan.close()
    print("Prueba del servo Pan completada")

**3. Ejecute la prueba:**

.. code-block:: bash

    python3 servo_test.py

Si el servo se mueve suavemente a través de todas las posiciones, repita la prueba para el servo Tilt cambiando el número de pin a 18.

Probar la Cámara
-------------------------------------------

**1. Habilite la interfaz de la cámara:**

.. code-block:: bash

    sudo raspi-config
    # Navegue a: Interface Options -> Camera -> Enable
    # O para sistemas más nuevos: Interface Options -> Legacy Camera -> Enable
    sudo reboot

**2. Pruebe la captura de la cámara:**

Para Raspberry Pi OS Bullseye y más recientes (usando libcamera):

.. code-block:: bash

    # Tomar una foto de prueba
    libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480

    # Vista previa del feed de la cámara
    libcamera-hello -t 0

Para sistemas más antiguos (usando raspistill):

.. code-block:: bash

    # Tomar una foto de prueba
    raspistill -o test.jpg -t 2000 -w 640 -h 480

    # Vista previa del feed de la cámara
    raspivid -t 0

**3. Verifique la foto:**

.. code-block:: bash

    ls -l test.jpg
    # Abrir la imagen (si tiene interfaz gráfica)
    xdg-open test.jpg

Ejemplo de Pan-Tilt
-------------------------------------------

Ahora combinemos el control de los servos y la funcionalidad de la cámara en un programa completo de control Pan-Tilt. Este ejemplo le permite controlar la dirección de la cámara usando las teclas WSAD y tomar fotos con la tecla T.

**1. Cree el script de control Pan-Tilt:**

.. code-block:: bash

    nano ptz_wsad_simple.py

Copie el siguiente código:

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # ptz_wsad_simple.py - Control PTZ con teclas WSAD, versión ultra simple

    from gpiozero import Servo
    import os
    from datetime import datetime

    # Inicializar servos
    # Parámetros SG90: ancho de pulso mínimo 0.5ms (0°), ancho de pulso máximo 2.5ms (180°)
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
    tilt = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    # Posición inicial (centro)
    pan.value = 0
    tilt.value = 0

    print("\n=== Control PTZ SG90 ===")
    print("W: Arriba")
    print("S: Abajo")
    print("A: Izquierda")
    print("D: Derecha")
    print("T: Tomar foto")
    print("C: Centrar")
    print("Q: Salir")
    print("-" * 30)

    def take_photo():
        """Función para tomar foto"""
        # Crear directorio de fotos si no existe
        photo_dir = "/home/pi/Pictures/ptz"
        os.makedirs(photo_dir, exist_ok=True)

        # Generar nombre de archivo con marca de tiempo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{photo_dir}/ptz_{timestamp}.jpg"

        # Tomar foto usando libcamera (para Raspberry Pi Bullseye y superior)
        # Alternativa para sistemas más antiguos: usar raspistill
        os.system(f"libcamera-jpeg -o {filename} -t 1 --width 640 --height 480")

        # Comando alternativo para sistemas más antiguos:
        # os.system(f"raspistill -o {filename} -t 1 -w 640 -h 480")

        print(f"Foto guardada: {filename}")

    try:
        while True:
            # Obtener entrada del usuario
            cmd = input("Ingrese comando: ").lower().strip()

            if cmd == 'w':
                # Mover arriba (aumentar ángulo de inclinación)
                tilt.value = min(1.0, tilt.value + 0.2)
                print(f"↑ Arriba ({tilt.value:.1f})")

            elif cmd == 's':
                # Mover abajo (disminuir ángulo de inclinación)
                tilt.value = max(-1.0, tilt.value - 0.2)
                print(f"↓ Abajo ({tilt.value:.1f})")

            elif cmd == 'a':
                # Mover izquierda (disminuir ángulo de pan)
                pan.value = max(-1.0, pan.value - 0.2)
                print(f"← Izquierda ({pan.value:.1f})")

            elif cmd == 'd':
                # Mover derecha (aumentar ángulo de pan)
                pan.value = min(1.0, pan.value + 0.2)
                print(f"→ Derecha ({pan.value:.1f})")

            elif cmd == 't':
                # Tomar foto
                take_photo()

            elif cmd == 'c':
                # Centrar el PTZ
                pan.value = 0
                tilt.value = 0
                print("PTZ centrado")

            elif cmd == 'q':
                # Salir del programa
                print("Saliendo del programa")
                break

            else:
                print("Comando inválido, use W/S/A/D/T/C/Q")

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")

    finally:
        # Limpiar recursos GPIO
        pan.close()
        tilt.close()
        print("GPIO limpiado")

**2. Haga el script ejecutable:**

.. code-block:: bash

    chmod +x ptz_wsad_simple.py

**3. Ejecute el controlador Pan-Tilt:**

.. code-block:: bash

    python3 ptz_wsad_simple.py

**4. Controle la cámara:**

- Presione **W/S** para inclinar arriba/abajo
- Presione **A/D** para girar izquierda/derecha
- Presione **T** para tomar una foto (guardada en `/home/pi/Pictures/ptz/`)
- Presione **C** para centrar la cámara
- Presione **Q** para salir

**Captura de Cámara:**

El script usa ``libcamera-jpeg`` (para versiones más recientes de Raspberry Pi OS) para capturar fotos. Las fotos se guardan automáticamente con marcas de tiempo para evitar sobrescrituras.