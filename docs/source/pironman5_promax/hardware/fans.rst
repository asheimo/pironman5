.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Lüfter
============

PWM-Lüfter
-----------

Der Pironman 5 Pro MAX verfügt über 3 PWM-Lüfter.

Der PWM-Lüfter am Pironman 5 Pro MAX wird vom Raspberry-Pi-System gesteuert.

Bei den Kühlungslösungen für den Raspberry Pi 5, insbesondere unter starker Last, integriert das Design des Pironman 5 Pro MAX ein intelligentes Kühlsystem. Es verfügt über einen primären PWM-Lüfter und zwei zusätzliche RGB-Lüfter. Die Kühlstrategie ist eng mit dem Thermalmanagement-System des Raspberry Pi 5 verzahnt.

Der Betrieb des PWM-Lüfters basiert auf der Temperatur des Raspberry Pi 5:

* Unter 50°C bleibt der PWM-Lüfter aus (0% Geschwindigkeit).
* Bei 50°C startet der Lüfter mit niedriger Geschwindigkeit (30% Geschwindigkeit).
* Bei Erreichen von 60°C erhöht der Lüfter auf mittlere Geschwindigkeit (50% Geschwindigkeit).
* Bei 67,5°C erhöht der Lüfter auf hohe Geschwindigkeit (70% Geschwindigkeit).
* Bei 75°C und darüber arbeitet der Lüfter mit voller Geschwindigkeit (100% Geschwindigkeit).

Diese Beziehung zwischen Temperatur und Geschwindigkeit gilt auch bei sinkender Temperatur, mit einer Hysterese von 5°C. Die Lüftergeschwindigkeit wird reduziert, wenn die Temperatur 5°C unter jeden dieser Schwellenwerte fällt.

* Befehle zur Überwachung des PWM-Lüfters. So überprüfen Sie den Status des PWM-Lüfters:

  .. code-block:: shell

    cat /sys/class/thermal/cooling_device0/cur_state

* So zeigen Sie die Drehzahl des PWM-Lüfters an:

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Im Pironman 5 Pro MAX ist der PWM-Lüfter eine kritische Komponente zur Aufrechterhaltung optimaler Betriebstemperaturen, insbesondere bei intensiven Aufgaben, und stellt sicher, dass der Raspberry Pi 5 effizient und zuverlässig läuft.

**Lüfter-Spezifikationen**

.. image:: img/size_fan.png

* **Außenabmessung**: 40*40*10MM
* **Nenneingangsleistung**: 5V/0,106A
* **Nenndrehzahl**: 4000 U/min
* **Gewicht**: 13,5±5g/Stück
* **Lebensdauer**: 30.000 Stunden (Raumtemperatur 25°C)
* **Geräuschentwicklung**: 22,31dBA
* **Maximaler Luftstrom**: 2,46CFM
* **Max. Luftdruck**: 0,62mm-H2O
* **Betriebstemperatur**: -10℃~+60℃
* **Lagertemperatur**: -20℃~+70℃

**Pinbelegung**

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Pin
     - Farbe
     - Beschreibung
   * - 1
     - Blau
     - PWM-Signal zur Steuerung der Lüftergeschwindigkeit
   * - 2
     - Rot
     - 5V Stromversorgung
   * - 3
     - Schwarz
     - Masse
   * - 4
     - Gelb
     - Dateneingang der internen RGB-LED
   * - 5
     - Grün
     - Datenausgang der internen RGB-LED


Tower-Kühler
----------------------------

Beim Pro MAX ist der Tower-Kühler eine leistungsstarke Kühllösung, die entwickelt wurde, um Ihren Raspberry Pi 5 auch bei anspruchsvollen Aufgaben auf optimalen Temperaturen zu halten. Er verfügt über einen großen Aluminium-Kühlkörper und einen Lüfter, der per PWM gesteuert werden kann, um die Kühlleistung nach Bedarf anzupassen. Der Tower-Kühler ist mit dem Raspberry Pi 5 kompatibel und kann einfach mit den mitgelieferten Schrauben und der Montagehalterung installiert werden.


.. image:: img/size_tower_cooler.png

**Warnung**

Berühren Sie nicht die Rotorblätter, lassen Sie die Stromkabel nicht um den Lüfter wickeln und ziehen Sie nicht mit Gewalt an den Stromkabeln, um eine Beschädigung des Lüfters zu vermeiden.

Nicht in Umgebungen mit brennbaren Gasen oder in gefährlichen Umgebungen verwenden.

Versuchen Sie nicht, den Lüfter für längere Zeit zu blockieren, während er in Betrieb ist. Andernfalls brennt der Lüfter aufgrund der hohen Wärmeentwicklung durch den dauerhaften Stillstand durch.

Achten Sie beim Zusammenbau des Lüfters besonders auf Geräusche, die durch Resonanz oder Vibration entstehen können.

Lassen Sie den Icecube Tower-Kühler nicht aus der Höhe fallen, da dies das Gleichgewicht der Lüfterblätter beeinträchtigen kann.