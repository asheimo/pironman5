.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_batocera:

Configuración en Batocera.linux
=========================================================

Si ha instalado el sistema operativo Batocera.linux, puede iniciar sesión de forma remota en este sistema a través de SSH y luego seguir los pasos a continuación para completar la configuración.

#. Una vez que el sistema arranque, use ssh para conectarse de forma remota a Pironman5. Para Windows, puede abrir **Powershell**, y para Mac OS X y Linux, puede abrir directamente **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%

#. El nombre de host predeterminado para el sistema batocera es ``batocera``, con el nombre de usuario predeterminado ``root`` y la contraseña ``linux``. Por lo tanto, puede iniciar sesión escribiendo ``ssh root@batocera.local`` e ingresando la contraseña ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Ejecute el comando: ``/etc/init.d/S92switch setup`` para ingresar a la página de configuración del menú.

   .. image:: img/batocera_configure.png
      :width: 90%

#. Use la tecla de flecha hacia abajo para navegar hasta el final, seleccione y active los servicios de **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Después de activar el servicio pironman5, seleccione **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Ejecute el comando ``reboot`` para reiniciar Pironman5.

   .. code-block:: shell

      reboot

#. Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Aquí están las configuraciones principales para Pironman 5 Pro MAX:

   * La pantalla OLED muestra CPU, RAM, uso de disco, temperatura de la CPU y la dirección IP de la Raspberry Pi.
   * Cuatro LEDs RGB WS2812 se iluminarán en azul con un modo de respiración.

Ahora, puede conectar el Pironman 5 Pro MAX a una pantalla, controladores de juegos, auriculares y más para sumergirse en su mundo de juegos.

.. note::

   En este punto, ha configurado exitosamente el Pironman 5 Pro MAX y está listo para usar.

   Para el control avanzado de sus componentes, consulte :ref:`control_commands_dashboard_promax`.