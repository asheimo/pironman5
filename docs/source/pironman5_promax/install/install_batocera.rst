.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Instalación del SO Batocera
=============================================

Siga el tutorial a continuación para instalar el sistema en su tarjeta Micro SD.

**Componentes Requeridos**

* Una Computadora Personal
* Una tarjeta Micro SD y un lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el SO en la tarjeta microSD
------------------------------------------------

.. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>

1. Descargue la última versión del SO desde el sitio web de |shared_link_batocera_linux|.

2. Inserte su tarjeta microSD en su ordenador usando un lector de tarjetas.
   Antes de continuar, respalde cualquier dato importante en la tarjeta, ya que será borrada.

   .. image:: img/insert_sd.png
      :width: 90%

3. Cuando se abra **Raspberry Pi Imager**, verá la página **Device**.
   Seleccione su modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

4. Vaya a la sección **OS**, desplácese hacia abajo hasta el final de la página y seleccione **Username custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

5. Elija el archivo **batocera-bcmxxxxxxx.img.gz** que acaba de descargar y haga clic en **Open**.

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. En la sección **Storage**, seleccione su tarjeta microSD.
   Por seguridad, se recomienda desconectar otros dispositivos de almacenamiento USB para que solo aparezca la tarjeta microSD en la lista.

   .. image:: img/imager_storage.png
      :width: 90%

#. Haga clic en **NEXT** y vaya directamente a **Writing**, donde el SO se escribe en la tarjeta microSD.

   .. image:: img/imager_betocera_write.png
      :width: 90%

#. Cuando aparezca la ventana emergente **“Write Successful”**, la imagen ha sido completamente escrita y verificada. Ahora puede retirar la tarjeta microSD de forma segura y usarla para arrancar su Raspberry Pi.

   .. image:: img/imager_betocera_finish.png
      :width: 90%