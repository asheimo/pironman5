.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_pi_os:

Raspberry Pi/Ubuntu/Kali/Homebridge OSでの設定
==================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Raspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをRaspberry Piにインストールした場合は、コマンドラインを使用してPironman 5 Pro MAXを設定する必要があります。詳細なチュートリアルは以下をご覧ください：

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、Raspberry Pi公式ウェブサイト |link_rpi_get_start| にアクセスしてください。


シャットダウン時のGPIO電源無効化設定
------------------------------------------------------------

Raspberry Pi GPIOから電源供給を受けるOLED画面やRGBファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を無効化するようにRaspberry Piを設定することが重要です。

#. EEPROM設定ツールを開きます：

   .. code-block::

      sudo raspi-config

#. **Advanced Options → A12 Shutdown Behaviour** に移動します。

   .. image:: img/shutdown_behaviour.png

#. **B1 Full Power Off** を選択します。

   .. image:: img/run_power_off.png

#. 変更を保存します。新しい設定を有効にするために再起動を促すプロンプトが表示されます。


.. _promax_download_pironman5_module:

``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

.. note::

   Liteシステムの場合、最初に ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールします。
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHubからコードをダウンロードし、 ``pironman5`` モジュールをインストールします。

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   インストールが成功したら、インストールを有効化するためにシステムの再起動が必要です。画面の再起動プロンプトに従ってください。

   再起動すると、 ``pironman5.service`` が自動的に起動します。Pironman 5 Pro MAXの主な設定は以下の通りです：
   
   * OLED画面には、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色でブリージングモードに点灯します。

#. ``systemctl`` ツールを使用して、 ``pironman5.service`` の ``start``、 ``stop``、 ``restart``、または ``status`` の確認ができます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``： Pironman 5 Pro MAXの設定に変更を加えた場合に、このコマンドを使用して適用します。
   * ``start/stop``： ``pironman5.service`` を有効化または無効化します。
   * ``status``： ``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   この時点で、Pironman 5 Pro MAXのセットアップは正常に完了し、使用可能な状態になりました。
   
   コンポーネントの高度な制御については、 :ref:`control_commands_dashboard_promax` を参照してください。