.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_view_control_commands:

Control mediante Comandos
========================================
Además de ver los datos del Pironman 5 Pro MAX y controlar varios dispositivos a través del Panel, también puede usar comandos para controlarlos.

Ver las Configuraciones Básicas
-----------------------------------

El módulo ``pironman5`` ofrece configuraciones básicas para Pironman, que puede revisar con el siguiente comando.

.. code-block:: shell

  sudo pironman5 -c

Las configuraciones estándar aparecen de la siguiente manera:

.. code-block:: 

  {
      "system": {
          "data_interval": 1,
          "enable_history": true,
          "rgb_color": "#ff3dbe",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 18,
          "temperature_unit": "C",
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "default_dashboard_page": "small",
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "debug_level": "INFO"
      }
  }

Personalice estas configuraciones según sus necesidades.

Use ``pironman5`` o ``pironman5 -h`` para obtener instrucciones.

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Interfaz de línea de comandos para Pironman 5 Pro Max

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rs, --rgb-style [RGB_STYLE]
                          RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u, --temperature-unit [{C,F}]
                          Temperature unit
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

  Subcommands:
    {start,stop,launch-browser}
      start               Start Pironman5
      stop                Stop Pironman5
      launch-browser      Launch browser

.. note::

  Cada vez que modifique el estado de ``pironman5.service``, necesita usar el siguiente comando para que los cambios de configuración surtan efecto.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Verifique el estado del programa ``pironman5`` usando la herramienta ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternativamente, inspeccione los archivos de registro generados por el programa.

  .. code-block:: shell

    ls /var/log/pironman5/

**Control de LEDs RGB**
----------------------------------------------
La placa cuenta con 18 LEDs RGB direccionables WS2812B: 6 en la placa y 12 integrados en los ventiladores RGB. Los usuarios pueden controlar la alimentación, el color, el brillo, los modos de visualización, la velocidad de animación y el número de LEDs activos.

.. note::

  Después de modificar la configuración de ``pironman5.service``, debe reiniciar el servicio para que los cambios surtan efecto:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **Habilitar/Deshabilitar LEDs RGB**: Use ``true`` para encender, ``false`` para apagar.

.. code-block:: shell

  sudo pironman5 -re true

* **Cambiar Color**: Establezca un color usando un valor hexadecimal (sin el `#`), por ejemplo, ``fe1a1a`` para rojo.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* **Ajustar Brillo**: Establezca el brillo del 0% al 100%.

.. code-block:: shell

  sudo pironman5 -rb 75

* **Cambiar Modo de Visualización**: Elija entre varios modos de animación:

  * ``solid``: Color estático.
  * ``breathing``: Atenuación pulsante.
  * ``flow`` / ``flow_reverse``: El color fluye en una dirección.
  * ``rainbow`` / ``rainbow_reverse``: Cicla a través del espectro arcoíris.
  * ``hue_cycle``: Cicla suavemente a través de los valores de tono.

.. code-block:: shell

  sudo pironman5 -rs breathing

.. note::

  Cuando use los modos ``rainbow``, ``rainbow_reverse`` o ``hue_cycle``, el color establecido mediante ``pironman5 -rc`` será sobrescrito por el ciclo de color automático del modo.

* **Ajustar Velocidad de Animación**: Controle la velocidad de los efectos del 0% (más lento) al 100% (más rápido).

.. code-block:: shell

  sudo pironman5 -rp 50

* **Establecer Cantidad de LEDs**: El sistema por defecto controla 18 LEDs. Si ha extendido la cadena con LEDs WS2812B externos adicionales, actualice el número total en consecuencia.

.. code-block:: shell

  sudo pironman5 -rl 12

**Ventilador**
--------------------------------

Este ventilador se conecta a un puerto dedicado de ventilador PWM de 4 pines en la Raspberry Pi 5. Su estrategia de control predeterminada es un esquema de ajuste de velocidad inteligente de múltiples niveles gestionado por firmware, basado en la temperatura de la CPU. Esto significa que cuando usa un ventilador PWM oficial o compatible y lo conecta correctamente, el sistema ajustará automáticamente la velocidad del ventilador según los cambios en la temperatura de la CPU (comenzando a operar por encima de los 50°C) sin ninguna intervención manual de su parte.

