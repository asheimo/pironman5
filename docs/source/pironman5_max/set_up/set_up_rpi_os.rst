.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Soluciona problemas técnicos y postventa con el apoyo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a lanzamientos de productos y adelantos especiales.
    - **Descuentos exclusivos**: Aprovecha promociones especiales en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y eventos promocionales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_set_up_pi_os:

Configuración en Raspberry Pi/Ubuntu/Kali/Homebridge OS
===================================================================

.. image:: ../img/pironman5_max.jpg
    :width: 400
    :align: center
    


Si has instalado Raspberry Pi OS, Ubuntu, Kali Linux o Homebridge en tu Raspberry Pi, deberás configurar el Pironman 5 MAX utilizando la línea de comandos. A continuación puedes encontrar tutoriales detallados.

.. note::

  Antes de proceder con la configuración, debes iniciar y acceder a tu Raspberry Pi.  
  Si no estás seguro de cómo iniciar sesión, puedes visitar el sitio oficial de Raspberry Pi: |link_rpi_get_start|.

.. include:: /pironman5_max/important_notice.rst
   :start-after: start_max_important_notice
   :end-before: end_max_important_notice

2. Configuración del apagado para desactivar la alimentación GPIO
-------------------------------------------------------------------------------

Para evitar que la pantalla OLED y los ventiladores RGB, alimentados por el GPIO de la Raspberry Pi, permanezcan activos después del apagado, es fundamental configurar la Raspberry Pi para desactivar la alimentación GPIO.

#. Abre la herramienta de configuración EEPROM:

   .. code-block::

      sudo raspi-config

#. Ve a **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Selecciona **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Guarda los cambios. Se te pedirá reiniciar para que la nueva configuración surta efecto.


.. _max_download_pironman5_module:

3. Descarga e instalación del módulo ``pironman5``
-----------------------------------------------------------

.. note::

   Para los sistemas “lite”, instala primero herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procede a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Después de una instalación exitosa, es necesario reiniciar el sistema para activar la instalación. Sigue las indicaciones en pantalla para reiniciar.

   Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente.  
   Estas son las configuraciones principales del Pironman 5 MAX:
   
   * La pantalla OLED muestra CPU, RAM, uso de disco, temperatura de la CPU y dirección IP de la Raspberry Pi.
   * Cuatro LED WS2812 RGB se iluminarán de color azul con un efecto de respiración.  
   * Los ventiladores RGB están configurados por defecto en **Always On**. Para obtener información sobre cómo configurar las temperaturas de activación, consulta :ref:`cc_control_fan_max`.

#. Puedes usar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` del servicio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa este comando para aplicar cualquier cambio en la configuración del Pironman 5 MAX.  
   * ``start/stop``: Habilita o deshabilita el servicio ``pironman5.service``.  
   * ``status``: Verifica el estado operativo del programa ``pironman5`` utilizando la herramienta ``systemctl``.

.. note::

   En este punto, has configurado correctamente el Pironman 5 MAX y está listo para su uso.  
   Para el control avanzado de sus componentes, consulta :ref:`control_commands_dashboard_max`.
