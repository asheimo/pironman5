.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_pironman5:

4. Einrichten oder Software installieren
================================================

Nachdem das System nun auf die Micro-SD oder NVMe-SSD geschrieben wurde, können Sie diese in den Steckplatz des Pironman 5 Pro MAX einsetzen. Drücken Sie dann den Netzschalter, um das Gerät einzuschalten.

Nach dem Einschalten leuchten die verschiedenen Betriebs-LEDs auf, aber der OLED-Bildschirm, die RGB-LEDs und die RGB-Lüfter (die beiden Lüfter an der Seite) sind noch nicht funktionsfähig, da sie konfiguriert werden müssen. Falls es zu einer Bildschirmstörung kommt, ignorieren Sie diese vorerst; sie wird nach der Konfiguration behoben sein.

Bevor Sie konfigurieren, müssen Sie Ihren Raspberry Pi hochfahren und sich anmelden. Wenn Sie nicht wissen, wie Sie sich anmelden, besuchen Sie die offizielle Raspberry Pi-Website: |link_rpi_get_start|.

Anschließend können Sie basierend auf Ihrem System das entsprechende Konfigurations-Tutorial auswählen.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os
    set_up_umbrel

.. set_up_batocera

.. set_up_home_assistant

**Über den Netzschalter**

Der Netzschalter führt den Netzschalter des Raspberry Pi 5 heraus und funktioniert genauso wie der Netzschalter des Raspberry Pi 5.

* **Herunterfahren**

    * Wenn Sie das System **Raspberry Pi OS Desktop** ausführen, können Sie den Netzschalter zweimal schnell hintereinander drücken, um herunterzufahren.
    * Wenn Sie das System **Raspberry Pi OS Lite** ausführen, drücken Sie den Netzschalter einmal, um ein Herunterfahren einzuleiten.
    * Um ein erzwungenes Herunterfahren durchzuführen, halten Sie den Netzschalter gedrückt.

* **Einschalten**

    * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, schaltet ein einzelner Tastendruck es aus dem heruntergefahrenen Zustand wieder ein.

* Wenn Sie ein System ausführen, das keinen Ausschaltknopf unterstützt, können Sie ihn 5 Sekunden lang gedrückt halten, um ein erzwungenes Herunterfahren zu erzwingen, und durch einmaliges Drücken aus dem heruntergefahrenen Zustand wieder einschalten.