
.. start_compatible_nvme_ssd

兼容的 NVMe SSD
========================

**推荐（稳定）**

以下 SSD 型号已经过测试，通常在 Raspberry Pi 5 和 Pironman NVMe 配置中表现稳定。

*   ADATA Legend 700
*   ADATA Legend 800
*   AData XPG SX8200 Pro
*   Axe Memory Generic Drive
*   Inland PCIe NVMe SSD
*   KIOXIA EXCERIA NVMe SSD
*   KIOXIA EXCERIA G2 NVMe SSD
*   Kingston KC3000
*   Kingston NV2
*   Lexar NM710
*   Lexar NM620
*   Netac NV3000 NVMe SSD
*   Netac NV2000 NVMe SSD
*   Origin Inception TLC830 Pro NVMe SSD
*   Ortial ON-750-128 NVME SSD
*   Pineberry Pi Pinedrive (2280)
*   PNY CS1030
*   Sabrent Rocket 4.0
*   Sabrent Rocket Nano
*   Samsung 970 EVO Plus
*   Samsung 980
*   Samsung 980 Pro
*   Samsung 990 Pro
*   TeamGroup MP33
*   Western Digital SN570
*   Western Digital SN530
*   Western Digital Black SN750 SE
*   Western Digital Blue SN550 系列 （如果您知道如何安装最新的 rpi-eeprom-updates，pieeprom-2024-01-24.bin 修复了 Western Digital Blue SN550 的 nvme 启动问题，请参考 https://forums.raspberrypi.com/viewtopic.php?t=364327。）
*   XPG GAMMIX S70 BLADE
*   XPG SX8200 Pro

**兼容（可能因人而异）**

这些型号在许多设置中可能正常工作，但部分用户报告称，根据工作负载或系统配置的不同，偶尔会遇到兼容性或稳定性差异。

*   Crucial P2 M.2
*   Crucial P3 M.2

**不推荐（潜在不稳定）**

这些型号或其控制器可能会在 Raspberry Pi 5 PCIe 接口上导致 NVMe 重置、I/O 错误或驱动器断开连接，因此不建议使用。

*   使用 Phison E27T / E21 控制器的 SSD
*   Crucial P310
*   Crucial P3 Plus M.2
*   Western Digital SN740
*   Western Digital Black SN770
*   WD Blue SN580 系列
*   Western Digital Green SN350 系列
*   Western Digital Black SN850 系列
*   WD BLACK 8TB SN850X
*   Inland tn446 nvme 驱动器
*   Corsair MP600 SSD
*   Samsung PM991
*   Kingston OM8SEP4256Q-A0
*   Transcend 110Q (TS500GMTE110Q)
*   其他配备相同 Phison 控制器的 NVMe 固态硬盘

.. end_compatible_nvme_ssd