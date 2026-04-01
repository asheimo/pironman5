.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con el apoyo de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para perfeccionar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y vistas previas especiales.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante celebraciones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_set_up_pironman5:

4. Configuración o instalación del software
================================================

Una vez que el sistema se haya escrito en la tarjeta Micro SD o en el SSD NVMe, insértalo en la ranura correspondiente del Pironman 5 MAX. Luego presiona el botón de encendido para iniciar el dispositivo.

Al encenderlo, verás que se iluminan los diferentes indicadores LED de alimentación. Sin embargo, la pantalla OLED, los LEDs RGB y los ventiladores RGB (los dos ventiladores laterales) aún no estarán operativos, ya que requieren configuración. Si notas algún error visual en la pantalla, puedes ignorarlo por ahora; se resolverá tras la configuración.

Antes de configurar, necesitas iniciar sesión en tu Raspberry Pi. Si no sabes cómo hacerlo, visita el sitio oficial de Raspberry Pi: |link_rpi_get_start|.

Después, puedes seguir el tutorial de configuración correspondiente a tu sistema operativo:


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel

.. set_up_batocera


**Acerca del botón de encendido**

El botón de encendido replica la funcionalidad del botón de encendido nativo de la Raspberry Pi 5 y funciona del mismo modo.

* **Apagar**

  * Si utilizas el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces rápidamente el botón de encendido para apagarlo.
  * Si utilizas el sistema **Raspberry Pi OS Lite** sin escritorio, presiona una vez el botón de encendido para iniciar el apagado.
  * Para forzar un apagado, mantén presionado el botón de encendido.

* **Encender**

  * Si la Raspberry Pi está apagada pero aún recibe energía, una sola pulsación encenderá el dispositivo desde el estado de apagado.

* Si estás usando un sistema que no admite el botón de apagado, puedes mantenerlo presionado durante 5 segundos para forzar el apagado, y presionarlo una vez para encenderlo desde el estado de apagado.