**Verificar la Pantalla OLED**
-----------------------------------

La pantalla OLED de 0.96" muestra información del sistema (CPU, RAM, Disco, Temp, IP) por defecto después de instalar la biblioteca ``pironman5`` y reiniciar.

Si la pantalla OLED está en blanco:

1. Asegúrese de que el cable FPC del OLED esté firmemente conectado a la placa base.
2. Verifique el registro del servicio en busca de errores:

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    O verifique el registro específico del OLED:

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3. Verifique que el OLED sea detectado en el bus I2C (dirección `0x3C`):

    .. code-block:: shell

      i2cdetect -y 1

**Comandos de Configuración del OLED**

* **Habilitar/Deshabilitar OLED**: Encienda o apague la pantalla OLED.

    .. code-block:: shell

      sudo pironman5 -oe false

* **Rotar Pantalla**: Establezca la orientación de la pantalla a ``0`` (predeterminado) o ``180`` grados.

    .. code-block:: shell

      sudo pironman5 -or 180

* **Configurar Páginas de Visualización**: Elija qué páginas de información recorrer. Las páginas son: ``mix`` (resumen), ``performance`` (CPU/RAM detallado), ``ips`` (IPs de red), ``disk`` (almacenamiento). Separe múltiples páginas con comas.

    .. code-block:: shell

      sudo pironman5 -op mix,ips,disk

* **Establecer Tiempo de Reposo**: Defina cuántos segundos de inactividad antes de que el OLED se apague (0 = nunca dormir).

    .. code-block:: shell

      sudo pironman5 -os 120

**Verificar el Receptor Infrarrojo**
---------------------------------------

El receptor IR incorporado permite el control mediante control remoto.

1. Instale el software necesario:

    .. code-block:: shell

      sudo apt-get install lirc -y

2. Pruebe el receptor. Ejecute el siguiente comando, luego apunte un control remoto hacia la carcasa y presione botones. Debería ver la salida del código en bruto.

    .. code-block:: shell

      mode2 -d /dev/lirc0

3. Para configurar asignaciones de botones específicas del control remoto (por ejemplo, para Kodi o Volumio), necesitará configurar el archivo `/etc/lirc/lircd.conf` con los códigos de su control remoto.

**Comandos Generales del Sistema**
-------------------------------------------------------

* **Mostrar Versión**: Muestra la versión del paquete ``pironman5`` instalado.

.. code-block:: shell

  sudo pironman5 -v

* **Mostrar Configuración Actual**: Muestra todos los ajustes actuales.

.. code-block:: shell

  sudo pironman5 -c

* **Establecer Unidad de Temperatura**: Cambie entre Celsius (``C``) y Fahrenheit (``F``) para las visualizaciones de temperatura.

.. code-block:: shell

  sudo pironman5 -u F

* **Configurar Registro de Datos**:

  * **Establecer Días de Retención de la Base de Datos**: Controle cuántos días de datos históricos (como registros de temperatura) se conservan.

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **Habilitar/Deshabilitar Registro Histórico**: Active o desactive la recopilación de datos.

    .. code-block:: shell

      sudo pironman5 -eh false

* **Establecer Nivel de Verbosidad del Registro**: Ajuste el nivel de detalle de los registros del sistema. Opciones: ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``.

.. code-block:: shell

  sudo pironman5 -dl DEBUG

* **Eliminar Panel Web**: Desinstale la interfaz de administración web opcional.

.. code-block:: shell

  sudo pironman5 -rd

* **Especificar Ruta de Configuración Personalizada**: Use un archivo de configuración desde una ubicación no estándar.

.. code-block:: shell

  sudo pironman5 -cp /home/pi/my_custom_config.json

**Subcomandos de Gestión del Servicio**
------------------------------------------------------------------

* **Iniciar el Servicio Pironman5**: Inicie manualmente el servicio en segundo plano que gestiona los LEDs, ventilador, OLED, etc.

.. code-block:: shell

  sudo pironman5 start

* **Detener el Servicio Pironman5**: Detenga de forma ordenada el servicio en segundo plano.

.. code-block:: shell

  sudo pironman5 stop

* **Lanzar el Panel Web en el Navegador**: Si el panel web está instalado, este comando lo abrirá en su navegador predeterminado.

.. code-block:: shell

  sudo pironman5 launch-browser