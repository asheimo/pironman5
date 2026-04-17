.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Expansor de E/S
================

.. image:: img/io_board.png

LEDs RGB
------------

.. image:: img/io_board_rgb.png

La placa cuenta con 18 LEDs RGB direccionables WS2812B: 6 en la placa y 12 integrados en los ventiladores RGB, ofreciendo un control personalizable. Los usuarios pueden encenderlos o apagarlos, cambiar el color, ajustar el brillo, cambiar los modos de visualización y establecer la velocidad de los cambios.

Pin de Control RGB
-------------------------

El LED RGB es controlado por SPI y está conectado a **GPIO10**, que también es el pin SPI MOSI. Los dos pines mostrados se utilizan para conectar el RGB a GPIO10. Si no se necesita, se puede retirar el puente.

  .. image:: img/io_board_rgb_pin.png

Pines de Salida RGB
-------------------------

.. image:: img/io_board_rgb_out.png

Los LEDs RGB WS2812 soportan conexión en serie, permitiendo la conexión de una tira de LED RGB externa. Conecte el pin **SIG** al pin **DIN** de la tira externa para la expansión.

La placa cuenta con 18 LEDs RGB direccionables WS2812B: 6 en la placa y 12 integrados en los ventiladores RGB. Conecte LEDs adicionales y actualice la cantidad usando:

.. code-block:: shell

  sudo pironman5 --rgb-led-count [cantidad]

Ejemplo:

.. code-block:: shell

  sudo pironman5 --rgb-led-count 24

Conector de la Pantalla OLED
----------------------------

El conector de la pantalla OLED, con una dirección 0x3C, es una característica clave.

.. image:: img/io_board_oled.png

Si la pantalla OLED no muestra o muestra incorrectamente, puede seguir estos pasos para solucionar el problema:

Verifique si el cable FPC de la pantalla OLED está correctamente conectado.

#. Use el siguiente comando para ver los registros de ejecución del programa y verificar si hay mensajes de error.

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. Alternativamente, use el siguiente comando para verificar si la dirección i2c 0x3C del OLED es reconocida:

    .. code-block:: shell

        sudo i2cdetect -y 1

#. Si los dos primeros pasos no revelan ningún problema, intente reiniciar el servicio pironman5 para ver si eso resuelve el problema.

    .. code-block:: shell

        sudo systemctl restart pironman5.service

Receptor Infrarrojo
---------------------------

.. image:: img/io_board_receiver.png

* **Modelo**: IRM-56384, operando a 38KHz.
* **Conexión**: El receptor IR se conecta a **GPIO13**.
* **D7**: Un indicador de recepción infrarroja que parpadea al detectar una señal.
* **J6**: Un pin para habilitar la función infrarroja. Por defecto, se inserta un puente para funcionalidad inmediata. Retire el puente para liberar GPIO13 si no se usa el receptor IR.

Para utilizar el receptor IR, verifique su conexión e instale el módulo necesario:

* Pruebe la conexión:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Instale el módulo ``lirc``:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Ahora, pruebe el Receptor IR ejecutando el siguiente comando.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Después de ejecutar el comando, presione un botón en el control remoto y se imprimirá el código de ese botón.

Pines de los Ventiladores RGB
--------------------------------------------

.. image:: img/io_board_pin_fan.png

La placa de expansión de E/S soporta hasta tres ventiladores PWM de 5V. Todos los ventiladores se controlan juntos.

La señal de control del ventilador está conectada al puerto **FAN IN** en la placa de expansión de E/S, y luego sale de los tres puertos de ventilador dedicados. Estos puertos están numerados de arriba a abajo como **REAR UPPER**, **REAR LOWER** y **CPU FAN**. Conéctelos según la serigrafía, de lo contrario afectará el control RGB en el ventilador.

Cabezales de Pines
------------------------------

.. image:: img/io_board_pin_header.png

Dos conectores de cabezal en ángulo recto extienden los GPIO de la Raspberry Pi, pero tenga en cuenta que el receptor IR, el LED RGB y el ventilador ocupan algunos pines. Retire los puentes correspondientes para utilizar estos pines para otras funciones.

.. list-table::
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 MAX
    - Raspberry Pi 5
  * - Receptor IR (Opcional)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - Ventilador (Opcional)
    - GPIO6
  * - FLED (Opcional)
    - GPIO5
  * - RGB (Opcional)
    - GPIO10