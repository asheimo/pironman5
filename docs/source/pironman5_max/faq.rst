.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Soluciona problemas técnicos y postventa con el apoyo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a lanzamientos de productos y adelantos especiales.
    - **Descuentos exclusivos**: Aprovecha promociones especiales en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y eventos promocionales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


FAQ
============

1. Acerca de los sistemas compatibles
------------------------------------------------

Sistemas que han pasado la prueba en la Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Acerca del botón de encendido
-----------------------------------------

El botón de encendido expone el botón de encendido de la Raspberry Pi 5 y funciona exactamente igual que el botón de encendido de la Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Apagar**

  * Si utilizas el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces rápidamente el botón de encendido para apagarlo.
  * Si utilizas el sistema **Raspberry Pi OS Lite** sin escritorio, presiona una vez el botón de encendido para iniciar el apagado.
  * Para forzar un apagado, mantén presionado el botón de encendido.

* **Encender**

  * Si la placa de Raspberry Pi está apagada pero aún conectada a la corriente, presione el botón una vez para encenderla desde el estado de apagado.

* Si utiliza un sistema que no admite el botón de apagado, puede mantenerlo presionado durante 5 segundos para forzar un apagado, y luego presionarlo una vez para volver a encender.

3. Acerca del Raspberry Pi AI HAT+
----------------------------------------------------------

El Raspberry Pi AI HAT+ no es compatible con el Pironman 5.

   .. image::  img/output3.png
        :width: 400

El Raspberry Pi AI Kit combina el Raspberry Pi M.2 HAT+ con el módulo acelerador Hailo AI.

   .. image::  img/output2.jpg
        :width: 400

Puede quitar el módulo acelerador Hailo AI del Raspberry Pi AI Kit e insertarlo directamente en el módulo NVMe PIP del Pironman 5 MAX.

   .. .. image::  img/output4.png
   ..      :width: 800

4. Acerca de los extremos de los tubos de cobre del disipador tipo torre
---------------------------------------------------------------------------------

Los tubos en forma de U en la parte superior del disipador tipo torre están comprimidos para permitir que los tubos de cobre pasen a través de las aletas de aluminio. Esto es parte del proceso de producción normal de los tubos de cobre.

   .. image::  img/tower_cooler1.png

5. ¿El PI5 no arranca (LED rojo)?
-------------------------------------------

Este problema puede deberse a una actualización del sistema, cambios en el orden de arranque o un cargador de arranque dañado. Puede intentar los siguientes pasos para resolver el problema:

#. Verificar la conexión del adaptador USB-HDMI

   * Verifique cuidadosamente que el adaptador USB-HDMI esté correctamente conectado al PI5.
   * Intente desconectar y volver a conectar el adaptador USB-HDMI.
   * Luego, vuelva a conectar la fuente de alimentación y compruebe si el PI5 arranca correctamente.

#. Probar el PI5 fuera de la carcasa

   * Si volver a conectar el adaptador no soluciona el problema:
   * Retire el PI5 de la carcasa del Pironman 5.
   * Alimente el PI5 directamente con el adaptador de corriente (sin la carcasa).
   * Verifique si puede arrancar normalmente.

#. Restaurar el cargador de arranque

   * Si el PI5 aún no arranca, es posible que el cargador de arranque esté dañado. Puede seguir esta guía: :ref:`update_bootloader_max` y elegir si desea arrancar desde la tarjeta SD o NVMe/USB.
   * Inserte la tarjeta SD preparada en el PI5, enciéndalo y espere al menos 10 segundos. Una vez completada la recuperación, retire y reformatee la tarjeta SD.
   * Luego, use Raspberry Pi Imager para grabar la versión más reciente del sistema operativo Raspberry Pi OS, inserte nuevamente la tarjeta y pruebe iniciar de nuevo.

6. ¿La pantalla OLED no funciona?
-----------------------------------------

Si la pantalla OLED no muestra nada o muestra información incorrecta, siga estos pasos para la solución de problemas:

1. **Verifique la conexión de la pantalla OLED**

   Asegúrese de que el cable FPC de la pantalla OLED esté correctamente conectado.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               Su navegador no admite la etiqueta de video.
           </video>
       </div>

2. **Verifique la compatibilidad del sistema operativo**

   Asegúrese de que está utilizando un sistema operativo compatible en su Raspberry Pi.

3. **Verifique la dirección I2C**

   Ejecute el siguiente comando para verificar si se detecta la dirección I2C (0x3C) del OLED:

   .. code-block:: shell

      sudo i2cdetect -y 1

   Si no se detecta la dirección, active I2C con el siguiente comando:

   .. code-block:: shell

      sudo raspi-config

4. **Reinicie el servicio pironman5**

   Reinicie el servicio `pironman5` para verificar si el problema se resuelve:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Verifique el archivo de registro**

   Si el problema persiste, revise el archivo de registro para detectar mensajes de error y envíe la información al soporte técnico para un análisis más detallado:

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log

