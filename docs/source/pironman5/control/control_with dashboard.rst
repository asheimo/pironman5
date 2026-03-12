.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _view_control_dashboard:

Anzeigen und Steuern über das Dashboard
=========================================

Nach erfolgreicher Installation des Moduls ``pironman5`` startet der Dienst ``pironman5.service`` automatisch beim Neustart.

Jetzt können Sie die Überwachungsseite in Ihrem Browser öffnen, um Informationen zu Ihrem Raspberry Pi anzuzeigen, RGB-LEDs zu konfigurieren, den Lüfter zu steuern und vieles mehr. Der Link zur Seite lautet: ``http://<ip>:34001``.

Diese Seite umfasst **Dashboard**, **Verlauf**, **Protokoll** und eine **Einstellungen**-Seite.

.. image:: img/dashboard_tab_new.jpg

Dashboard
-----------------------

Das Dashboard enthält mehrere Karten zur Anzeige des Status Ihres Raspberry Pi, darunter:

* **Lüfter**: Zeigt die CPU-Temperatur des Raspberry Pi und die PWM-Lüftergeschwindigkeit an. **GPIO Fan State** zeigt den Status der seitlichen RGB-Lüfter an. Bei der aktuellen Temperatur sind die beiden RGB-Lüfter ausgeschaltet.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%

* **Speicher**: Zeigt die Speicherkapazität des Raspberry Pi, einschließlich der belegten und verfügbaren Bereiche der verschiedenen Partitionen.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Arbeitsspeicher**: Zeigt die RAM-Auslastung des Raspberry Pi in Prozent an.

  .. image:: img/dashboard_memory.png
    :width: 90%

* **Netzwerk**: Zeigt den aktuellen Netzwerkverbindungstyp sowie Upload- und Download-Geschwindigkeiten an.

  .. image:: img/dashboard_network.png
    :width: 90%

* **Prozessor**: Veranschaulicht die CPU-Leistung des Raspberry Pi, einschließlich des Status seiner vier Kerne, der Betriebsfrequenzen und der CPU-Auslastung in Prozent.

  .. image:: img/dashboard_processor.png
    :width: 90%

Verlauf
--------------

Auf der Seite „Verlauf“ können Sie historische Daten anzeigen. Wählen Sie im linken Seitenmenü die gewünschten Daten aus, legen Sie den Zeitraum fest, um die Daten für diesen Zeitraum anzuzeigen, und klicken Sie optional auf „Herunterladen“.

.. image:: img/dashboard_history1.png
  :width: 90%
  
.. image:: img/dashboard_history2.png
  :width: 90%

Protokoll
------------

Die Seite „Protokoll“ dient zur Anzeige der Protokolle des aktuell laufenden Pironman5-Dienstes. Der Pironman5-Dienst umfasst mehrere Unterdienste, die jeweils ein eigenes Protokoll haben. Wählen Sie das Protokoll aus, das Sie anzeigen möchten, und die Daten werden rechts angezeigt. Wenn keine Inhalte erscheinen, bedeutet dies möglicherweise, dass keine Protokollinhalte vorhanden sind.

* Jedes Protokoll hat eine feste Größe von 10 MB. Wird diese Größe überschritten, wird ein zweites Protokoll erstellt.
* Die Anzahl der Protokolle für denselben Dienst ist auf 10 begrenzt. Wenn diese Grenze überschritten wird, wird das älteste Protokoll automatisch gelöscht. Sie können Protokolle auch manuell löschen.
* Über den Protokollbereich auf der rechten Seite stehen Filtertools zur Verfügung. Sie können die Protokollebene auswählen, nach Schlüsselwörtern filtern und Tools wie **Zeilenumbruch**, **Automatisches Scrollen** und **Automatisches Aktualisieren** verwenden.
* Protokolle können auch lokal heruntergeladen werden.

.. image:: img/dashboard_log1.png
  :width: 90%
  
.. image:: img/dashboard_log2.png
  :width: 90%

Einstellungen
-----------------

