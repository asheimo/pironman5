.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============

1. Acerca de los Sistemas Compatibles
--------------------------------------------------------

Sistemas que pasaron la prueba en la Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Acerca del Botón de Encendido
---------------------------------------------

El botón de encendido expone el botón de encendido de la Raspberry Pi 5, y funciona igual que el botón de encendido de la Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Apagado**

  * Si ejecuta el sistema **Raspberry Pi OS Desktop**, puede presionar el botón de encendido dos veces rápidamente para apagar.
  * Si ejecuta el sistema **Raspberry Pi OS Lite**, presione el botón de encendido una sola vez para iniciar un apagado.
  * Para forzar un apagado completo, mantenga presionado el botón de encendido.

* **Encendido**

  * Si la placa Raspberry Pi está apagada, pero aún tiene alimentación, presione una vez para encender desde el estado de apagado.

* Si está ejecutando un sistema que no soporta un botón de apagado, puede mantenerlo presionado durante 5 segundos para forzar un apagado completo, y presionar una vez para encender desde el estado de apagado.

3. Acerca del Raspberry Pi AI HAT+
----------------------------------------------------------

El Raspberry Pi AI HAT+ no es compatible con el Pironman 5.

   .. image::  img/output3.png
        :width: 400

El Raspberry Pi AI Kit combina el Raspberry Pi M.2 HAT+ y el módulo acelerador AI Hailo.

   .. image::  img/output2.jpg
        :width: 400

Puede separar el módulo acelerador AI Hailo del Raspberry Pi AI Kit e insertarlo directamente en el módulo NVMe PIP del Pironman 5 MAX.

4. Acerca de los Extremos de los Tubos de Cobre del Enfriador de Torre
---------------------------------------------------------------------------------------

Los tubos de calor en forma de U en la parte superior del enfriador de torre están comprimidos para facilitar que los tubos de cobre pasen a través de las aletas de aluminio, lo cual es parte del proceso normal de producción de los tubos de cobre.

   .. image::  img/tower_cooler1.png

5. ¿La PI5 no arranca (LED rojo)?
-------------------------------------------

Este problema puede ser causado por una actualización del sistema, cambios en el orden de arranque o un bootloader corrupto. Puede intentar los siguientes pasos para resolver el problema:

#. Verifique la Conexión del Adaptador USB-HDMI

   * Verifique cuidadosamente si el adaptador USB-HDMI está firmemente conectado a la PI5.
   * Intente desconectar y volver a conectar el adaptador USB-HDMI.
   * Luego reconecte la fuente de alimentación y verifique si la PI5 arranca correctamente.

#. Pruebe la PI5 Fuera de la Carcasa

   * Si reconectar el adaptador no resuelve el problema:
   * Retire la PI5 de la carcasa Pironman 5.
   * Alimente la PI5 directamente con el adaptador de corriente (sin la carcasa).
   * Verifique si puede arrancar normalmente.

#. Restaure el Bootloader

   * Si la PI5 aún no puede arrancar, el bootloader puede estar corrupto. Puede seguir esta guía: :ref:`update_bootloader_promax` y elegir si arrancar desde la tarjeta SD o desde NVMe/USB.
   * Inserte la tarjeta SD preparada en la PI5, enciéndala y espere al menos 10 segundos. Una vez completada la recuperación, retire y formatee la tarjeta SD.
   * Luego, use Raspberry Pi Imager para grabar la última versión de Raspberry Pi OS, vuelva a insertar la tarjeta e intente arrancar de nuevo.

6. ¿La Pantalla OLED no Funciona?
-----------------------------------------------

Si la pantalla OLED no muestra o muestra incorrectamente, siga estos pasos de solución de problemas:

1. **Verifique la Conexión de la Pantalla OLED**

   Asegúrese de que el cable FPC de la pantalla OLED esté correctamente conectado.

2. **Verifique la Compatibilidad del SO**

   Asegúrese de que está ejecutando un sistema operativo compatible en su Raspberry Pi.

3. **Verifique la Dirección I2C**

   Ejecute el siguiente comando para verificar si la dirección I2C del OLED (0x3C) es reconocida:

   .. code-block:: shell

      sudo i2cdetect -y 1

   Si la dirección no es detectada, habilite I2C usando el siguiente comando:

   .. code-block:: shell

      sudo raspi-config

4. **Reinicie el Servicio pironman5**

   Reinicie el servicio `pironman5` para ver si resuelve el problema:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Verifique el Archivo de Registro**

   Si el problema persiste, verifique el archivo de registro en busca de mensajes de error y proporcione la información al soporte al cliente para un análisis más detallado:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

