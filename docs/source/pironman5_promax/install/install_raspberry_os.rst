.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Raspberry Pi OS installieren
================================================================================

Sie können je nach Verfügbarkeit einer Micro-SD-Karte oder einer NVMe-SSD eine Installationsmethode wählen.

**Nur mit einer Micro-SD-Karte**

  Wenn Sie nur eine Micro-SD-Karte verwenden, können Sie einfach der ersten Methode unten folgen.

**Mit einer M.2-NVMe-SSD**

  * Wenn Sie einen **M.2-NVMe-SSD-Gehäuseadapter** besitzen, können Sie Ihre SSD mit dem Adapter an Ihren Computer anschließen und der zweiten Methode folgen, um das Betriebssystem zu installieren.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center

  * Wenn Sie den oben gezeigten Adapter nicht haben, können Sie das Betriebssystem zunächst mit der ersten Methode auf einer Micro-SD-Karte installieren und dann mit der dritten Methode das System von der Micro-SD-Karte auf Ihre M.2-NVMe-SSD kopieren.

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi