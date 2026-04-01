.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============

1. 対応システムについて
-------------------------------

Raspberry Pi 5でテストに合格したシステム：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 電源ボタンについて
--------------------------

電源ボタンはRaspberry Pi 5の電源ボタンを引き出したもので、Raspberry Pi 5の電源ボタンと同様に機能します。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * **Raspberry Pi OS Desktop** システムを実行している場合は、電源ボタンを素早く2回押すとシャットダウンします。
  * **Raspberry Pi OS Lite** システムを実行している場合は、電源ボタンを1回押すとシャットダウンが開始されます。
  * 強制的なハードシャットダウンを行うには、電源ボタンを長押しします。

* **電源オン**

  * Raspberry Piボードがシャットダウンしているが、電源が供給されている状態の場合、シャットダウン状態から電源を入れるには1回押します。

* シャットダウンボタンをサポートしていないシステムを実行している場合は、5秒間長押しすると強制的にハードシャットダウンし、シャットダウン状態から1回押すと電源が入ります。

3. Raspberry Pi AI HAT+について
----------------------------------------------------------

Raspberry Pi AI HAT+はPironman 5と互換性がありません。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI Kitは、Raspberry Pi M.2 HAT+とHailo AIアクセラレーターモジュールを組み合わせたものです。

   .. image::  img/output2.jpg
        :width: 400

Raspberry Pi AI KitからHailo AIアクセラレーターモジュールを取り外し、Pironman 5 MAXのNVMe PIPモジュールに直接挿入できます。

   .. .. image::  img/output4.png
   ..      :width: 800

4. タワークーラーの銅管の端について
----------------------------------------------------------

タワークーラーの上部にあるU字型ヒートパイプは、銅管がアルミフィンを通過しやすくするために圧縮されています。これは銅管の通常の製造工程の一部です。

   .. image::  img/tower_cooler1.png

5. PI5が起動しない（赤色LED）？
-------------------------------------------

この問題は、システムアップデート、起動順序の変更、またはブートローダーの破損によって発生する可能性があります。以下の手順を試して問題を解決してください：

#. USB-HDMIアダプターの接続を確認

   * USB-HDMIアダプターがPI5にしっかりと接続されているかを慎重に確認してください。
   * USB-HDMIアダプターを抜き差ししてみてください。
   * その後、電源を再接続し、PI5が正常に起動するか確認してください。

#. ケースの外でPI5をテスト

   * アダプターの再接続で問題が解決しない場合：
   * PI5をPironman 5ケースから取り外します。
   * 電源アダプターをPI5に直接接続します（ケースを介さずに）。
   * 正常に起動できるか確認してください。

#. ブートローダーの復元

   * PI5がまだ起動できない場合、ブートローダーが破損している可能性があります。こちらのガイドに従ってください： :ref:`update_bootloader_promax` で、SDカードまたはNVMe/USBから起動するかを選択します。
   * 準備したSDカードをPI5に挿入し、電源を入れて少なくとも10秒間待ちます。リカバリが完了したら、SDカードを取り外してフォーマットします。
   * その後、Raspberry Pi Imagerを使用して最新のRaspberry Pi OSを書き込み、カードを再挿入して起動を試みます。

6. OLED画面が動作しない？
------------------------------


OLED画面が表示されない、または正しく表示されない場合は、以下のトラブルシューティング手順に従ってください：

1. **OLED画面の接続を確認**

   OLED画面のFPCケーブルが正しく接続されていることを確認します。

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Oled-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

   .. todo 更新MP4

2. **OSの互換性を確認**

   Raspberry Piで互換性のあるオペレーティングシステムを実行していることを確認してください。

3. **I2Cアドレスを確認**

   以下のコマンドを実行して、OLEDのI2Cアドレス（0x3C）が認識されているか確認します：

   .. code-block:: shell

      sudo i2cdetect -y 1

   アドレスが検出されない場合は、以下のコマンドでI2Cを有効にします：

   .. code-block:: shell

      sudo raspi-config

4. **pironman5サービスを再起動**

   `pironman5` サービスを再起動して問題が解決するか確認します：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **ログファイルを確認**

   問題が続く場合は、ログファイルでエラーメッセージを確認し、情報をカスタマーサポートに提供してさらなる分析を依頼してください：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

7. NVMe PIPモジュールが動作しない？
---------------------------------------

1. NVMe PIPモジュールとRaspberry Pi 5を接続するFPCケーブルがしっかりと取り付けられていることを確認します。

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

.. todo 更新MP4

2. SSDがNVMe PIPモジュールに正しく固定されていることを確認します。

3. NVMe PIPモジュールのLEDの状態を確認します：

   すべての接続を確認した後、Pironman 5 MAXの電源を入れ、NVMe PIPモジュールの2つのインジケーターを観察します：

   * **PWR LED**: 点灯している必要があります。
   * **STA LED**: 正常動作を示すために点滅する必要があります。

   .. image:: img/dual_nvme_pip_leds.png  

   * **PWR LED** が点灯しているが **STA LED** が点滅していない場合、NVMe SSDがRaspberry Piに認識されていないことを示します。
   * **PWR LED** が消灯している場合は、モジュールの「Force Enable」ピンを短絡します。**PWR LED** が点灯した場合、FPCケーブルの緩みまたはNVMeに対応していないシステム構成の可能性があります。

   .. image:: img/dual_nvme_pip_j4.png  

     
4. NVMe SSDにオペレーティングシステムが正しくインストールされていることを確認します。参照： :ref:`install_the_os_promax`.

5. 配線が正しく、OSがインストールされているにもかかわらずNVMe SSDが起動しない場合は、Micro SDカードから起動して他のコンポーネントの機能を確認します。確認後、 :ref:`configure_boot_ssd_promax` に進みます。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com までメールをお送りください。できるだけ早く対応いたします。

8. RGB LEDが動作しない？
--------------------------

#. IO ExpanderのJ9上の2つのピンは、RGB LEDをGPIO10に接続するために使用されます。これらの2つのピンのジャンパーキャップが正しく装着されていることを確認します。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Raspberry Piが互換性のあるオペレーティングシステムを実行していることを確認します。Pironman 5は以下のOSバージョンのみをサポートしています：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   サポートされていないOSをインストールしている場合は、ガイドに従って互換性のあるオペレーティングシステムをインストールしてください： :ref:`install_the_os_promax`.

#. コマンド ``sudo raspi-config`` を実行して設定メニューを開きます。**3 Interfacing Options** -> **I3 SPI** -> **YES** に移動し、 **OK** と **Finish** をクリックしてSPIを有効にします。SPIを有効にした後、Pironman 5を再起動します。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com までメールをお送りください。できるだけ早く対応いたします。

.. _promax_fan_faq:

9. ファンが動作しない／制御できない場合
----------------------------------------------

Pro / MAX は、公式の Raspberry Pi PWM ファン制御ソリューションを採用しています。3 つの冷却ファンはすべて Raspberry Pi システムによって直接制御されており、pironman5 サービスに依存していません（そのため、コマンドラインツールやダッシュボードにはファン制御オプションは表示されません）。

**ファンが正常に動作するかどうかのテスト**

以下のコマンドを使用して、ファンを手動で制御できます。

.. code-block:: bash

   pinctrl FAN_PWM op dl   # ファン有効（ローアクティブ）
   pinctrl FAN_PWM op dh   # ファン無効（ハイアクティブ）
   pinctrl FAN_PWM a0      # 自動モード（システム温度制御）

**温度に基づくファン速度制御**

PWMファンは、Raspberry Pi 5の温度に応じて動的に速度を調整します：

* **50°C未満**: ファンはオフ（速度0%）。
* **50°C**: ファンは低速で動作（速度30%）。
* **60°C**: ファンは中速に増加（速度50%）。
* **67.5°C**: ファンは高速に増加（速度70%）。
* **75°C以上**: ファンは全速で動作（速度100%）。


10. OLED画面を起動するには？
---------------------------------------------------------------------------------

省電力と画面の寿命を延ばすため、OLED画面は一定時間操作がないと自動的にオフになります。これは通常の設計であり、製品の機能に影響を与えるものではありません。


.. note::

   OLED画面の設定（オン/オフ、スリープ時間、回転など）については、以下を参照してください： :ref:`promax_view_control_dashboard` または :ref:`promax_view_control_commands`.

11. Webダッシュボードを無効にするには？
------------------------------------------------------

``pironman5`` モジュールのインストールが完了すると、 :ref:`promax_view_control_dashboard` にアクセスできるようになります。