7. ¿El módulo NVMe PIP no funciona?
---------------------------------------

1. Asegúrese de que el cable FPC que conecta el módulo NVMe PIP con la Raspberry Pi 5 esté correctamente conectado.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Su navegador no admite la etiqueta de video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Su navegador no admite la etiqueta de video.
           </video>
       </div>

2. Confirme que su SSD esté correctamente instalada en el módulo NVMe PIP.  

3. Verifique el estado de los LED del módulo NVMe PIP:

   Después de confirmar todas las conexiones, encienda el Pironman 5 MAX y observe los dos indicadores del módulo NVMe PIP:  

   * **PWR-LED**: Debe encenderse.  
   * **STA-LED**: Debe parpadear para indicar el funcionamiento normal.  

   .. image:: img/dual_nvme_pip_leds.png  

   * Si el **PWR-LED** está encendido pero el **STA-LED** no parpadea, significa que el SSD NVMe no es reconocido por la Raspberry Pi.  
   * Si el **PWR-LED** está apagado, puente los pines "Force Enable" del módulo. Si el **PWR-LED** se enciende, podría deberse a un cable FPC suelto o una configuración del sistema no compatible con NVMe.

   .. image:: img/dual_nvme_pip_j4.png  

4. Asegúrese de que en su SSD NVMe haya un sistema operativo correctamente instalado. Consulte: :ref:`install_the_os_max`.

5. Si el cableado es correcto y el sistema operativo está instalado, pero el SSD NVMe aún no arranca, intente iniciar desde una tarjeta microSD para verificar la funcionalidad de los demás componentes. Una vez confirmado, continúe con: :ref:`configure_boot_ssd_max`.

Si el problema persiste después de los pasos anteriores, envíe un correo electrónico a service@sunfounder.com. Le responderemos lo antes posible.

8. ¿Los LED RGB no funcionan?
--------------------------------------

#. Los dos pines del expansor IO situados encima de J9 se utilizan para conectar los LED RGB al GPIO10. Asegúrese de que el jumper esté correctamente colocado sobre estos dos pines.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifique que la Raspberry Pi ejecute un sistema operativo compatible. El Pironman 5 solo admite las siguientes versiones del sistema operativo:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si ha instalado un sistema operativo no compatible, siga la guía para instalar uno compatible: :ref:`install_the_os_max`.

#. Ejecute el comando ``sudo raspi-config`` para abrir el menú de configuración. Navegue a **3 Interfacing Options** -> **I3 SPI** -> **YES**, luego haga clic en **OK** y **Finish** para habilitar SPI. Después de activar SPI, reinicie el Pironman 5.

Si el problema persiste después de estos pasos, envíe un correo electrónico a service@sunfounder.com. Le responderemos lo antes posible.

9. ¿El ventilador de la CPU no funciona?
----------------------------------------------

Si la temperatura de la CPU no ha alcanzado el umbral establecido, el ventilador de la CPU no se activará.

**Control de velocidad del ventilador según la temperatura**  

El ventilador PWM funciona de manera dinámica y ajusta su velocidad de rotación según la temperatura de la Raspberry Pi 5:  

* **Por debajo de 50°C**: El ventilador permanece apagado (0%).  
* **A 50°C**: El ventilador gira a baja velocidad (30%).  
* **A 60°C**: El ventilador aumenta a velocidad media (50%).  
* **A 67,5°C**: El ventilador sube a alta velocidad (70%).  
* **A 75°C o más**: El ventilador funciona a velocidad máxima (100%).  

Para más detalles, consulte : :ref:`fan_max`

10. ¿Cómo activar la pantalla OLED?
---------------------------------------------------------------------------------

Para ahorrar energía y prolongar la vida útil de la pantalla, la pantalla OLED se apaga automáticamente tras un período de inactividad. Esto es parte del diseño normal y no afecta la funcionalidad del producto.

Puedes presionar el botón para activar la pantalla.

.. note::

   Para la configuración de la pantalla OLED (por ejemplo, encendido/apagado, tiempo de suspensión, rotación, etc.), consulte: :ref:`max_view_control_dashboard` o :ref:`max_view_control_commands`.


11. ¿Cómo desactivar el panel web (dashboard)?
------------------------------------------------------

Una vez que haya completado la instalación del módulo ``pironman5``, podrá acceder al :ref:`max_view_control_dashboard`.
      
