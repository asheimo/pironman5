.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Dual-NVMe-PIP
=====================

Das **Dual NVMe PIP** (PCIe-Peripherieplatine), wie von der Raspberry Pi Foundation definiert, ist ein PCIe-Adapter, der speziell für NVMe-Solid-State-Laufwerke entwickelt wurde.

Die PCIe-Schnittstelle des Raspberry Pi 5 bietet nativ eine einzelne **Gen2 x1**-Lane (500 MB/s). Durch die Integration des **ASM1182e**-PCIe-Switch-Chips erweitert das Dual-NVMe-PIP diese zu **zwei unabhängigen Gen2-x1-Lanes**, sodass Sie anschließen können:

* **Zwei M.2-NVMe-SSDs** oder
* **Eine M.2-NVMe-SSD + einen M.2-Hailo-8/8L-AI-Beschleuniger**

**Wichtige Hinweise**:

* Gen3 wird nicht unterstützt
* Unterstützt NVMe-SSD-Größen: **2230**, **2242**, **2260**, **2280** (alle in M.2-M-Key-Steckplätzen)

.. image:: img/nvme_pip.png

* Die Platine wird über ein 16-poliges 0,5-mm-Reverse-FFC-Kabel (Flexible Flat Cable) oder ein kundenspezifisches impedanzangepasstes FPC-Kabel (Flexible Printed Circuit) angeschlossen.
* **STA**: Eine Status-LED-Anzeige.
* **PWR**: Eine Betriebs-LED-Anzeige.
* Die integrierte 3,3-V-Stromversorgung kann bis zu 3 A Ausgangsstrom liefern. Da die PCIe-Schnittstelle des Raspberry Pi jedoch auf eine Ausgangsleistung von 5 V/1 A (entspricht 5 W) begrenzt ist, kann zusätzliche Energie für die 3,3-V/3-A-Nutzung über den J3-Anschluss von einer 5-V-Quelle zugeführt werden.
* **FORCE ENABLE**: Die integrierte Stromversorgung wird durch das Schaltsignal der PCIe-Schnittstelle aktiviert. Nach dem Einschalten des Raspberry Pi sendet dieser ein Signal, um die 3,3-V-Stromversorgung einzuschalten. Falls einige Systeme das Schaltsignal nicht unterstützen oder aus anderen Gründen, können Sie J4 FORCE ENABLE durch Löten eines Drahts zwischen den beiden freiliegenden Pads kurzschließen, um die integrierte 3,3-V-Stromversorgung für die NVMe zu erzwingen.

Über das Modell
---------------------------

M.2-SSDs, bekannt für ihre kompakte Größe, gibt es in verschiedenen Typen, die sich hauptsächlich durch ihre Codierung (Kerbe im Stecker) und die verwendete Schnittstelle unterscheiden. Hier sind die wichtigsten Typen:

* **M.2-SATA-SSDs**: Diese verwenden die SATA-Schnittstelle, ähnlich wie 2,5-Zoll-SATA-SSDs, aber im kleineren M.2-Formfaktor. Sie sind durch die maximalen Geschwindigkeiten von SATA III von etwa 600 MB/s begrenzt. Diese SSDs sind mit M.2-Steckplätzen kompatibel, die für B- und M-Key codiert sind.
* **M.2-NVMe-SSDs**: Diese SSDs verwenden das NVMe-Protokoll über PCIe-Lanes und sind deutlich schneller als M.2-SATA-SSDs. Sie eignen sich für Anwendungen, die hohe Lese-/Schreibgeschwindigkeiten erfordern, wie Spiele, Videobearbeitung und datenintensive Aufgaben. Diese SSDs benötigen typischerweise M-Key-Steckplätze. Diese Laufwerke nutzen die PCIe-Schnittstelle (Peripheral Component Interconnect Express) in verschiedenen Versionen wie 3.0, 4.0 und 5.0. Jede neue PCIe-Version verdoppelt effektiv die Datenübertragungsgeschwindigkeit ihres Vorgängers. Der Raspberry Pi 5 verwendet jedoch eine PCIe-3.0-Schnittstelle, die Übertragungsgeschwindigkeiten von bis zu 3500 MB/s erreichen kann.

M.2-SSDs gibt es in drei Codierungsarten: B-Key, M-Key und B+M-Key. Später wurde jedoch der B+M-Key eingeführt, der die Funktionalitäten von B-Key und M-Key kombiniert. Infolgedessen ersetzte er den eigenständigen B-Key. Bitte beachten Sie das folgende Bild.

