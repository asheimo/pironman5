.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _max_view_control_commands:

Steuerung mit Befehlen
========================================
Neben der Anzeige von Daten des Pironman 5 MAX und der Steuerung verschiedener Geräte über das Dashboard, kannst du diese auch über Befehle steuern.

.. note::

  * Beim **Home Assistant**-System kannst du den Pironman 5 MAX nur über das Dashboard überwachen und steuern, indem du die Webseite unter ``http://<ip>:34001`` öffnest.

.. * Beim **Batocera.linux**-System kannst du den Pironman 5 MAX nur über Befehle überwachen und steuern. Es ist wichtig zu beachten, dass Änderungen an der Konfiguration einen Neustart des Dienstes mit ``pironman5 restart`` erfordern, damit sie wirksam werden.

Anzeige der Basiskonfigurationen
-----------------------------------

Das ``pironman5``-Modul bietet grundlegende Konfigurationen für Pironman, die du mit folgendem Befehl anzeigen kannst.

.. code-block:: shell

  sudo pironman5 -c

Die Standardkonfigurationen erscheinen wie folgt:

.. code-block:: 

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

Passe diese Konfigurationen nach deinen Bedürfnissen an.

Verwende ``pironman5`` oder ``pironman5 -h`` für Anweisungen.

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]     
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]]
                          [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop}]

  Pironman 5 MAX command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin
    -oe [OLED_ENABLE], --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -od [OLED_DISK], --oled-disk [OLED_DISK]
                          Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme
    -oi [OLED_NETWORK_INTERFACE], --oled-network-interface [OLED_NETWORK_INTERFACE]
                          Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or      
                          wlan0
    -or [{0,180}], --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds



.. note::

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den folgenden Befehl verwenden, um die Konfigurationsänderungen wirksam zu machen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Überprüfe den Status des ``pironman5``-Programms mit dem ``systemctl``-Tool.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternativ kannst du die vom Programm generierten Log-Dateien einsehen.

  .. code-block:: shell

    ls /var/log/pironman5/


Steuerung der RGB-LEDs
-------------------------

Das Board verfügt über 4 WS2812 RGB-LEDs, die eine anpassbare Steuerung bieten. Benutzer können sie ein- oder ausschalten, die Farbe ändern, die Helligkeit anpassen, die RGB-LED-Anzeigemodi wechseln und die Geschwindigkeit der Änderungen festlegen.

.. note::

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den folgenden Befehl verwenden, um die Konfigurationsänderungen wirksam zu machen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Um den Ein- und Aus-Zustand der RGB-LEDs zu ändern, verwende ``true``, um die RGB-LEDs einzuschalten, und ``false``, um sie auszuschalten.

.. code-block:: shell

  sudo pironman5 -re true

* Um die Farbe zu ändern, gib die gewünschten hexadezimalen Farbwerte ein, wie z.B. ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Um die Helligkeit der RGB-LED zu ändern (Bereich: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rb 100

* Um die Anzeigemodi der RGB-LED zu wechseln, wähle aus den Optionen: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``:

.. note::

  Wenn du den RGB-LED-Anzeigemodus auf ``rainbow``, ``rainbow_reverse`` oder ``hue_cycle`` einstellst, kannst du die Farbe nicht mit ``sudo pironman5 -rc`` festlegen.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Um die Geschwindigkeit der Änderungen zu ändern (Bereich: 0 ~ 100%):

.. code-block:: shell

  sudo pironman5 -rp 80

* Die Standardkonfiguration umfasst 4 RGB-LEDs. Schließe zusätzliche LEDs an und aktualisiere die Anzahl mit:

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

Steuerung der RGB-Lüfter
---------------------------

Das IO-Erweiterungsboard unterstützt bis zu zwei 5V-Nicht-PWM-Lüfter. Beide Lüfter werden gemeinsam gesteuert.

.. note::

  Jedes Mal, wenn du den Status von ``pironman5.service`` änderst, musst du den folgenden Befehl verwenden, um die Konfigurationsänderungen wirksam zu machen.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Du kannst den Betriebmodus der beiden RGB-Lüfter über einen Befehl konfigurieren. Diese Modi bestimmen, unter welchen Bedingungen die RGB-Lüfter aktiviert werden.

Zum Beispiel, wenn auf **1: Performance**-Modus eingestellt, werden die RGB-Lüfter bei 50°C aktiviert.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**: Die RGB-Lüfter werden bei 70°C aktiviert.
* **3: Balanced**: Die RGB-Lüfter werden bei 67,5°C aktiviert.
* **2: Cool**: Die RGB-Lüfter werden bei 60°C aktiviert.
* **1: Performance**: Die RGB-Lüfter werden bei 50°C aktiviert.
* **0: Always On**: Die RGB-Lüfter sind immer eingeschaltet.

* Wenn du den Steuerpin des RGB-Lüfters an verschiedene Pins des Raspberry Pi anschließt, kannst du den folgenden Befehl verwenden, um die Pin-Nummer zu ändern.

.. code-block:: shell

  sudo pironman5 -gp 18

**Über den Hauptlüfter**

Der Hauptlüfter wird an einen dedizierten 4-Pin-PWM-Lüfteranschluss auf dem Raspberry Pi 5 angeschlossen. Seine Standard-Steuerungsstrategie ist ein firmwaregesteuertes, mehrstufiges intelligentes Drehzahlanpassungssystem, das auf der CPU-Temperatur basiert. Das bedeutet, dass das System bei Verwendung eines offiziellen oder kompatiblen PWM-Lüfters und korrektem Anschluss die Lüftergeschwindigkeit automatisch an die Änderungen der CPU-Temperatur anpasst (er beginnt oberhalb von 50°C zu arbeiten), ohne dass ein manueller Eingriff Ihrerseits erforderlich ist.


Überprüfung des OLED-Bildschirms
-----------------------------------

Nachdem du die ``pironman5``-Bibliothek installiert hast, zeigt der OLED-Bildschirm die CPU-Auslastung, RAM, Festplattennutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an und zeigt diese Informationen bei jedem Neustart an.

Wenn dein OLED-Bildschirm keine Inhalte anzeigt, überprüfe zunächst, ob das FPC-Kabel des OLED richtig angeschlossen ist.

Danach kannst du das Programmlog überprüfen, um zu sehen, was das Problem sein könnte, mit folgendem Befehl.

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

Oder überprüfe, ob die i2c-Adresse 0x3C des OLED erkannt wird:

.. code-block:: shell

  i2cdetect -y 1

Überprüfung des Infrarot-Empfängers
---------------------------------------



* Installiere das ``lirc``-Modul:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Teste nun den IR-Empfänger, indem du den folgenden Befehl ausführst.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Nachdem du den Befehl ausgeführt hast, drücke eine Taste auf der Fernbedienung, und der Code dieser Taste wird angezeigt.