Si no necesita esta función y desea reducir el uso de CPU y RAM, puede desactivar el panel durante la instalación de ``pironman5`` agregando la opción ``--disable-dashboard``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Si ya ha instalado ``pironman5``, puede eliminar el módulo ``dashboard`` y ``influxdb``, luego reiniciar pironman5 para aplicar los cambios:
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. ¿El Pironman 5 MAX es compatible con sistemas de retro gaming?
.. ------------------------------------------------------
.. Sí, es compatible. Sin embargo, la mayoría de los sistemas de retro gaming son versiones simplificadas que no pueden instalar ni ejecutar software adicional. Esta limitación puede hacer que algunos componentes del Pironman 5 MAX, como la pantalla OLED, los dos ventiladores RGB y los 4 LED RGB, no funcionen correctamente, ya que estos componentes requieren la instalación de los paquetes de software del Pironman 5 MAX.

.. .. note::

..     El sistema Batocera.linux ahora es totalmente compatible con Pironman 5 MAX. Batocera.linux es una distribución de juegos retro de código abierto y completamente gratuita.

..     * :ref:`max_install_batocera`
..     * :ref:`max_set_up_batocera`

12. ¿Cómo controlar los componentes usando el comando ``pironman5``?
----------------------------------------------------------------------

Puede consultar el siguiente tutorial para controlar los componentes del Pironman 5 MAX usando el comando ``pironman5``.

* :ref:`max_view_control_commands`

13. ¿Cómo cambiar el orden de arranque de la Raspberry Pi usando comandos?
-----------------------------------------------------------------------------

Si ya ha iniciado sesión en su Raspberry Pi, puede cambiar el orden de arranque mediante comandos. Las instrucciones detalladas son las siguientes:

* :ref:`configure_boot_ssd_max`

14. ¿Cómo modificar el orden de arranque con Raspberry Pi Imager?
--------------------------------------------------------------------------

Además de modificar el ``BOOT_ORDER`` en la configuración del EEPROM, también puede usar **Raspberry Pi Imager** para cambiar el orden de arranque de su Raspberry Pi.

Se recomienda usar una tarjeta de repuesto para este paso.

* :ref:`update_bootloader_max`

15. ¿Cómo copiar el sistema desde la tarjeta SD a un SSD NVMe?
------------------------------------------------------------------------

Si tiene un SSD NVMe pero no un adaptador para conectarlo a su computadora, primero puede instalar el sistema en su tarjeta Micro SD. Una vez que el Pironman 5 MAX haya arrancado correctamente, puede copiar el sistema desde su Micro SD al SSD NVMe. Las instrucciones detalladas son las siguientes:

* :ref:`copy_sd_to_nvme_max`

16. ¿Cómo quitar la película protectora de las placas acrílicas?
-----------------------------------------------------------------

El paquete incluye dos paneles acrílicos, ambos cubiertos con una película protectora amarilla o transparente en ambos lados para evitar arañazos. La película puede ser un poco difícil de quitar. Use un destornillador para raspar suavemente las esquinas y luego retire con cuidado toda la película.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _max_openssh_powershell:

17. ¿Cómo instalar OpenSSH mediante PowerShell?
--------------------------------------------------

Cuando utilice ``ssh <nombre_de_usuario>@<nombre_de_host>.local`` (o ``ssh <nombre_de_usuario>@<dirección_IP>``) para conectarse a su Raspberry Pi, pero aparezca el siguiente mensaje de error:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Significa que su sistema operativo es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Debe seguir el siguiente tutorial para instalarlo manualmente.

#. Escriba ``powershell`` en el cuadro de búsqueda del escritorio de Windows, haga clic derecho sobre ``Windows PowerShell`` y seleccione ``Ejecutar como administrador`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%
      
#. Use el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se mostrará la siguiente salida.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifique la instalación usando el siguiente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora verá que ``OpenSSH.Client`` se ha instalado correctamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        Si no aparece el mensaje anterior, significa que su sistema Windows sigue siendo demasiado antiguo y se recomienda instalar una herramienta SSH de terceros, como |link_putty|.

#. Ahora reinicie PowerShell y ejecútelo nuevamente como administrador. En este punto, podrá iniciar sesión en su Raspberry Pi utilizando el comando ``ssh``, donde se le pedirá que introduzca la contraseña que configuró anteriormente.

   .. image:: img/powershell_login.png


18. Si configuro OMV, ¿aún puedo usar las funciones del Pironman5?
--------------------------------------------------------------------------------------------------------

Sí, OpenMediaVault se instala sobre el sistema Raspberry Pi. Por favor, siga los pasos de :ref:`max_set_up_pi_os` para continuar con la configuración.


19. ¿Puedo usar la función de interruptor por vibración del Pironman5 Max?
--------------------------------------------------------------------------------------------------------

La función de interruptor por vibración del Pironman5 Max ya no es compatible a nivel de software a partir de la versión 1.3.6. Este cambio se debe a la evolución de las versiones, no a un fallo de hardware. Si depende de esta función, puede considerar volver a una versión anterior, modificar el código manualmente o enviar una solicitud al soporte oficial. La duración de visualización de la pantalla OLED aún se puede ajustar mediante la línea de comandos. La pantalla OLED se activa presionando el botón una vez y permanece encendida durante unos segundos.