.. image:: img/ssd_key.png


Im Allgemeinen sind M.2-SATA-SSDs B+M-key-codiert (passen in Sockel für B-key- und M-key-Module), während M.2-NVMe-SSDs für PCIe-3.0-x4-Lanes M-key-codiert sind.

.. image:: img/ssd_model2.png

Über die Länge
-----------------------

M.2-Module gibt es in verschiedenen Größen und können auch für WLAN, WWAN, Bluetooth, GPS und NFC verwendet werden.

Der Pironman 5 MAX unterstützt vier (PCIe Gen 2.0) NVMe-M.2-SSD-Größen basierend auf ihrer Bezeichnung: 2230, 2242, 2260 und 2280. Die "22" ist die Breite in Millimetern (mm), und die folgenden zwei Zahlen sind die Länge. Je länger das Laufwerk, desto mehr NAND-Flash-Chips können montiert werden; daher desto größer die Kapazität.


.. image:: img/m2_ssd_size.png
  :width: 600


Stromversorgung
-----------------------

Die integrierte doppelte 3,3-V-Stromversorgung unterstützt einen maximalen Ausgang von 3 A (10 W). Beide Stromschienen arbeiten unabhängig voneinander ohne Störungen.

**FORCE ENABLE**
Die integrierte Stromversorgung wird durch das Schaltsignal der PCIe-Schnittstelle aktiviert. Nach dem Hochfahren des Raspberry Pi schaltet das Signal die 3,3-V-Stromversorgung ein. Falls das System das Schaltsignal nicht unterstützt oder aus anderen Gründen, schließen Sie den J4 FORCE EN-Jumper kurz, um die integrierte 3,3-V-Stromversorgung für die NVMe zwangsweise zu aktivieren.

**LED**
Jede Schnittstelle verfügt über unabhängige Betriebsanzeigen (PWR) und Statusanzeigen (STA).

Netzschalter-Konverter
-------------------------------


**Hinzufügen des Netzschalters**

* Der Raspberry Pi 5 verfügt über einen **J2**-Jumper, der sich zwischen dem RTC-Batterieanschluss und der Platinenkante befindet. Diese Durchkontaktierung ermöglicht das Hinzufügen eines benutzerdefinierten Netzschalters zum Raspberry Pi 5, indem ein Taster (Schließer) über die beiden Pads angeschlossen wird. Kurzes Betätigen dieses Schalters ahmt die Funktionalität des integrierten Netzschalters nach.

   .. image:: img/pi5_j2.jpg

* Beim Pironman 5 gibt es einen **Netzschalter-Konverter**, der den **J2**-Jumper über zwei Pogo-Pins zu einem externen Netzschalter führt.

   .. image:: img/psc.png

* Jetzt kann der Raspberry Pi 5 mit dem Netzschalter ein- und ausgeschaltet werden.

**Ein-/Ausschalten**

Beim ersten Einschalten Ihres Raspberry Pi 5 wird dieser automatisch eingeschaltet und bootet in das Betriebssystem, ohne dass Sie die Taste drücken müssen.

Wenn Sie den Raspberry Pi Desktop ausführen, wird durch kurzes Drücken des Netzschalters ein sauberer Herunterfahrvorgang eingeleitet. Ein Menü wird angezeigt, das Optionen zum Herunterfahren, Neustarten oder Abmelden bietet. Durch Auswahl einer Option oder erneutes Drücken des Netzschalters wird ein sauberes Herunterfahren gestartet.

.. image:: img/button_shutdown.png

**Herunterfahren**

    * Wenn Sie das System **Raspberry Pi OS Desktop** ausführen, können Sie den Netzschalter zweimal schnell hintereinander drücken, um herunterzufahren.
    * Wenn Sie das System **Raspberry Pi OS Lite** ohne Desktop ausführen, drücken Sie den Netzschalter einmal, um ein Herunterfahren einzuleiten.
    * Um ein erzwungenes Herunterfahren durchzuführen, halten Sie den Netzschalter gedrückt.


**Einschalten**

    * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, schaltet ein einzelner Tastendruck es aus dem heruntergefahrenen Zustand wieder ein.

.. note::

    Wenn Sie ein System ausführen, das keinen Ausschaltknopf unterstützt, können Sie ihn 5 Sekunden lang gedrückt halten, um ein erzwungenes Herunterfahren zu erzwingen, und durch einmaliges Drücken aus dem heruntergefahrenen Zustand wieder einschalten.