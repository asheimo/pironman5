.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

IO-Expander
================

.. image:: img/io_board.png


RGB-LEDs
------------

.. image:: img/io_board_rgb.png

Die Platine verfügt über 18 adressierbare WS2812B-RGB-LEDs: 6 auf der Platine und 12 in die RGB-Lüfter integriert.  Benutzer können sie ein- oder ausschalten, die Farbe ändern, die Helligkeit anpassen, die Anzeigemodi wechseln und die Geschwindigkeit der Änderungen einstellen.






RGB-Steuerungspin
-------------------------

Die RGB-LED wird über SPI angesteuert und ist mit **GPIO10** verbunden, dem SPI-MOSI-Pin. Die beiden gezeigten Pins werden verwendet, um die RGB-LED mit GPIO10 zu verbinden. Wenn nicht benötigt, kann der Jumper entfernt werden.

  .. image:: img/io_board_rgb_pin.png

RGB-Ausgangspins
-------------------------

.. image:: img/io_board_rgb_out.png

Die WS2812-RGB-LEDs unterstützen eine serielle Verbindung, was den Anschluss eines externen RGB-LED-Streifens ermöglicht. Verbinden Sie den **SIG**-Pin mit dem **DIN**-Pin des externen Streifens zur Erweiterung.

Die Platine verfügt über 18 adressierbare WS2812B-RGB-LEDs: 6 auf der Platine und 12 in die RGB-Lüfter integriert. Schließen Sie zusätzliche LEDs an und aktualisieren Sie die Anzahl mit:

.. code-block:: shell

  sudo pironman5 --rgb-led-count [Anzahl]

Beispiel:

.. code-block:: shell

  sudo pironman5 --rgb-led-count 24



OLED-Bildschirmanschluss
----------------------------

Der OLED-Bildschirmanschluss mit der Adresse 0x3C ist ein Hauptmerkmal.

.. image:: img/io_board_oled.png

Wenn der OLED-Bildschirm nichts anzeigt oder falsch anzeigt, können Sie die folgenden Schritte zur Fehlerbehebung ausführen:

Überprüfen Sie, ob das FPC-Kabel des OLED-Bildschirms richtig angeschlossen ist.

#. Verwenden Sie den folgenden Befehl, um die Laufprotokolle des Programms anzuzeigen und auf Fehlermeldungen zu prüfen.

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. Alternativ können Sie mit dem folgenden Befehl prüfen, ob die i2c-Adresse 0x3C des OLEDs erkannt wird:

    .. code-block:: shell

        sudo i2cdetect -y 1

#. Wenn die ersten beiden Schritte keine Probleme ergeben, versuchen Sie, den pironman5-Dienst neu zu starten, um zu sehen, ob das Problem dadurch behoben wird.

    .. code-block:: shell

        sudo systemctl restart pironman5.service



Infrarotempfänger
---------------------------

.. image:: img/io_board_receiver.png

* **Modell**: IRM-56384, arbeitet bei 38KHz.
* **Verbindung**: Der IR-Empfänger ist mit **GPIO13** verbunden.
* **D7**: Eine Infrarot-Empfangsanzeige, die bei Signalerfassung blinkt.
* **J6**: Ein Pin zur Aktivierung der Infrarotfunktion. Standardmäßig ist eine Jumperkappe aufgesteckt, um die Funktion sofort nutzen zu können. Entfernen Sie die Kappe, um GPIO13 freizugeben, wenn der IR-Empfänger nicht verwendet wird.

Um den IR-Empfänger zu nutzen, überprüfen Sie die Verbindung und installieren Sie das erforderliche Modul:

* Verbindung testen:

  .. code-block:: shell

    sudo ls /dev |grep lirc

* Das Modul ``lirc`` installieren:

  .. code-block:: shell

    sudo apt-get install lirc -y

* Testen Sie nun den IR-Empfänger, indem Sie den folgenden Befehl ausführen.

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Drücken Sie nach Ausführung des Befehls eine Taste auf der Fernbedienung, und der Code dieser Taste wird ausgegeben.


RGB-Lüfter-Pins
---------------

.. image:: img/io_board_pin_fan.png

Die IO-Erweiterungsplatine unterstützt bis zu drei 5V-PWM-Lüfter. Alle Lüfter werden gemeinsam gesteuert.

Das Lüftersteuersignal wird an den **FAN IN**-Anschluss auf der IO-Erweiterungsplatine angeschlossen und dann über die drei dedizierten Lüfteranschlüsse ausgegeben. Diese Anschlüsse sind von oben nach unten als **REAR UPPER**, **REAR LOWER** und **CPU FAN** beschriftet. Bitte schließen Sie sie gemäß dem Siebdruck an, da dies sonst die RGB-Steuerung am Lüfter beeinträchtigt.

Stiftleisten
--------------

.. image:: img/io_board_pin_header.png

Zwei rechtwinklige Stiftleisten führen die GPIOs des Raspberry Pi heraus. Beachten Sie jedoch, dass der IR-Empfänger, die RGB-LEDs und die Lüfter einige Pins belegen. Entfernen Sie die entsprechenden Jumperkappen, um diese Pins für andere Funktionen zu nutzen.

.. list-table::
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 MAX
    - Raspberry Pi 5
  * - IR-Empfänger (Optional)
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - Lüfter (Optional)
    - GPIO6
  * - FLED (Optional)
    - GPIO5
  * - RGB (Optional)
    - GPIO10