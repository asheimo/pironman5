.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_view_control_commands:

Steuerung mit Befehlen
========================================
Neben der Anzeige von Daten des Pironman 5 Pro MAX und der Steuerung verschiedener Geräte über das Dashboard können Sie auch Befehle zu deren Steuerung verwenden.

.. note::

  * Für das **Home Assistant**-System können Sie den Pironman 5 Pro MAX nur über das Dashboard überwachen und steuern, indem Sie die Webseite ``http://<ip>:34001`` öffnen.

Grundkonfigurationen anzeigen
-----------------------------------

Das Modul ``pironman5`` bietet grundlegende Konfigurationen für Pironman, die Sie mit dem folgenden Befehl einsehen können.

.. code-block:: shell

  sudo pironman5 -c

Die Standardkonfigurationen erscheinen wie folgt:

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "enable_history": true,
          "rgb_color": "#ff3dbe",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 18,
          "temperature_unit": "C",
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "default_dashboard_page": "small",
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "debug_level": "INFO"
      }
  }

Passen Sie diese Konfigurationen an Ihre Bedürfnisse an.

Verwenden Sie ``pironman5`` oder ``pironman5 -h`` für Anweisungen.

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Pironman 5 Pro Max Befehlszeilenschnittstelle

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                          Database retention days
    -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                          Debug level
    -rd, --remove-dashboard
                          Remove dashboard
    -cp, --config-path [CONFIG_PATH]
                          Config path
    -eh, --enable-history [ENABLE_HISTORY]
                          Enable history, True/true/on/On/1 or False/false/off/Off/0
    -re, --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rs, --rgb-style [RGB_STYLE]
                          RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
    -rc, --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb, --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rp, --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -rl, --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u, --temperature-unit [{C,F}]
                          Temperature unit
    -oe, --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -or, --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -op, --oled-pages [OLED_PAGES]
                          OLED pages, split by ',': mix,performance,ips,disk
    -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds

  Subcommands:
    {start,stop,launch-browser}
      start               Start Pironman5
      stop                Stop Pironman5
      launch-browser      Launch browser



.. note::

  Jedes Mal, wenn Sie den Status von ``pironman5.service`` ändern, müssen Sie den folgenden Befehl verwenden, um die Konfigurationsänderungen zu übernehmen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Überprüfen Sie den Status des ``pironman5``-Programms mit dem ``systemctl``-Werkzeug.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Oder überprüfen Sie die vom Programm erstellten Protokolldateien.

  .. code-block:: shell

    ls /var/log/pironman5/


**RGB-LEDs steuern**
----------------------
Die Platine verfügt über 18 adressierbare WS2812B-RGB-LEDs: 6 auf der Platine und 12 in die RGB-Lüfter integriert. Benutzer können Strom, Farbe, Helligkeit, Anzeigemodi, Animationsgeschwindigkeit und die Anzahl der aktiven LEDs steuern.

.. note::

  Nach dem Ändern der Konfiguration für ``pironman5.service`` müssen Sie den Dienst neu starten, damit die Änderungen wirksam werden:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **RGB-LEDs aktivieren/deaktivieren**: Verwenden Sie ``true`` zum Einschalten, ``false`` zum Ausschalten.

.. code-block:: shell

  sudo pironman5 -re true

* **Farbe ändern**: Legen Sie eine Farbe mit einem hexadezimalen Wert fest (ohne das `#`), z.B. ``fe1a1a`` für Rot.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* **Helligkeit anpassen**: Stellen Sie die Helligkeit von 0% bis 100% ein.

.. code-block:: shell

  sudo pironman5 -rb 75

* **Anzeigemodus ändern**: Wählen Sie aus mehreren Animationsmodi:

  * ``solid``: Statische Farbe.
  * ``breathing``: Pulsierendes Ein-/Ausblenden.
  * ``flow`` / ``flow_reverse``: Farbe fließt in eine Richtung.
  * ``rainbow`` / ``rainbow_reverse``: Durchläuft ein Regenbogenspektrum.
  * ``hue_cycle``: Durchläuft sanft die Farbtöne.

.. code-block:: shell

  sudo pironman5 -rs breathing