この機能が不要で、CPUとRAMの使用量を削減したい場合は、 ``pironman5`` のインストール時に ``--disable-dashboard`` フラグを追加してダッシュボードを無効にできます。

.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
既に ``pironman5`` をインストールしている場合は、 ``dashboard`` モジュールと ``influxdb`` を削除し、pironman5を再起動して変更を適用できます：
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. Pironman 5 MAXはレトロゲーミングシステムをサポートしていますか？
.. ------------------------------------------------------
.. はい、互換性があります。ただし、ほとんどのレトロゲーミングシステムは、追加ソフトウェアをインストールして実行できない簡素化されたバージョンです。この制限により、OLEDディスプレイ、2つのRGBファン、4つのRGB LEDなど、Pironman 5 MAXの一部のコンポーネントが正しく機能しない場合があります。これらのコンポーネントはPironman 5 MAXのソフトウェアパッケージのインストールを必要とするためです。


.. .. note::

..     Batocera.linuxシステムは現在、Pironman 5 MAXと完全に互換性があります。Batocera.linuxはオープンソースで完全に無料のレトロゲーミングディストリビューションです。

..     * :ref:`promax_install_batocera`
..     * :ref:`promax_set_up_batocera`

12. ``pironman5`` コマンドを使用してコンポーネントを制御する方法
----------------------------------------------------------------------
以下のチュートリアルを参照して、 ``pironman5`` コマンドを使用してPironman 5 MAXのコンポーネントを制御できます。

* :ref:`promax_view_control_commands`

13. コマンドを使用してRaspberry Piの起動順序を変更する方法
-------------------------------------------------------------

既にRaspberry Piにログインしている場合は、コマンドを使用して起動順序を変更できます。詳細な手順は以下の通りです：

* :ref:`configure_boot_ssd_promax`


14. Raspberry Pi Imagerで起動順序を変更する方法
---------------------------------------------------------------

EEPROM設定で ``BOOT_ORDER`` を変更するだけでなく、 **Raspberry Pi Imager** を使用してRaspberry Piの起動順序を変更することもできます。

この手順では予備のカードを使用することをお勧めします。

* :ref:`update_bootloader_promax`

15. SDカードからNVMe SSDにシステムをコピーする方法
-------------------------------------------------------------

NVMe SSDはあるが、NVMeをコンピューターに接続するアダプターがない場合は、最初にMicro SDカードにシステムをインストールします。Pironman 5 MAXが正常に起動した後、Micro SDカードからNVMe SSDにシステムをコピーできます。詳細な手順は以下の通りです：


* :ref:`copy_sd_to_nvme_promax`

16. アクリル板の保護フィルムの剥がし方
-----------------------------------------------------------------

パッケージには2枚のアクリルパネルが含まれており、どちらも傷を防ぐために両面に黄色/透明の保護フィルムが貼られています。保護フィルムは少し剥がしにくい場合があります。ドライバーを使用して角をそっとこすり、全体のフィルムを慎重に剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _promax_openssh_powershell:

17. Powershell経由でOpenSSHをインストールする方法
--------------------------------------------------

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）を使用してRaspberry Piに接続しようとすると、以下のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、お使いのコンピューターシステムが古く、`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ がプリインストールされていないことを意味します。以下のチュートリアルに従って手動でインストールする必要があります。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. 以下のコマンドを使用して ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、以下の出力が返されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 以下のコマンドを使用してインストールを確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これで ``OpenSSH.Client`` が正常にインストールされたことが表示されます。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        上記のプロンプトが表示されない場合は、Windowsシステムがまだ古すぎることを意味します。その場合は、|link_putty| などのサードパーティ製SSHツールをインストールすることをお勧めします。

#. PowerShellを再起動し、引き続き管理者として実行します。この時点で、 ``ssh`` コマンドを使用してRaspberry Piにログインできるようになります。ここで、以前に設定したパスワードの入力を求められます。

   .. image:: img/powershell_login.png


18. OMVを設定した場合、Pironman5の機能は引き続き使用できますか？
--------------------------------------------------------------------------------------------------------

はい、OpenMediaVaultはRaspberry Piシステム上で設定されます。 :ref:`promax_set_up_pi_os` の手順に従って設定を続行してください。