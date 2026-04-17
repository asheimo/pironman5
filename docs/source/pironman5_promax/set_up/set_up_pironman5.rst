.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pironman5:

4. Configurar o Instalar el Software
================================================

Ahora que el sistema ha sido escrito en la Micro SD o en el SSD NVMe, puede insertarlos en la ranura del Pironman 5 Pro MAX. Luego presione el botón de encendido para encender el dispositivo.

Después de encender, verá los diversos LEDs de encendido iluminados, pero la pantalla OLED, los LEDs RGB y los ventiladores RGB (los dos ventiladores laterales) aún no funcionarán, ya que necesitan ser configurados. Si hay un problema de distorsión de la pantalla, ignórelo por ahora; se resolverá después de la configuración.

Antes de configurar, necesita arrancar e iniciar sesión en su Raspberry Pi. Si no está seguro de cómo iniciar sesión, puede visitar el sitio web oficial de Raspberry Pi: |link_rpi_get_start|.

Luego puede proceder a seleccionar el tutorial de configuración según su sistema.

.. toctree::
    :maxdepth: 1

    set_up_rpi_os
    set_up_umbrel

.. set_up_batocera

.. set_up_home_assistant

**Acerca del Botón de Encendido**

El botón de encendido expone el botón de encendido de la Raspberry Pi 5, y funciona igual que el botón de encendido de la Raspberry Pi 5.

* **Apagado**

    * Si ejecuta el sistema **Raspberry Pi OS Desktop**, puede presionar el botón de encendido dos veces rápidamente para apagar.
    * Si ejecuta el sistema **Raspberry Pi OS Lite**, presione el botón de encendido una sola vez para iniciar un apagado.
    * Para forzar un apagado completo, mantenga presionado el botón de encendido.

* **Encendido**

    * Si la placa Raspberry Pi está apagada, pero aún tiene alimentación, presione una vez para encender desde el estado de apagado.

* Si está ejecutando un sistema que no soporta un botón de apagado, puede mantenerlo presionado durante 5 segundos para forzar un apagado completo, y presionar una vez para encender desde el estado de apagado.