.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に情熱を注ぐ仲間たちとともに、より深く学び、創造しましょう。

    **参加するメリット**

    - **専門サポート**：購入後の技術的な問題を、コミュニティとチームが協力してサポートします。
    - **学びと共有**：チュートリアルやヒントを交換し、スキルを高めましょう。
    - **新製品の先行プレビュー**：開発中の製品や情報をいち早く入手。
    - **限定割引**：最新製品を対象とした特別割引を提供。
    - **キャンペーン & プレゼント企画**：イベントやプレゼントに参加できます。

    👉 私たちと一緒に創造と探求の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_view_control_commands:

コマンドによる制御
========================================

ダッシュボードを使って Pironman 5 MAX の各種デバイスを操作するだけでなく、コマンドでも制御できます。

.. note::

  * **Home Assistant** システムでは、 ``http://<ip>:34001`` にアクセスしてダッシュボードからのみ制御・監視が可能です。

.. * **Batocera.linux** システムでは、コマンドからのみ操作が可能です。構成を変更した場合は ``pironman5 restart`` によるサービスの再起動が必要です。

基本設定の確認
-----------------------------------

``pironman5`` モジュールには、以下のコマンドで確認できる基本設定が含まれています。

.. code-block:: shell

  sudo pironman5 -c

標準設定の例：

.. code-block:: 

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

必要に応じて、これらの設定をカスタマイズしてください。

``pironman5`` または ``pironman5 -h`` を実行すると、使用方法が表示されます。

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]     
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]]
                          [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]] [-vp [VIBRATION_SWITCH_PIN]]
                          [-vu [VIBRATION_SWITCH_PULL_UP]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop}]

  Pironman 5 MAX command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin
    -oe [OLED_ENABLE], --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -od [OLED_DISK], --oled-disk [OLED_DISK]
                          Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme
    -oi [OLED_NETWORK_INTERFACE], --oled-network-interface [OLED_NETWORK_INTERFACE]
                          Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or      
                          wlan0
    -or [{0,180}], --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -vp [VIBRATION_SWITCH_PIN], --vibration-switch-pin [VIBRATION_SWITCH_PIN]
                          Vibration switch pin
    -vu [VIBRATION_SWITCH_PULL_UP], --vibration-switch-pull-up [VIBRATION_SWITCH_PULL_UP]
                          Vibration switch pull up True/False
    -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds



.. note::

  ``pironman5.service`` の状態を変更した後は、次のコマンドで設定を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``systemctl`` で ``pironman5`` のステータスを確認：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* または、ログファイルを確認：

  .. code-block:: shell

    ls /var/log/pironman5/


RGB LED の制御
----------------------
ボードにはカスタマイズ可能な WS2812 RGB LED が4個搭載されており、点灯・消灯、色変更、明るさ調整、スタイル変更、変化速度の設定が可能です。

.. note::

    ``pironman5.service`` のステータスを変更するたびに、設定の変更を反映させるには、以下のコマンドを実行してください。

.. code-block:: shell

    sudo systemctl restart pironman5.service

* RGB LEDのオン・オフ状態を変更するには、 ``true`` で点灯、 ``false`` で消灯となります。

.. code-block:: shell

  sudo pironman5 -re true

* 色変更（例： ``fe1a1a``）：

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* 明るさ変更（0〜100%）：

.. code-block:: shell

  sudo pironman5 -rb 100

* RGB LEDの表示モードを切り替えるには、次のオプションから選択してください： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` 。

.. note::

  スタイルを ``rainbow`` 、 ``rainbow_reverse`` 、 ``hue_cycle`` に設定した場合は、 ``pironman5 -rc`` による色変更は無効になります。

.. code-block:: shell

  sudo pironman5 -rs breathing

* 変化速度の設定（0〜100%）：

.. code-block:: shell

  sudo pironman5 -rp 80

* デフォルトは4個のLED。LED数を変更するには：

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

RGBファンの制御
---------------------
IO拡張ボードは最大2基の5V非PWMファンに対応し、同時制御されます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、設定の変更を反映させるには次のコマンドを実行する必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* RGBファンの動作モードを設定可能：

例： **1: Performance** に設定すると、50℃で起動します。


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**：70℃で起動  
* **3: Balanced**：67.5℃で起動  
* **2: Cool**：60℃で起動  
* **1: Performance**：50℃で起動  
* **0: Always On**：常に起動状態  

* RGBファンの制御ピンをRaspberry Piの別のピンに接続する場合は、次のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18


**コアファンについて**

コアファンは、ラズベリーパイ5の専用4ピンPWMファン端子に接続します。その標準の制御方式は、ファームウェアによって管理され、CPU温度に基づく多段階の知的回転数調整機構です。つまり、公式または互換性のあるPWMファンを正しく接続して使用する場合、システムはCPU温度の変化に応じてファン回転数を自動的に調整し（50℃以上で作動を開始）、利用者の手動介入は一切不要です。

OLED画面の確認
-----------------------------------

``pironman5`` ライブラリをインストールすると、CPU・RAM・ディスク使用量・CPU温度・IPアドレスなどが再起動時にOLED画面へ表示されます。

表示されない場合は、まずFPCケーブルの接続状態を確認してください。

次にログを確認：

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

I2Cアドレス 0x3C が認識されているか確認：

.. code-block:: shell

  i2cdetect -y 1

赤外線受信モジュールの確認
---------------------------------------



* ``lirc`` モジュールのインストール：

  .. code-block:: shell

    sudo apt-get install lirc -y

* IR受信確認：

  .. code-block:: shell

    mode2 -d /dev/lirc0

* コマンド実行後にリモコンのボタンを押すと、そのボタンに対応するコードが表示されます。

