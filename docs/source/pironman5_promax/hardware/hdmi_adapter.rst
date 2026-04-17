.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Adaptador USB HDMI
==========================================

.. image:: img/hdmi_adapter.png

Esta placa adaptadora USB HDMI está diseñada específicamente para la Raspberry Pi 5. Su función principal es reposicionar las conexiones USB y HDMI para alinearlas con el lado de la interfaz USB de la Raspberry Pi, mejorando la accesibilidad y la gestión de cables.

Adicionalmente, el puerto HDMI se convierte a una interfaz HDMI Tipo A estándar, ofreciendo una compatibilidad más amplia.

**Alimentación Adicional para NVMe**

La placa cuenta con un cabezal de alimentación de 5V específicamente para la alimentación del PIP NVMe. Junto con un cabezal de extensión, se puede conectar a la interfaz de alimentación adicional del NVMe para proporcionar energía extra.

**Soporte para Batería 1220RTC**

Se incorpora un soporte para batería 1220RTC para la instalación conveniente de una batería RTC. Se conecta a la interfaz RTC de la Raspberry Pi mediante un cable inverso SH1.0 2P.

El soporte para batería es compatible tanto con baterías CR1220 como ML1220. Si se usa una ML1220 (batería de dióxido de manganeso y litio), la carga se puede configurar directamente en la Raspberry Pi. Tenga en cuenta que la CR1220 no es recargable.

**Habilitar la Carga por Goteo**

.. warning::

  Si está usando una batería CR1220, no habilite la carga por goteo, ya que puede causar daños irreparables a la batería y riesgo de dañar la placa.

Por defecto, la función de carga por goteo para la batería está deshabilitada. Los archivos ``sysfs`` indican el voltaje de carga por goteo actual y los límites:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Para habilitar la carga por goteo, agregue ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``:

  * Abra el archivo ``/boot/firmware/config.txt``.

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt

  * Agregue ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``.

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

Después de reiniciar, el sistema mostrará:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Esto confirma que la batería está ahora en carga por goteo. Para deshabilitar esta función, simplemente elimine la línea ``dtparam`` de ``config.txt``.

**Interfaz de Audio**
---------------------------------

Esta sección cubre las características de salida de audio de la placa, incluyendo la salida de altavoces y el conector para auriculares.

.. image:: img/hdmi_speaker_port.png

**Puerto de Altavoces**

La placa cuenta con una interfaz de salida de altavoces de dos canales que soporta dos altavoces de 4Ω 3W.

**Interruptor de Altavoces**

La señal de audio de los altavoces se origina en la fuente HDMI0. Si HDMI0 está conectado a una pantalla con altavoces integrados, tanto los altavoces del Pironman 5 Pro Max como los de la pantalla pueden reproducir audio simultáneamente. El puente **SPEAKER** le permite controlar este comportamiento.

*   Conecte el puente a los dos pines izquierdos (**ON**) para mantener los altavoces **siempre habilitados**.
*   Conecte el puente a los dos pines derechos (**AUTO**) para que los altavoces se **deshabiliten automáticamente** cuando se inserten auriculares o cuando HDMI0 esté conectado.

Por lo tanto, si desea usar los altavoces integrados mientras hay una pantalla HDMI conectada, puede:

*   Conectar la pantalla al puerto **HDMI1** en su lugar.
*   Colocar el puente **SPEAKER** en la posición **ON**.

**Conector de Audio de 3.5mm**

El conector para auriculares comparte la misma fuente de audio que los altavoces pero lleva una señal **no amplificada**. Utiliza un conector conmutado que **deshabilita automáticamente el amplificador de los altavoces** cuando se insertan auriculares, evitando que ambos reproduzcan sonido simultáneamente.

El conector es un conector TRRS de 4 pines pero solo soporta **salida de audio estéreo estándar**:

*   **Punta (T):** Canal Izquierdo
*   **Anillo 1 (R1):** Canal Derecho
*   **Anillo 2 (R2):** Tierra
*   **Cubierta (S):** Tierra

Esta configuración mantiene la compatibilidad con la mayoría de los estándares comunes de auriculares de 4 pines.