.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Dual NVMe PIP
=====================

El **Dual NVMe PIP** (Placa Periférica PCIe), según la definición de la Raspberry Pi Foundation, es un adaptador PCIe diseñado específicamente para unidades de estado sólido NVMe.

La interfaz PCIe de la Raspberry Pi 5 ofrece de forma nativa un único carril **Gen2 x1** (500 MB/s). Al integrar el chip conmutador PCIe **ASM1182e**, el Dual NVMe PIP expande esto en **dos carriles Gen2 x1 independientes**, permitiéndole conectar:

* **Dos SSD NVMe M.2**, o
* **Un SSD NVMe M.2 + un acelerador AI M.2 Hailo-8/8L**

**Notas Clave**:

* No soporta Gen3
* Soporta tamaños de SSD NVMe: **2230**, **2242**, **2260**, **2280** (todos en ranuras M.2 M-key)

.. image:: img/nvme_pip.png

* La placa se conecta mediante un cable FFC (Cable Plano Flexible) inverso de 16P 0.5mm o un cable FPC (Circuito Impreso Flexible) con impedancia adaptada.
* **STA**: Un indicador LED de estado.
* **PWR**: Un indicador LED de alimentación.
* La fuente de alimentación integrada de 3.3V puede soportar hasta 3A de salida. Sin embargo, dado que la interfaz PCIe de la Raspberry Pi está limitada a proporcionar 5V/1A de salida (equivalente a 5W), se puede suministrar alimentación adicional para uso de 3.3V/3A a través del conector J3 desde una fuente de 5V.
* **FORCE ENABLE**: La fuente de alimentación integrada se activa mediante la señal de conmutación de la interfaz PCIe. Después de que la Raspberry Pi se enciende, envía una señal para activar la fuente de alimentación de 3.3V. Si algunos sistemas no soportan la señal de conmutación o por otras razones, puede puentear J4 FORCE ENABLE soldando un cable entre las dos almohadillas flotantes para forzar que la fuente de alimentación integrada de 3.3V alimente el NVMe.

Sobre el Modelo
---------------------------

Los SSD M.2, conocidos por su tamaño compacto, vienen en varios tipos que se diferencian principalmente por su muesca (diseño de muesca en el conector) y la interfaz que utilizan. Estos son los tipos principales:

* **SSD M.2 SATA**: Utilizan la interfaz SATA, similar a los SSD SATA de 2.5 pulgadas pero en el factor de forma M.2 más pequeño. Están limitados por las velocidades máximas de SATA III de alrededor de 600 MB/s. Estos SSD son compatibles con ranuras M.2 con muesca para claves B y M.
* **SSD M.2 NVMe**: Estos SSD utilizan el protocolo NVMe sobre carriles PCIe y son significativamente más rápidos que los SSD M.2 SATA. Son adecuados para aplicaciones que requieren altas velocidades de lectura/escritura como juegos, edición de video y tareas intensivas en datos. Estos SSD típicamente requieren ranuras con clave M. Estas unidades utilizan la interfaz PCIe (Interconexión de Componentes Periféricos), con diferentes versiones como 3.0, 4.0 y 5.0. Cada nueva versión de PCIe efectivamente duplica la velocidad de transferencia de datos de su predecesora. Sin embargo, la Raspberry Pi 5 utiliza una interfaz PCIe 3.0, capaz de entregar velocidades de transferencia de hasta 3,500 MB/s.

Los SSD M.2 vienen en tres tipos de clave: B key, M key y B+M key. Sin embargo, más tarde se introdujo la clave B+M, que combina las funcionalidades de la clave B y la clave M. Como resultado, reemplazó a la clave B independiente. Consulte la imagen a continuación.

.. image:: img/ssd_key.png

En general, los SSD M.2 SATA tienen clave B+M (pueden encajar en zócalos para módulos con clave B y M), mientras que los SSD M.2 NVMe para carril PCIe 3.0 x4 tienen clave M.

.. image:: img/ssd_model2.png

Sobre la Longitud
-----------------------

Los módulos M.2 vienen en diferentes tamaños y también se pueden utilizar para Wi-Fi, WWAN, Bluetooth, GPS y NFC.

Pironman 5 MAX soporta cuatro tamaños de SSD NVMe M.2 (PCIe Gen 2.0) según sus nombres: 2230, 2242, 2260 y 2280. El "22" es el ancho en milímetros (mm), y los dos números siguientes son la longitud. Cuanto más largo es la unidad, más chips de memoria flash NAND se pueden montar; por lo tanto, mayor capacidad.

.. image:: img/m2_ssd_size.png
  :width: 600

Alimentación
-----------------------

La fuente de alimentación dual integrada de 3.3V soporta una salida máxima de 3A (10W). Ambos rieles de alimentación funcionan de forma independiente sin interferencias.

**FORCE ENABLE**
La fuente de alimentación integrada se activa mediante la señal de conmutación de la interfaz PCIe. Después de que la Raspberry Pi arranca, la señal activa la alimentación de 3.3V. Si el sistema no soporta la señal de conmutación o debido a otras razones, puentee el puente J4 FORCE EN para forzar la activación de la alimentación integrada de 3.3V para el NVMe.

**LED**
Cada interfaz tiene indicadores de estado de alimentación (PWR) e indicadores de estado (STA) independientes.

Convertidor de Interruptor de Alimentación
---------------------------------------------------------------------

**Agregar el Botón de Alimentación**

* La Raspberry Pi 5 presenta un puente **J2**, situado entre el conector de la batería RTC y el borde de la placa. Esta conexión permite agregar un botón de alimentación personalizado a la Raspberry Pi 5 conectando un interruptor momentáneo Normalmente Abierto (NO) a través de las dos almohadillas. Accionar brevemente este interruptor imita la funcionalidad del botón de alimentación integrado.

   .. image:: img/pi5_j2.jpg

* En el Pironman 5, hay un **Convertidor de Interruptor de Alimentación** que extiende el puente **J2** a un botón de alimentación externo usando dos pines Pogo.

   .. image:: img/psc.png

* Ahora, la Raspberry Pi 5 se puede encender y apagar usando el Botón de Alimentación.

**Ciclo de Alimentación**

Al encender inicialmente su Raspberry Pi 5, se encenderá automáticamente y arrancará en el sistema operativo sin necesidad de presionar el botón.

Si ejecuta el escritorio de Raspberry Pi, una pulsación breve del botón de alimentación inicia un proceso de apagado limpio. Aparecerá un menú que ofrece opciones para apagar, reiniciar o cerrar sesión. Seleccionar una opción o presionar el botón de alimentación nuevamente iniciará un apagado limpio.

.. image:: img/button_shutdown.png

**Apagado**

    * Si ejecuta el sistema **Raspberry Pi OS Desktop**, puede presionar el botón de alimentación dos veces rápidamente para apagar.
    * Si ejecuta el sistema **Raspberry Pi OS Lite** sin escritorio, presione el botón de alimentación una sola vez para iniciar un apagado.
    * Para forzar un apagado completo, mantenga presionado el botón de alimentación.

**Encendido**

    * Si la placa Raspberry Pi está apagada, pero aún tiene alimentación, presione una vez para encender desde el estado de apagado.

.. note::

    Si está ejecutando un sistema que no soporta un botón de apagado, puede mantenerlo presionado durante 5 segundos para forzar un apagado completo, y presionar una vez para encender desde el estado de apagado.