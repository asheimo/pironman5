.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Instalación de Umbrel OS
============================================

Umbrel es una plataforma/sistema operativo de servidor doméstico autoalojado de código abierto que le permite ejecutar su propio nodo Bitcoin, instalar una variedad de aplicaciones autoalojadas con un solo clic y convertir su hardware en su nube personal doméstica. Es una excelente manera de comenzar con la autocustodia y la privacidad.

**Componentes Requeridos**

* Una Computadora Personal
* Un SSD NVMe
* Un adaptador de NVMe a USB
* Tarjeta Micro SD y Lector

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Instalar el SO en el SSD NVMe
-----------------------------------

Ahora está listo para instalar el sistema operativo en su **SSD NVMe**.
Simplemente siga los pasos a continuación con cuidado — esta guía está escrita para principiantes y es fácil de seguir.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. Descargue la última imagen de **Umbrel OS** y extraiga el archivo. Si desea usar una versión específica, también puede visitar la página de |link_umbrel_release|.

   * :download:`Imagen más reciente de Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Inserte el **SSD NVMe** en su ordenador usando un **adaptador de NVMe a USB**.

#. Abra **Raspberry Pi Imager**. En la pantalla **Device**, seleccione su modelo de **Raspberry Pi 5** de la lista.

   .. image:: img/imager_device.png
      :width: 90%

#. Vaya a la sección **OS**, desplácese hacia abajo y seleccione **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Seleccione el **archivo de imagen de Umbrel OS** que descargó y extrajo anteriormente, luego haga clic en **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Haga clic en **Next** para continuar.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. En la sección **Storage**, seleccione su **SSD NVMe**. Asegúrese de elegir el SSD NVMe y no otra unidad en su ordenador.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Revise todas las configuraciones cuidadosamente, luego haga clic en **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Si el SSD NVMe ya contiene datos, Raspberry Pi Imager le advertirá que todos los datos serán borrados. Verifique que la unidad correcta esté seleccionada, luego haga clic en **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Cuando aparezca el mensaje **“Write Complete”**, la imagen ha sido escrita y verificada exitosamente.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%