7. ¿El Módulo NVMe PIP no Funciona?
---------------------------------------

1. Asegúrese de que el cable FPC que conecta el módulo NVMe PIP a la Raspberry Pi 5 esté firmemente conectado.

2. Confirme que su SSD esté correctamente asegurado al módulo NVMe PIP.

3. Verifique el estado de los LEDs del Módulo NVMe PIP:

   Después de confirmar todas las conexiones, encienda el Pironman 5 MAX y observe los dos indicadores en el Módulo NVMe PIP:

   * **PWR LED**: Debería estar encendido.
   * **STA LED**: Debería parpadear para indicar funcionamiento normal.

   .. image:: img/dual_nvme_pip_leds.png

   * Si el **PWR LED** está encendido pero el **STA LED** no parpadea, indica que el SSD NVMe no es reconocido por la Raspberry Pi.
   * Si el **PWR LED** está apagado, puentee los pines "Force Enable" en el módulo. Si el **PWR LED** se enciende, podría indicar un cable FPC suelto o una configuración del sistema no compatible con NVMe.

   .. image:: img/dual_nvme_pip_j4.png

4. Confirme que su SSD NVMe tenga un sistema operativo correctamente instalado. Consulte: :ref:`install_the_os_promax`.

5. Si el cableado es correcto y el SO está instalado, pero el SSD NVMe aún no arranca, intente arrancar desde una tarjeta Micro SD para verificar la funcionalidad de otros componentes. Una vez confirmado, proceda a: :ref:`configure_boot_ssd_promax`.

Si el problema persiste después de realizar los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

8. ¿Los LEDs RGB no Funcionan?
------------------------------------------

#. Los dos pines en el Expansor de E/S encima de J9 se utilizan para conectar los LEDs RGB a GPIO10. Asegúrese de que el puente en estos dos pines esté correctamente colocado.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifique que la Raspberry Pi esté ejecutando un sistema operativo compatible. El Pironman 5 solo soporta las siguientes versiones de SO:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si ha instalado un SO no compatible, siga la guía para instalar un sistema operativo compatible: :ref:`install_the_os_promax`.

#. Ejecute el comando ``sudo raspi-config`` para abrir el menú de configuración. Navegue a **3 Interfacing Options** -> **I3 SPI** -> **YES**, luego haga clic en **OK** y **Finish** para habilitar SPI. Después de habilitar SPI, reinicie el Pironman 5.

Si el problema persiste después de realizar los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.

.. _promax_fan_faq:

9. ¿El ventilador no funciona / no se puede controlar?
----------------------------------------------------------------

El Pro / MAX adopta la solución oficial de control de ventilador PWM de Raspberry Pi. Los tres ventiladores de refrigeración son controlados directamente por el sistema Raspberry Pi y no dependen del servicio pironman5 (por lo tanto, no verá opciones de control de ventiladores en la herramienta de línea de comandos o en el Panel).

**Pruebe si el ventilador funciona correctamente**

Puede controlar manualmente el ventilador usando los siguientes comandos:

.. code-block:: bash

   pinctrl FAN_PWM op dl   # habilitar ventilador (activo bajo)
   pinctrl FAN_PWM op dh   # deshabilitar ventilador (activo alto)
   pinctrl FAN_PWM a0      # modo automático (control por temperatura del sistema)

**Control de Velocidad del Ventilador Basado en la Temperatura**

El ventilador PWM funciona dinámicamente, ajustando su velocidad según la temperatura de la Raspberry Pi 5:

* **Por debajo de 50°C**: El ventilador permanece apagado (0% de velocidad).
* **A 50°C**: El ventilador funciona a baja velocidad (30% de velocidad).
* **A 60°C**: El ventilador aumenta a velocidad media (50% de velocidad).
* **A 67.5°C**: El ventilador acelera a alta velocidad (70% de velocidad).
* **A 75°C o más**: El ventilador funciona a máxima velocidad (100% de velocidad).

10. ¿Cómo activar la pantalla OLED?
---------------------------------------------------------------------------------

Para ahorrar energía y extender la vida útil de la pantalla, la pantalla OLED se apagará automáticamente después de un período de inactividad. Esto es parte del diseño normal y no afecta la funcionalidad del producto.

.. note::

   Para la configuración de la pantalla OLED (como encender/apagar, tiempo de reposo, rotación, etc.), consulte: :ref:`promax_view_control_dashboard` o :ref:`promax_view_control_commands`.

