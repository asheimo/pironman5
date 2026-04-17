.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_view_control_dashboard:

Ver y Controlar desde el Panel
=========================================

Una vez que haya instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar.

Ahora puede abrir la página de monitoreo en su navegador para ver la información de su Raspberry Pi, configurar los RGB, etc. El enlace de la página es: ``http://<ip>:34001``.

.. image:: img/dashboard_prm5promax.png
  :width: 90%

Esta página tiene las secciones **Dashboard**, **History**, **Log** y **Settings**.

.. image:: img/dashboard_tab.png
  :width: 90%

Dashboard
-----------------------

Hay múltiples tarjetas para ver el estado relevante de la Raspberry Pi, incluyendo:

* **Temperature**: Vea la temperatura de la CPU y GPU de la Raspberry Pi.

  .. image:: img/dashboard_temp.png
    :align: center

* **Storage**: Muestra la capacidad de almacenamiento de la Raspberry Pi, mostrando varias particiones de disco con su espacio usado y disponible.

  .. image:: img/dashboard_storage.png
    :align: center

* **Memory**: Muestra el uso y porcentaje de RAM de la Raspberry Pi.

  .. image:: img/dashboard_memory.png
    :align: center

* **Network**: Muestra el tipo de conexión de red actual, velocidades de subida y bajada.

  .. image:: img/dashboard_network.png
    :align: center

* **Processor**: Ilustra el rendimiento de la CPU de la Raspberry Pi, incluyendo el estado de sus cuatro núcleos, frecuencias de operación y porcentaje de uso de la CPU.

  .. image:: img/dashboard_processor.png
    :align: center

History
--------------

La página History le permite ver datos históricos. Marque los datos que desea ver en la barra lateral izquierda, luego seleccione el rango de tiempo para ver los datos de ese período, y también puede hacer clic para descargarlos.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

La página Log se utiliza para ver los registros del servicio Pironman5 actualmente en ejecución. El servicio Pironman5 incluye múltiples subservicios, cada uno con su propio registro. Seleccione el registro que desea ver y podrá ver los datos del registro a la derecha. Si está en blanco, puede significar que no hay contenido de registro.

* Cada registro tiene un tamaño fijo de 10MB. Cuando supera este tamaño, se creará un segundo registro.
* El número de registros para el mismo servicio está limitado a 10. Si el número supera este límite, el registro más antiguo se eliminará automáticamente.
* Hay herramientas de filtro encima del área de registro a la derecha. Puede seleccionar el nivel de registro, filtrar por palabras clave y usar varias herramientas convenientes, incluyendo **Line Wrap**, **Auto Scroll** y **Auto Update**.
* Los registros también se pueden descargar localmente.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%

Settings
-----------------

Hay un menú de configuración en la **esquina superior derecha** de la página donde puede personalizar los ajustes según sus preferencias. Después de hacer modificaciones, los cambios se guardarán automáticamente. Si es necesario, puede hacer clic en el botón CLEAR en la parte inferior para borrar los datos históricos.

.. image:: img/dashboard_setting_darkmode.png
  :width: 600

* **Dark Mode**: Cambie entre temas de modo claro y oscuro. La opción de tema se guarda en la caché del navegador. Cambiar de navegador o borrar la caché volverá al tema claro predeterminado.
* **Show Unmounted Disk**: Si mostrar o no discos no montados en el panel.
* **Show All Cores**: Si mostrar o no todos los núcleos en el panel.
* **Card layout**: Establezca la disposición de las tarjetas del panel.
* **Temperature Unit**: Establezca la unidad de temperatura mostrada por el sistema.

**Acerca de la Pantalla OLED**

.. image:: img/dashboard_setting_oled.png
  :width: 600

* **OLED Enable**: Si habilitar o no el OLED.
* **OLED Rotation**: Establezca la rotación del OLED.
* **OLED Sleep Timeout**: Establezca el tiempo de reposo del OLED.

* **OLED Page**: Establezca la página del OLED a mostrar: **System Mix**, **Performance Metrics**, **Disk Usage**, **IP Addresses**.

**Acerca de los LEDs RGB**

.. image:: img/dashboard_setting_rgb.png
  :width: 600

* **RGB Enable**: Si habilitar o no los LEDs RGB.
* **RGB Color**: Establezca el color de los LEDs RGB.
* **RGB Brightness**: Puede ajustar el brillo de los LEDs RGB con un control deslizante.
* **RGB Style**: Elija el modo de visualización de los LEDs RGB. Las opciones incluyen **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** y **Hue Cycle**.
* **RGB Speed**: Establezca la velocidad de cambio de los LEDs RGB.
* **RGB Led**: Establezca el número de LEDs RGB a controlar.

**Acerca de los Datos**

.. image:: img/dashboard_setting_debug.png
  :width: 600

* **Debug Level**: Establezca el nivel de depuración. Las opciones incluyen **Info**, **Warning**, **Error** y **Critical**.
* **History Retention**: Establezca el número de días para retener datos históricos.
* **Clear All Data**: Borre todos los datos históricos.
* **Reboot**: Reinicie el sistema.
* **Shutdown**: Apague el sistema.
* **Restart service**: Reinicie los servicios del sistema.

**Ventilador**

Este ventilador se conecta a un puerto dedicado de ventilador PWM de 4 pines en la Raspberry Pi 5. Su estrategia de control predeterminada es un esquema de ajuste de velocidad inteligente de múltiples niveles gestionado por firmware, basado en la temperatura de la CPU. Esto significa que cuando usa un ventilador PWM oficial o compatible y lo conecta correctamente, el sistema ajustará automáticamente la velocidad del ventilador según los cambios en la temperatura de la CPU (comenzando a operar por encima de los 50°C) sin ninguna intervención manual de su parte.