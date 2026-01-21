.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!



Installing the OS on a Micro SD Card
=============================================

If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.


**Required Components**

* A Personal Computer
* A Micro SD card and Reader

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Install the OS to the microSD Card
------------------------------------------------


.. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>   


1. Download the latest version of the OS from the |shared_link_batocera_linux| website.

2. Insert your microSD card into your computer using a card reader.  
   Before proceeding, back up any important data on the card, as it will be erased.

   .. image:: img/insert_sd.png
      :width: 90%

3. When **Raspberry Pi Imager** opens, you will see the **Device** page.  
   Select your **Raspberry Pi 5** model from the list.

   .. image:: img/imager_device.png
      :width: 90%

4. Go to the **OS** section, scroll down to the bottom of the page, and select **Username custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

5. Choose the **batocera-bcmxxxxxxx.img.gz** file you just downloaded and click **Open**.

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. In the **Storage** section, select your microSD card.  
   For safety, it is recommended to unplug other USB storage devices so that only the microSD card appears in the list.

   .. image:: img/imager_storage.png
      :width: 90%

#. Click **NEXT** and go directly to **Writing**, where the OS is written to the microSD card.


   .. image:: img/imager_betocera_write.png
      :width: 90%

#. When the **“Write Successful”** popup appears, the image has been fully written and verified. You can now safely remove the microSD card and use it to boot your Raspberry Pi.

   .. image:: img/imager_betocera_finish.png
      :width: 90%
