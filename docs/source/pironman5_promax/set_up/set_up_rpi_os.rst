.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pi_os:

Configuración en Raspberry Pi/Ubuntu/Kali/Homebridge OS
==========================================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Si ha instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en su Raspberry Pi, necesitará configurar el Pironman 5 Pro MAX usando la línea de comandos. Los tutoriales detallados se pueden encontrar a continuación:

.. note::

  Antes de configurar, necesita arrancar e iniciar sesión en su Raspberry Pi. Si no está seguro de cómo iniciar sesión, puede visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

Configuración del Apagado para Desactivar la Alimentación GPIO
--------------------------------------------------------------------------------

Para evitar que la pantalla OLED y los ventiladores RGB, alimentados por el GPIO de la Raspberry Pi, permanezcan activos después del apagado, es esencial configurar la Raspberry Pi para la desactivación de la alimentación GPIO.

#. Abra la herramienta de configuración EEPROM:

   .. code-block::

      sudo raspi-config

#. Navegue a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Seleccione **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Guarde los cambios. Se le pedirá que reinicie para que los nuevos ajustes tomen efecto.

.. _promax_download_pironman5_module:

Descarga e Instalación del Módulo ``pironman5``
-----------------------------------------------------------

.. note::

   Para sistemas lite, instale inicialmente herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

   .. code-block:: shell

      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Proceda a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Después de una instalación exitosa, se requiere un reinicio del sistema para activar la instalación. Siga el mensaje de reinicio en pantalla.

   Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Aquí están las configuraciones principales para Pironman 5 Pro MAX:

   * La pantalla OLED muestra CPU, RAM, uso de disco, temperatura de la CPU y la dirección IP de la Raspberry Pi.
   * Cuatro LEDs RGB WS2812 se iluminarán en azul con un modo de respiración.

#. Puede usar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` de ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Use este comando para aplicar cualquier cambio realizado en la configuración de Pironman 5 Pro MAX.
   * ``start/stop``: Habilite o deshabilite el ``pironman5.service``.
   * ``status``: Verifique el estado operativo del programa ``pironman5`` usando la herramienta ``systemctl``.

.. note::

   En este punto, ha configurado exitosamente el Pironman 5 Pro MAX y está listo para usar.

   Para el control avanzado de sus componentes, consulte :ref:`control_commands_dashboard_promax`.