.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_view_control_dashboard:

Ansicht und Steuerung über das Dashboard
=========================================

Sobald Sie das Modul ``pironman5`` erfolgreich installiert haben, wird der ``pironman5.service`` nach einem Neustart automatisch gestartet.

Jetzt können Sie die Überwachungsseite in Ihrem Browser öffnen, um Informationen über Ihren Raspberry Pi anzuzeigen, die RGB zu konfigurieren usw. Der Seiten-Link lautet: ``http://<ip>:34001``.

.. image:: img/dashboard_prm5promax.png
  :width: 90%


Diese Seite hat einen Bereich **Dashboard**, **History**, **Log** und eine Seite **Settings**.


.. image:: img/dashboard_tab.png
  :width: 90%

Dashboard
-----------------------

Es gibt mehrere Karten, um den relevanten Status des Raspberry Pi anzuzeigen, darunter:

* **Temperature**: Zeigt die CPU- & GPU-Temperatur des Raspberry Pi an.

  .. image:: img/dashboard_temp.png
    :align: center


* **Storage**: Zeigt die Speicherkapazität eines Raspberry Pi an und zeigt verschiedene Datenträgerpartitionen mit ihrem belegten und verfügbaren Speicherplatz an.

  .. image:: img/dashboard_storage.png
    :align: center


* **Memory**: Zeigt die RAM-Nutzung und den Prozentsatz des Raspberry Pi an.

  .. image:: img/dashboard_memory.png
    :align: center


* **Network**: Zeigt den aktuellen Netzwerkverbindungstyp, Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :align: center


* **Processor**: Veranschaulicht die CPU-Leistung des Raspberry Pi, einschließlich des Status seiner vier Kerne, Betriebsfrequenzen und CPU-Auslastungsprozentsatz.

  .. image:: img/dashboard_processor.png
    :align: center


History
--------------

Auf der Seite History können Sie historische Daten einsehen. Wählen Sie in der linken Seitenleiste die Daten aus, die Sie anzeigen möchten, und wählen Sie dann den Zeitraum aus, um die Daten für diesen Zeitraum zu sehen. Sie können sie auch durch Klicken herunterladen.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Log
------------

Die Seite Log dient zum Anzeigen der Protokolle des aktuell laufenden Pironman5-Dienstes. Der Pironman5-Dienst umfasst mehrere Unterdienste, jeder mit seinem eigenen Protokoll. Wählen Sie das Protokoll aus, das Sie anzeigen möchten, und Sie können die Protokolldaten auf der rechten Seite sehen. Wenn es leer ist, kann das bedeuten, dass es keinen Protokollinhalt gibt.

* Jedes Protokoll hat eine feste Größe von 10 MB. Wenn diese Größe überschritten wird, wird ein zweites Protokoll erstellt.
* Die Anzahl der Protokolle für denselben Dienst ist auf 10 begrenzt. Wenn die Anzahl diese Grenze überschreitet, wird das älteste Protokoll automatisch gelöscht.
* Oberhalb des Protokollbereichs auf der rechten Seite befinden sich Filterwerkzeuge. Sie können die Protokollebene auswählen, nach Stichwörtern filtern und mehrere praktische Werkzeuge verwenden, darunter **Zeilenumbruch**, **Automatisches Scrollen** und **Automatische Aktualisierung**.
* Protokolle können auch lokal heruntergeladen werden.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%


Settings
-----------------

Es gibt ein Einstellungsmenü in der **oberen rechten Ecke** der Seite, in dem Sie die Einstellungen nach Ihren Wünschen anpassen können. Nach Änderungen werden die Einstellungen automatisch gespeichert. Bei Bedarf können Sie unten auf die Schaltfläche CLEAR klicken, um die historischen Daten zu löschen.

.. image:: img/dashboard_setting_darkmode.png
  :width: 600

* **Dark Mode**: Umschalten zwischen hellem und dunklem Design. Die Designoption wird im Browser-Cache gespeichert. Ein Wechsel des Browsers oder das Löschen des Caches setzt das Design auf das standardmäßige helle Design zurück.
* **Show Unmounted Disk**: Ob nicht eingehängte Datenträger im Dashboard angezeigt werden sollen.
* **Show All Cores**: Ob alle Kerne im Dashboard angezeigt werden sollen.
* **Card layout**: Legt das Kartenlayout des Dashboards fest.
* **Temperature Unit**: Legt die vom System angezeigte Temperatureinheit fest.

**About OLED Screen**

.. image:: img/dashboard_setting_oled.png
  :width: 600

* **OLED Enable**: Ob OLED aktiviert werden soll.
* **OLED Rotation**: OLED-Rotation einstellen.
* **OLED Sleep Timeout**: OLED-Schlaf-Timeout einstellen.

* **OLED Page**: Legt die anzuzeigende OLED-Seite fest: **System Mix**, **Performance Metrics**, **Disk Usage**, **IP Addresses**.



**About RGB LEDs**

.. image:: img/dashboard_setting_rgb.png
  :width: 600

* **RGB Enable**: Ob RGB-LEDs aktiviert werden sollen.
* **RGB Color**: Legt die Farbe der RGB-LEDs fest.
* **RGB Brightness**: Sie können die Helligkeit der RGB-LEDs mit einem Schieberegler einstellen.
* **RGB Style**: Wählen Sie den Anzeigemodus der RGB-LEDs. Zu den Optionen gehören **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** und **Hue Cycle**.
* **RGB Speed**: Legt die Geschwindigkeit der RGB-LED-Änderungen fest.
* **RGB Led**: Legt die Anzahl der zu steuernden RGB-LEDs fest.


**About Data**

.. image:: img/dashboard_setting_debug.png
  :width: 600

* **Debug Level**: Legt die Debug-Ebene fest. Zu den Optionen gehören **Info**, **Warning**, **Error** und **Critical**.
* **History Retention**: Legt die Anzahl der Tage fest, für die historische Daten aufbewahrt werden sollen.
* **Clear All Data**: Löscht alle historischen Daten.
* **Reboot**: Startet das System neu.
* **Shutdown**: Fährt das System herunter.
* **Restart service**: Startet die Systemdienste neu.

**Fan**

Der Kernlüfter wird an einen dedizierten 4-Pin-PWM-Lüfteranschluss des Raspberry Pi 5 angeschlossen. Seine Standardsteuerungsstrategie ist ein firmwaregesteuertes, mehrstufiges intelligentes Drehzahlanpassungsschema basierend auf der CPU-Temperatur. Das bedeutet, dass das System bei Verwendung eines offiziellen oder kompatiblen PWM-Lüfters und korrektem Anschluss die Lüftergeschwindigkeit automatisch an Änderungen der CPU-Temperatur anpasst (Beginn des Betriebs über 50°C), ohne dass ein manueller Eingriff erforderlich ist.