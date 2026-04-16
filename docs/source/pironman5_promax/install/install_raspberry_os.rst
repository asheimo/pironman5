.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Installazione di Raspberry Pi OS
================================================================================

Puoi scegliere un metodo di installazione in base al fatto che tu abbia disponibile una scheda Micro SD o un SSD NVMe.

**Utilizzare Solo una Scheda Micro SD**

  Se stai utilizzando solo una scheda Micro SD, puoi semplicemente seguire il primo metodo qui sotto.

**Utilizzare un SSD M.2 NVMe**

  * Se disponi di un **Adattatore per Enclosure M.2 NVMe**, puoi collegare il tuo SSD al computer usando l'adattatore e seguire il secondo metodo per installare il sistema operativo.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center

  * Se non disponi dell'adattatore mostrato sopra, puoi prima installare il sistema operativo su una scheda Micro SD usando il primo metodo, quindi usare il terzo metodo per copiare il sistema dalla scheda Micro SD al tuo SSD M.2 NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi