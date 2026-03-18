Configuring Display
===================================================================

This chapter guides you through configuring the display settings for the Pironman 5 Pro MAX, including enabling power-saving screen blanking and setting up screen flipping to accommodate special installation orientations.


-------------------------------------------------------------------

**Setting Up Screen Idle Sleep**


To save power when you are not actively using the Pironman 5 Pro MAX, you can enable the screen's automatic sleep function. When the device has been idle for a set period, the main display will automatically turn off, entering a low-power state.

Follow these steps to configure it:

1. Click **Menu -> Preferences** in the bottom-left corner of the screen, then find and open the **Control Centre**.

   .. image:: img/flip_mode1.png

2.  In the Control Centre interface, click to enter the **Display** settings.

3.  Locate the **Screen Blanking** option and toggle it on.

   .. image:: img/flip_mode2.png



----------------------------------------------------------------------

**Flip the Pironman 5 Pro MAX**

The Pironman 5 Pro MAX can be flipped over for use. In this configuration, the touchscreen will be positioned on top and the GPIO ports will be on the bottom, offering greater flexibility for various projects. This setup is ideal for applications such as more convenient screen viewing or easier access to GPIO pins when connecting sensors.

When flipping the device, both displays need separate adjustment:

   * Main touchscreen – Requires OS-level rotation settings
   * OLED status screen – Requires command-line configuration

To flip the Pironman 5 Pro MAX, follow these steps:


1. Physical Preparation

   Remove the camera from the Pironman 5 Pro MAX, flip the entire unit over, and reinstall the camera. The installation should be symmetrical to its original orientation.

   .. image:: img/inverted_screen0.png

2. Touchscreen Orientation Setup

   Power on the device. On the touchscreen, long-press the desktop to bring up the menu and select **Desktop Preferences**.

   .. image:: img/inverted_screen1.png

   Scroll down to find the **Screens** option, then long-press the screen indicator in the display. Select **Orientation → Inverted**.

   .. image:: img/inverted_screen2.png

   Apply, the update window will show the screen, you need to click OK to confirm.

   .. image:: img/inverted_screen3.png

3. OLED Screen Configuration

   In the Terminal, run the following command to rotate the OLED 180 degrees:

   .. code-block:: bash

      sudo pironman5 -or 180

----------------------------------------------------

**Note**

- After flipping, ensure the unit is placed on a stable surface to prevent tipping.
- If you encounter touch input misalignment, recalibrate the touchscreen through system settings.
- For advanced display adjustments, refer to the :ref:`promax_view_control_commands` section for additional commands related to OLED and screen rotation.
