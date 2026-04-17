.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Ventiladores
================

Ventilador PWM
-----------------------------

El Pironman 5 Pro MAX tiene 3 ventiladores PWM.

El ventilador PWM del Pironman 5 Pro MAX es controlado por el sistema de la Raspberry Pi.

En cuanto a las soluciones de refrigeración para la Raspberry Pi 5, especialmente bajo cargas pesadas, el diseño del Pironman 5 Pro MAX incorpora un sistema de refrigeración inteligente. Cuenta con un ventilador PWM principal y dos ventiladores RGB adicionales. La estrategia de refrigeración está estrechamente integrada con el sistema de gestión térmica de la Raspberry Pi 5.

El funcionamiento del ventilador PWM se basa en la temperatura de la Raspberry Pi 5:

* Por debajo de 50°C, el ventilador PWM permanece apagado (0% de velocidad).
* A 50°C, el ventilador arranca a baja velocidad (30% de velocidad).
* Al alcanzar 60°C, el ventilador aumenta a velocidad media (50% de velocidad).
* A 67.5°C, el ventilador acelera a alta velocidad (70% de velocidad).
* A 75°C o más, el ventilador funciona a máxima velocidad (100% de velocidad).

Esta relación temperatura-velocidad también se aplica cuando la temperatura disminuye, con una histéresis de 5°C. La velocidad del ventilador se reduce cuando la temperatura cae 5°C por debajo de cada uno de estos umbrales.

* Comandos para monitorear el ventilador PWM. Para verificar el estado del ventilador PWM:

  .. code-block:: shell

    cat /sys/class/thermal/cooling_device0/cur_state

* Para ver la velocidad del ventilador PWM:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

En el Pironman 5 Pro MAX, el ventilador PWM es un componente crítico para mantener temperaturas operativas óptimas, particularmente durante tareas intensivas, asegurando que la Raspberry Pi 5 funcione de manera eficiente y confiable.

**Especificaciones del Ventilador**

.. image:: img/size_fan.png

* **Dimensiones externas**: 40*40*10MM
* **Potencia nominal de entrada**: 5V/0.106A
* **Velocidad nominal**: 4000RPM
* **Peso**: 13.5±5g/pieza
* **Vida útil**: 30,000 horas (temperatura ambiente 25°C)
* **Ruido acústico**: 22.31dBA
* **Flujo de aire máximo**: 2.46CFM
* **Presión de aire máxima**: 0.62mm-H2O
* **Temperatura de funcionamiento**: -10°C ~ +60°C
* **Temperatura de almacenamiento**: -20°C ~ +70°C

**Definiciones de Pines**

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Pin
     - Color
     - Descripción
   * - 1
     - Azul
     - Señal PWM para controlar la velocidad del ventilador
   * - 2
     - Rojo
     - Alimentación 5V
   * - 3
     - Negro
     - Tierra
   * - 4
     - Amarillo
     - Entrada de datos del LED RGB interno
   * - 5
     - Verde
     - Salida de datos del LED RGB interno

Enfriador de Torre
----------------------------

El Pro MAX, el enfriador de torre es una solución de refrigeración de alto rendimiento diseñada para mantener su Raspberry Pi 5 a temperaturas óptimas durante tareas exigentes. Cuenta con un gran disipador de calor de aluminio y un ventilador que se puede controlar mediante PWM para ajustar el rendimiento de refrigeración según sea necesario. El enfriador de torre es compatible con la Raspberry Pi 5 y se puede instalar fácilmente usando los tornillos y el soporte de montaje incluidos.

.. image:: img/size_tower_cooler.png

**Advertencia**

No toque las aspas, ni permita que los cables de alimentación se enrollen alrededor del ventilador, ni tire de los cables de alimentación con fuerza para evitar dañar el ventilador.

No lo use en entornos con gases inflamables o cualquier peligro.

Cuando el ventilador esté funcionando, no intente bloquearlo durante mucho tiempo. Si lo hace, el ventilador se quemará debido al alto calor generado por la detención continua.

Al ensamblar el ventilador, preste especial atención al ruido generado por resonancia o vibración.

No deje caer el Enfriador de Torre Icecube desde una altura, ya que esto podría afectar el equilibrio de las aspas del ventilador.