.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. start_compatible_nvme_ssd

**SSD NVMe compatibles**
========================

**Recomendados (Estables)**

Estos modelos de SSD han sido probados y son generalmente estables con Raspberry Pi 5 y configuraciones NVMe de Pironman.

* ADATA Legend 700
* ADATA Legend 800
* AData XPG SX8200 Pro

* Axe Memory Generic Drive

* Inland PCIe NVMe SSD

* KIOXIA EXCERIA NVMe SSD
* KIOXIA EXCERIA G2 NVMe SSD

* Kingston KC3000
* Kingston NV2

* Lexar NM710
* Lexar NM620

* Netac NV3000 NVMe SSD
* Netac NV2000 NVMe SSD

* Origin Inception TLC830 Pro NVMe SSD
* Ortial ON-750-128 NVME SSD

* Pineberry Pi Pinedrive (2280)

* PNY CS1030

* Sabrent Rocket 4.0
* Sabrent Rocket Nano

* Samsung 970 EVO Plus
* Samsung 980
* Samsung 980 Pro
* Samsung 990 Pro

* TeamGroup MP33

* Western Digital SN570
* Western Digital SN530
* Western Digital Black SN750 SE
* Western Digital Blue SN550 series (Si sabe cómo instalar las últimas actualizaciones de rpi-eeprom, pieeprom-2024-01-24.bin solucionó el problema de arranque nvme de Western Digital Blue SN550. Consulte https://forums.raspberrypi.com/viewtopic.php?t=364327.)

* XPG GAMMIX S70 BLADE
* XPG SX8200 Pro


**Compatibles (Pueden Variar)**

Estos modelos pueden funcionar correctamente en muchas configuraciones, pero algunos usuarios han informado diferencias ocasionales de compatibilidad o estabilidad dependiendo de la carga de trabajo o la configuración del sistema.

* Crucial P2 M.2
* Crucial P3 M.2



**No Recomendados (Inestabilidad Potencial)**

Estos modelos o controladores pueden causar restablecimientos de NVMe, errores de E/S o desconexiones de la unidad en las interfaces PCIe de Raspberry Pi 5, por lo que no se recomiendan.

* SSD que utilizan controladores Phison E27T / E21
* Crucial P310
* Crucial P3 Plus M.2
* Western Digital SN740
* Western Digital Black SN770
* WD Blue SN580 series
* Western Digital Green SN350 series
* Western Digital Black SN850 series
* WD BLACK 8TB SN850X
* Inland tn446 nvme drive
* Corsair MP600 SSD
* Samsung PM991
* Kingston OM8SEP4256Q-A0
* Transcend 110Q (TS500GMTE110Q)
* Otras unidades SSD NVMe equipadas con el mismo controlador Phison

.. end_compatible_nvme_ssd