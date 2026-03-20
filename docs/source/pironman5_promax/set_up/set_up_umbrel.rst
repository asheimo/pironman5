.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _set_up_umbrel_promax:

Setting Up on Umbrel OS
======================================================================

If you have installed Umbrel OS on your Raspberry Pi 5, you will need to configure the Pironman 5 Pro MAX using the command line. Detailed instructions are provided below:

#. Connect your Raspberry Pi 5 to your network using an Ethernet cable. This step is essential to ensure that your Raspberry Pi has internet access.

#. In your browser, visit: ``http://umbrel.local``. If the page does not open, check your router for the Umbrel device’s IP address, for example: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Create your Umbrel account by setting a username and password. This password will be used for future remote access to Umbrel, so make sure to remember it.

   .. image:: img/umbrel_account.png

#. Click **Next** to complete the Umbrel setup and enter the desktop environment.

   .. image:: img/umbrel_desktop.png

#. Open the Terminal. From the desktop, click the **Settings** icon, then select **Advanced Settings** and click **Open**.

   .. image:: img/umbrel_setting.png

#. Click **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. You can choose to open the Terminal in Umbrel OS or within a specific app. Either option will take you to the Terminal interface.

   .. image:: img/umbrel_terminal.png

#. Proceed to download the code from GitHub and install the ``pironman5`` module.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. After the installation is complete, enter the following command to reboot your Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5 Pro MAX:
   
   * The OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address.
   * Four WS2812 RGB LEDs will light up in blue with a breathing mode.


#. You can use the ``systemctl`` tool to ``start``, ``stop``, ``restart``, or check the ``status`` of ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Use this command to apply any changes made to the settings of pironman 5 Pro MAX.
   * ``start/stop``: Enable or disable the ``pironman5.service``.
   * ``status``: Check the operational status of the ``pironman5`` program using the ``systemctl`` tool.

.. note::

   At this point, you have successfully set up the Pironman 5 Pro MAX, and it is ready to use.
   
   For advanced control of its components, please refer to :ref:`control_commands_dashboard_promax`.



