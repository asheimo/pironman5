.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_view_control_commands:

Control with Commands
========================================
In addition to viewing data from the Pironman 5 Pro MAX and controlling various devices through the Dashboard, you can also use commands to control them.

.. note::

  * For the **Home Assistant** system, you can only monitor and control the Pironman 5 Pro MAX through the dashboard by opening the webpage at ``http://<ip>:34001``.
 
.. * For the **Batocera.linux** system, you can only monitor and control the Pironman 5 Pro MAX via commands. It is important to note that any changes to the configuration require a restart of the service using ``pironman5 restart`` to take effect.

View the Basic Configurations
-----------------------------------

The ``pironman5`` module offers basic configurations for Pironman, which you can review with the following command.

.. code-block:: shell

  sudo pironman5 -c

The standard configurations appear as follows:

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

Customize these configurations to fit your needs.

Use ``pironman5`` or ``pironman5 -h`` for instructions.

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Pironman 5 Pro Max command line interface

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

  Each time you modify the status of ``pironman5.service``, you need to use the following command to make the configuration changes take effect.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Verify the ``pironman5`` program status using the ``systemctl`` tool.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Alternatively, inspect the program-generated log files.

  .. code-block:: shell

    ls /var/log/pironman5/


**Control RGB LEDs**
----------------------
The board features 18 WS2812B addressable RGB LEDs: 6 onboard and 12 integrated into the RGB fans. Users can control power, color, brightness, display modes, animation speed, and the number of active LEDs.

.. note::

  After modifying the configuration for ``pironman5.service``, you must restart the service for the changes to take effect:

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **Enable/Disable RGB LEDs**: Use ``true`` to turn on, ``false`` to turn off.

.. code-block:: shell

  sudo pironman5 -re true

* **Change Color**: Set a color using a hexadecimal value (without the `#`), e.g., ``fe1a1a`` for red.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* **Adjust Brightness**: Set brightness from 0% to 100%.

.. code-block:: shell

  sudo pironman5 -rb 75

* **Change Display Mode**: Choose from several animation modes:

  * ``solid``: Static color.
  * ``breathing``: Pulsing fade in/out.
  * ``flow`` / ``flow_reverse``: Color flows in one direction.
  * ``rainbow`` / ``rainbow_reverse``: Cycles through a rainbow spectrum.
  * ``hue_cycle``: Smoothly cycles through hue values.

.. code-block:: shell

  sudo pironman5 -rs breathing

.. note::

  When using ``rainbow``, ``rainbow_reverse``, or ``hue_cycle`` modes, the color set via ``pironman5 -rc`` will be overridden by the mode's automatic color cycle.

* **Adjust Animation Speed**: Control the speed of effects from 0% (slowest) to 100% (fastest).

.. code-block:: shell

  sudo pironman5 -rp 50

* **Set LED Count**: The system defaults to controlling 18 LEDs. If you have extended the chain with additional external WS2812B LEDs, update the total count accordingly.

.. code-block:: shell

  sudo pironman5 -rl 12



**Fan**
--------------------------------

These fans connects to a dedicated 4-pin PWM fan port on the Raspberry Pi 5. Its default control strategy is a firmware-managed, multi-level intelligent speed adjustment scheme based on CPU temperature. This means that when you use an official or compatible PWM fan and connect it correctly, the system will automatically adjust the fan speed according to changes in CPU temperature (starting to operate above 50°C) without any manual intervention from you.




**Check the OLED Screen**
-----------------------------------

The 0.96" OLED screen displays system information (CPU, RAM, Disk, Temp, IP) by default after installing the ``pironman5`` library and rebooting.

If the OLED screen is blank:

1.  Ensure the OLED's FPC cable is securely connected to the mainboard.
2.  Check the service log for errors:

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    Or check the specific OLED log:

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3.  Verify the OLED is detected on the I2C bus (address `0x3C`):

    .. code-block:: shell

      i2cdetect -y 1

**OLED Configuration Commands**

* **Enable/Disable OLED**: Turn the OLED display on or off.

    .. code-block:: shell

      sudo pironman5 -oe false

* **Rotate Display**: Set screen orientation to ``0`` (default) or ``180`` degrees.

    .. code-block:: shell

      sudo pironman5 -or 180

* **Configure Display Pages**: Choose which info pages to cycle through. Pages are: ``mix`` (overview), ``performance`` (detailed CPU/RAM), ``ips`` (network IPs), ``disk`` (storage). Separate multiple pages with commas.

    .. code-block:: shell

      sudo pironman5 -op mix,ips,disk

* **Set Sleep Timeout**: Define how many seconds of inactivity before the OLED turns off (0 = never sleep).

    .. code-block:: shell

      sudo pironman5 -os 120

**Check the Infrared Receiver**
---------------------------------------

The built-in IR receiver allows control via remote.

1.  Install the required software:

    .. code-block:: shell

      sudo apt-get install lirc -y

2.  Test the receiver. Run the following command, then point a remote at the case and press buttons. You should see raw code output.

    .. code-block:: shell

      mode2 -d /dev/lirc0

3.  To set up specific remote button mappings (e.g., for Kodi or Volumio), you will need to configure the `/etc/lirc/lircd.conf` file with your remote's codes.




**General System Commands**
----------------------------

* **Show Version**: Display the installed ``pironman5`` package version.

.. code-block:: shell

  sudo pironman5 -v

* **Show Current Configuration**: Display all current settings.

.. code-block:: shell

  sudo pironman5 -c

* **Set Temperature Unit**: Switch between Celsius (``C``) and Fahrenheit (``F``) for temperature displays.

.. code-block:: shell

  sudo pironman5 -u F

* **Configure Data Logging**:

  * **Set Database Retention Days**: Control how many days of historical data (like temperature logs) are kept.

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **Enable/Disable History Logging**: Turn data collection on or off.

    .. code-block:: shell

      sudo pironman5 -eh false

* **Set Logging Verbosity**: Adjust the detail level of system logs. Options: ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``.

.. code-block:: shell

  sudo pironman5 -dl DEBUG

* **Remove Web Dashboard**: Uninstall the optional web-based management interface.

.. code-block:: shell

  sudo pironman5 -rd

* **Specify Custom Config Path**: Use a configuration file from a non-standard location.

.. code-block:: shell

  sudo pironman5 -cp /home/pi/my_custom_config.json

**Service Management Subcommands**
-----------------------------------

* **Start the Pironman5 Service**: Manually start the background service that manages LEDs, fans, OLED, etc.

.. code-block:: shell

  sudo pironman5 start

* **Stop the Pironman5 Service**: Gracefully stop the background service.

.. code-block:: shell

  sudo pironman5 stop

* **Launch Web Dashboard in Browser**: If the web dashboard is installed, this command will open it in your default browser.

.. code-block:: shell

  sudo pironman5 launch-browser