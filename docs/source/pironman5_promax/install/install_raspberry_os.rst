.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Instalación de Raspberry Pi OS
================================================================================

Puede elegir un método de instalación según si tiene disponible una tarjeta Micro SD o un SSD NVMe.

**Usar Solo una Tarjeta Micro SD**

  Si solo usa una tarjeta Micro SD, simplemente puede seguir el primer método a continuación.

**Usar un SSD M.2 NVMe**

  * Si tiene un **Adaptador de Carcasa para SSD M.2 NVMe**, puede conectar su SSD a su ordenador usando el adaptador y seguir el segundo método para instalar el SO.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center

  * Si no tiene el adaptador que se muestra arriba, puede instalar primero el SO en una tarjeta Micro SD usando el primer método, luego usar el tercer método para copiar el sistema de la tarjeta Micro SD a su SSD M.2 NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi