.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _set_up_umbrel_promax:

Configuración en Umbrel OS
======================================================================

Si ha instalado Umbrel OS en su Raspberry Pi 5, necesitará configurar el Pironman 5 Pro MAX usando la línea de comandos. Las instrucciones detalladas se proporcionan a continuación:

#. Conecte su Raspberry Pi 5 a su red usando un cable Ethernet. Este paso es esencial para asegurar que su Raspberry Pi tenga acceso a internet.

#. En su navegador, visite: ``http://umbrel.local``. Si la página no se abre, verifique en su router la dirección IP del dispositivo Umbrel, por ejemplo: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Cree su cuenta de Umbrel estableciendo un nombre de usuario y una contraseña. Esta contraseña se usará para el acceso remoto futuro a Umbrel, así que asegúrese de recordarla.

   .. image:: img/umbrel_account.png

#. Haga clic en **Next** para completar la configuración de Umbrel y entrar al entorno de escritorio.

   .. image:: img/umbrel_desktop.png

#. Abra la Terminal. Desde el escritorio, haga clic en el icono **Settings**, luego seleccione **Advanced Settings** y haga clic en **Open**.

   .. image:: img/umbrel_setting.png

#. Haga clic en **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Puede elegir abrir la Terminal en Umbrel OS o dentro de una aplicación específica. Cualquiera de las opciones lo llevará a la interfaz de la Terminal.

   .. image:: img/umbrel_terminal.png

#. Proceda a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Después de que la instalación esté completa, ingrese el siguiente comando para reiniciar su Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente. Aquí están las configuraciones principales para Pironman 5 Pro MAX:

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