Im oberen rechten Bereich der Seite befindet sich ein Einstellungsmenü, in dem Sie die Einstellungen nach Ihren Vorlieben anpassen können. Nach Änderungen werden diese automatisch gespeichert. Falls erforderlich, können Sie mit der Schaltfläche „CLEAR“ am unteren Rand die historischen Daten löschen.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Dunkelmodus**: Wechseln Sie zwischen den Themen „Hell“ und „Dunkel“. Diese Einstellung wird im Browser-Cache gespeichert. Ein Wechsel des Browsers oder das Leeren des Caches setzt das Thema auf das Standard-Hellthema zurück.
* **Temperatureinheit**: Legen Sie die vom System angezeigte Temperatureinheit fest.

**Über den OLED-Bildschirm**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **OLED Aktivieren**: Aktivieren oder deaktivieren Sie das OLED.
* **OLED Disk**: Legen Sie die OLED-Disk fest.
* **OLED Netzwerkschnittstelle**: 

  * **all**: Schaltet zwischen der Anzeige der Ethernet-IP und der Wi-Fi-IP um.
  * **eth0**: Zeigt nur die Ethernet-IP an.
  * **wlan0**: Zeigt nur die Wi-Fi-IP an.

* **OLED Rotation**: Legen Sie die Rotation des OLED fest.

**Über RGB-LEDs**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **RGB Aktivieren**: Aktivieren oder deaktivieren Sie die RGB-LEDs.
* **RGB Farbe**: Legen Sie die Farbe der RGB-LEDs fest.
* **RGB Helligkeit**: Passen Sie die Helligkeit der RGB-LEDs mit einem Schieberegler an.
* **RGB Stil**: Wählen Sie den Anzeigemodus der RGB-LEDs. Optionen sind **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** und **Hue Cycle**.

  .. note::

     Wenn Sie den **RGB Stil** auf **Rainbow**, **Rainbow Reverse** oder **Hue Cycle** einstellen, können Sie die Farbe nicht ändern.

* **RGB Geschwindigkeit**: Legen Sie die Geschwindigkeit der Farbwechsel der RGB-LEDs fest.

**Über RGB-Lüfter**

.. image:: img/RGB_FAN2.jpg
  :width: 600

.. * **Lüfter-LED**: Sie können die Lüfter-LED auf EIN, AUS oder FOLGEN-Modus einstellen.

* **Lüftermodus**: Legen Sie den Betriebsmodus der beiden RGB-Lüfter fest. Diese Modi bestimmen die Bedingungen, unter denen die RGB-Lüfter aktiviert werden.

    * **Leise**: Die RGB-Lüfter werden bei 70°C aktiviert.
    * **Ausgewogen**: Die RGB-Lüfter werden bei 67,5°C aktiviert.
    * **Kühl**: Die RGB-Lüfter werden bei 60°C aktiviert.
    * **Leistung**: Die RGB-Lüfter werden bei 50°C aktiviert.
    * **Immer an**: Die RGB-Lüfter sind immer eingeschaltet.

Zum Beispiel: Wenn der Modus auf **Leistung** eingestellt ist, werden die RGB-Lüfter bei 50°C aktiviert.

Nach dem Speichern, wenn die CPU-Temperatur 50°C überschreitet, sehen Sie, wie sich der **GPIO Fan State** im Dashboard auf EIN ändert, und die seitlichen RGB-Lüfter beginnen zu drehen.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300

**Über den Hauptlüfter**

Der Hauptlüfter wird an einen dedizierten 4-Pin-PWM-Lüfteranschluss auf dem Raspberry Pi 5 angeschlossen. Seine Standard-Steuerungsstrategie ist ein firmwaregesteuertes, mehrstufiges intelligentes Drehzahlanpassungssystem, das auf der CPU-Temperatur basiert. Das bedeutet, dass das System bei Verwendung eines offiziellen oder kompatiblen PWM-Lüfters und korrektem Anschluss die Lüftergeschwindigkeit automatisch an die Änderungen der CPU-Temperatur anpasst (er beginnt oberhalb von 50°C zu arbeiten), ohne dass ein manueller Eingriff Ihrerseits erforderlich ist.