11. ¿Cómo deshabilitar el panel web?
------------------------------------------------------

Una vez que haya completado la instalación del módulo ``pironman5``, podrá acceder al :ref:`promax_view_control_dashboard`.

Si no necesita esta función y desea reducir el uso de CPU y RAM, puede deshabilitar el panel durante la instalación de ``pironman5`` agregando la bandera ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si ya ha instalado ``pironman5``, puede eliminar el módulo ``dashboard`` e ``influxdb``, luego reiniciar pironman5 para aplicar los cambios:

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. ¿Cómo controlar los componentes usando el comando ``pironman5``?
------------------------------------------------------------------------

Puede consultar el siguiente tutorial para controlar los componentes del Pironman 5 MAX usando el comando ``pironman5``.

* :ref:`promax_view_control_commands`

13. ¿Cómo cambiar el orden de arranque de la Raspberry Pi usando comandos?
----------------------------------------------------------------------------------------

Si ya ha iniciado sesión en su Raspberry Pi, puede cambiar el orden de arranque usando comandos. Las instrucciones detalladas son las siguientes:

* :ref:`configure_boot_ssd_promax`

14. ¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
-------------------------------------------------------------------

Además de modificar el ``BOOT_ORDER`` en la configuración EEPROM, también puede usar **Raspberry Pi Imager** para cambiar el orden de arranque de su Raspberry Pi.

Se recomienda usar una tarjeta de repuesto para este paso.

* :ref:`update_bootloader_promax`

15. ¿Cómo copiar el sistema de la tarjeta SD a un SSD NVMe?
--------------------------------------------------------------

Si tiene un SSD NVMe pero no tiene un adaptador para conectar su NVMe a su computadora, puede instalar primero el sistema en su tarjeta Micro SD. Una vez que el Pironman 5 MAX arranque correctamente, puede copiar el sistema de su tarjeta Micro SD a su SSD NVMe. Las instrucciones detalladas son las siguientes:

* :ref:`copy_sd_to_nvme_promax`

16. ¿Cómo quitar la película protectora de las placas acrílicas?
--------------------------------------------------------------------

Se incluyen dos paneles acrílicos en el paquete, ambos cubiertos con una película protectora amarilla/transparente en ambos lados para prevenir rayones. La película protectora puede ser un poco difícil de quitar. Use un destornillador para raspar suavemente las esquinas, luego retire con cuidado toda la película.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _promax_openssh_powershell:

17. ¿Cómo instalar OpenSSH a través de Powershell?
-------------------------------------------------------

Cuando usa ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) para conectarse a su Raspberry Pi, pero aparece el siguiente mensaje de error.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Significa que su sistema informático es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado, necesita seguir el tutorial a continuación para instalarlo manualmente.

#. Escriba ``powershell`` en el cuadro de búsqueda de su escritorio Windows, haga clic derecho en ``Windows PowerShell`` y seleccione ``Run as administrator`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Use el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se devolverá la siguiente salida.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifique la instalación usando el siguiente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora le indica que ``OpenSSH.Client`` se ha instalado correctamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Si el mensaje anterior no aparece, significa que su sistema Windows sigue siendo demasiado antiguo, y se recomienda instalar una herramienta SSH de terceros, como |link_putty|.

#. Ahora reinicie PowerShell y continúe ejecutándolo como administrador. En este punto podrá iniciar sesión en su Raspberry Pi usando el comando ``ssh``, donde se le pedirá que ingrese la contraseña que configuró anteriormente.

   .. image:: img/powershell_login.png

18. Si configuro OMV, ¿puedo seguir usando las funciones del Pironman5?
--------------------------------------------------------------------------------------------------------

Sí, OpenMediaVault se configura en el sistema Raspberry Pi. Siga los pasos de :ref:`promax_set_up_pi_os` para continuar con la configuración.

19. ¿La cámara de la Raspberry Pi no funciona?
------------------------------------------------------------

Cuando la cámara no funciona, el 90% de los problemas están relacionados con la conexión del cable plano o con el hardware de la cámara.

Primero, use ``rpicam-hello --list-cameras`` para confirmar si la cámara es detectada. Si se detecta correctamente, debería ver un mensaje similar al siguiente:

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Si la cámara no es detectada, verifique si el cable plano está invertido o no está completamente insertado. Si el problema persiste, intente reemplazar el cable plano o el módulo de la cámara para hacer una prueba cruzada.