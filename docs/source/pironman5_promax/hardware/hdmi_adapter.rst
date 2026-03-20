.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



USB HDMIアダプター
==========================================

.. image:: img/hdmi_adapter.png

このUSB HDMIアダプターボードは、Raspberry Pi 5専用に設計されています。主な機能は、USBとHDMIの接続をRaspberry PiのUSBインターフェース側に合わせて配置し直し、アクセシビリティとケーブル管理を向上させることです。

さらに、HDMIポートは標準的なHDMI Type Aインターフェースに変換され、より幅広い互換性を提供します。

**NVMe追加電源**

このボードには、NVMe PIP電源供給用の5V電源ヘッダーが搭載されています。拡張ヘッダーと組み合わせることで、NVMeの追加電源インターフェースに接続し、追加電力を供給できます。

**1220RTCバッテリーホルダー**

RTCバッテリーを簡単に取り付けるための1220RTCバッテリーホルダーが組み込まれています。SH1.0 2Pリバースケーブルを介してRaspberry PiのRTCインターフェースに接続します。

バッテリーホルダーはCR1220とML1220の両方のバッテリーに対応しています。ML1220（リチウム二酸化マンガンバッテリー）を使用する場合、充電はRaspberry Pi上で直接設定できます。CR1220は充電式ではないことに注意してください。

**トリクル充電の有効化**

.. warning::

  CR1220バッテリーを使用している場合は、トリクル充電を有効にしないでください。バッテリーに回復不能な損傷を与え、ボードを損傷する恐れがあります。

デフォルトでは、バッテリーのトリクル充電機能は無効になっています。 ``sysfs`` ファイルは、現在のトリクル充電電圧と制限を示します：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

トリクル充電を有効にするには、 ``rtc_bbat_vchg`` を ``/boot/firmware/config.txt`` に追加します：

  * ``/boot/firmware/config.txt`` を開きます。
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * ``rtc_bbat_vchg`` を ``/boot/firmware/config.txt`` に追加します。
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
再起動後、システムには以下が表示されます：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

これにより、バッテリーがトリクル充電されていることが確認できます。この機能を無効にするには、 ``config.txt`` から ``dtparam`` 行を削除するだけです。



オーディオインターフェース
---------------------------------

このセクションでは、スピーカー出力やヘッドフォンジャックなど、ボードのオーディオ出力機能について説明します。

.. image:: img/hdmi_speaker_port.png

**スピーカーポート**

このボードには、2つの4Ω 3Wスピーカーをサポートするデュアルチャンネルスピーカー出力インターフェースが搭載されています。

**スピーカースイッチ**

スピーカーのオーディオ信号はHDMI0ソースから出力されます。HDMI0が内蔵スピーカー付きのディスプレイに接続されている場合、Pironman 5 Pro MAXのスピーカーとディスプレイのスピーカーの両方から音声が同時に再生される可能性があります。 **SPEAKER** ジャンパーを使用すると、この動作を制御できます。

*   ジャンパーを左側の2ピン（ **ON** ）に接続すると、スピーカーが **常に有効** になります。
*   ジャンパーを右側の2ピン（ **AUTO** ）に接続すると、ヘッドフォンが挿入されたとき、またはHDMI0が接続されたときにスピーカーが **自動的に無効化** されます。

したがって、HDMIディスプレイが接続されている状態でオンボードスピーカーを使用したい場合は、以下のいずれかを行います：

*   ディスプレイを **HDMI1** ポートに接続します。
*   **SPEAKER** ジャンパーを **ON** の位置に設定します。

**3.5mmオーディオジャック**

ヘッドフォンジャックはスピーカーと同じオーディオソースを共有しますが、 **増幅されていない** 信号を出力します。スイッチ付きジャックを使用しており、ヘッドフォンが挿入されると **スピーカーアンプを自動的に無効化** し、両方から同時に音声が再生されるのを防ぎます。

このジャックは4ピンTRRSコネクタですが、 **標準的なステレオオーディオ出力のみ** をサポートします：

*   **チップ (T):** 左チャンネル
*   **リング1 (R1):** 右チャンネル
*   **リング2 (R2):** グランド
*   **スリーブ (S):** グランド

この構成により、一般的な4ピンヘッドフォン規格との互換性が維持されます。