.. note::

  Bei Verwendung der Modi ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` wird die über ``pironman5 -rc`` eingestellte Farbe durch den automatischen Farbzyklus des Modus überschrieben.

* **Animationsgeschwindigkeit anpassen**: Steuern Sie die Geschwindigkeit der Effekte von 0% (langsamste) bis 100% (schnellste).

.. code-block:: shell

  sudo pironman5 -rp 50

* **LED-Anzahl festlegen**: Das System steuert standardmäßig 18 LEDs. Wenn Sie die Kette mit zusätzlichen externen WS2812B-LEDs erweitert haben, aktualisieren Sie die Gesamtzahl entsprechend.

.. code-block:: shell

  sudo pironman5 -rl 12

**Lüfter**
--------------------------------

Der Kernlüfter wird an einen dedizierten 4-Pin-PWM-Lüfteranschluss des Raspberry Pi 5 angeschlossen. Seine Standardsteuerungsstrategie ist ein firmwaregesteuertes, mehrstufiges intelligentes Drehzahlanpassungsschema basierend auf der CPU-Temperatur. Das bedeutet, dass das System bei Verwendung eines offiziellen oder kompatiblen PWM-Lüfters und korrektem Anschluss die Lüftergeschwindigkeit automatisch an Änderungen der CPU-Temperatur anpasst (Beginn des Betriebs über 50°C), ohne dass ein manueller Eingriff erforderlich ist.



**OLED-Bildschirm überprüfen**
-----------------------------------

Der 0,96-Zoll-OLED-Bildschirm zeigt nach der Installation der Bibliothek ``pironman5`` und einem Neustart standardmäßig Systeminformationen (CPU, RAM, Festplatte, Temp, IP) an.

Wenn der OLED-Bildschirm leer ist:

1.  Stellen Sie sicher, dass das FPC-Kabel des OLEDs fest mit der Hauptplatine verbunden ist.
2.  Überprüfen Sie das Dienstprotokoll auf Fehler:

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    Oder überprüfen Sie das spezifische OLED-Protokoll:

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3.  Überprüfen Sie, ob das OLED auf dem I2C-Bus erkannt wird (Adresse `0x3C`):

    .. code-block:: shell

      i2cdetect -y 1

**OLED-Konfigurationsbefehle**

* **OLED aktivieren/deaktivieren**: Schalten Sie die OLED-Anzeige ein oder aus.

    .. code-block:: shell

      sudo pironman5 -oe false

* **Anzeige drehen**: Stellen Sie die Bildschirmausrichtung auf ``0`` (Standard) oder ``180`` Grad ein.

    .. code-block:: shell

      sudo pironman5 -or 180

* **Anzeigeseiten konfigurieren**: Wählen Sie aus, welche Infoseiten durchlaufen werden sollen. Seiten sind: ``mix`` (Übersicht), ``performance`` (detaillierte CPU/RAM), ``ips`` (Netzwerk-IPs), ``disk`` (Speicher). Trennen Sie mehrere Seiten durch Kommas.

    .. code-block:: shell

      sudo pironman5 -op mix,ips,disk

* **Schlaf-Timeout einstellen**: Legen Sie fest, nach wie vielen Sekunden Inaktivität sich das OLED ausschalten soll (0 = nie schlafen).

    .. code-block:: shell

      sudo pironman5 -os 120

**Infrarotempfänger überprüfen**
---------------------------------------

Der integrierte IR-Empfänger ermöglicht die Steuerung per Fernbedienung.

1.  Installieren Sie die erforderliche Software:

    .. code-block:: shell

      sudo apt-get install lirc -y

2.  Testen Sie den Empfänger. Führen Sie den folgenden Befehl aus, richten Sie dann eine Fernbedienung auf das Gehäuse und drücken Sie Tasten. Sie sollten eine rohe Codeausgabe sehen.

    .. code-block:: shell

      mode2 -d /dev/lirc0

3.  Um spezifische Tastenzuordnungen für die Fernbedienung einzurichten (z.B. für Kodi oder Volumio), müssen Sie die Datei `/etc/lirc/lircd.conf` mit den Codes Ihrer Fernbedienung konfigurieren.




**Allgemeine Systembefehle**
----------------------------

* **Version anzeigen**: Zeigt die installierte Version des Pakets ``pironman5`` an.

.. code-block:: shell

  sudo pironman5 -v

* **Aktuelle Konfiguration anzeigen**: Zeigt alle aktuellen Einstellungen an.

.. code-block:: shell

  sudo pironman5 -c

* **Temperatureinheit einstellen**: Wechseln Sie zwischen Celsius (``C``) und Fahrenheit (``F``) für die Temperaturanzeigen.

.. code-block:: shell

  sudo pironman5 -u F

* **Datenprotokollierung konfigurieren**:

  * **Aufbewahrungstage für die Datenbank festlegen**: Steuern Sie, wie viele Tage historische Daten (wie Temperaturprotokolle) aufbewahrt werden.

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **Verlaufsprotokollierung aktivieren/deaktivieren**: Schalten Sie die Datenerfassung ein oder aus.

    .. code-block:: shell

      sudo pironman5 -eh false

* **Ausführlichkeit der Protokollierung einstellen**: Passen Sie die Detailtiefe der Systemprotokolle an. Optionen: ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``.

.. code-block:: shell

  sudo pironman5 -dl DEBUG

* **Web-Dashboard entfernen**: Deinstallieren Sie die optionale webbasierte Verwaltungsoberfläche.

.. code-block:: shell

  sudo pironman5 -rd

* **Benutzerdefinierten Konfigurationspfad angeben**: Verwenden Sie eine Konfigurationsdatei von einem nicht standardmäßigen Speicherort.

.. code-block:: shell

  sudo pironman5 -cp /home/pi/meine_benutzerdefinierte_config.json

**Dienstverwaltungs-Unterbefehle**
-----------------------------------

* **Pironman5-Dienst starten**: Starten Sie manuell den Hintergrunddienst, der LEDs, Lüfter, OLED usw. verwaltet.

.. code-block:: shell

  sudo pironman5 start

* **Pironman5-Dienst stoppen**: Beenden Sie den Hintergrunddienst ordnungsgemäß.

.. code-block:: shell

  sudo pironman5 stop

* **Web-Dashboard im Browser starten**: Wenn das Web-Dashboard installiert ist, öffnet dieser Befehl es in Ihrem Standardbrowser.

.. code-block:: shell

  sudo pironman5 launch-browser