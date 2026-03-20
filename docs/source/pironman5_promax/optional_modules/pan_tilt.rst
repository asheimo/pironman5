.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




パン・チルトカメラモジュール
===========================================


.. image:: img/pan_tilt.jpg
    :width: 600
    :align: center


.. note::

    Pironman 5シリーズにはカメラモジュールは付属していません。
    ご自身でご用意いただくか、公式ウェブサイトからご購入ください：

    * `AI Funsion Lab Kit <https://www.sunfounder.com/products/sunfounder-ai-fusion-lab-kit>`_

このセクションでは、2つのSG90サーボをGPIOピンに直接接続してパン・チルトカメラモジュールをセットアップし、制御する方法を学びます。このセクションが終了すると、プロジェクトで使用できる状態の、完全にインストールされた機能的なパン・チルトモジュールが完成します。

ハードウェア接続
-------------------------------------------

始める前に、Raspberry Piの電源がオフになっていることを確認してください。

**接続図:**


.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - デバイス
     - GPIOピン
     - 物理ピン
   * - パンサーボ（オレンジ）
     - GPIO17
     - ピン11
   * - チルトサーボ（オレンジ）
     - GPIO18
     - ピン12
   * - VCC（赤）
     - 5V
     - ピン2または4
   * - GND（茶）
     - GND
     - ピン6、9、14、20、25、30、34、39
   * - カメラモジュール
     - CSIインターフェース
     - カメラポートに接続



.. warning::

    SG90サーボはテスト中にRaspberry Piの5Vピンから直接電源を供給できますが、長時間の使用や両方のサーボを同時に動かすと電圧降下やシステムの不安定化を引き起こす可能性があります。長期的なプロジェクトでは、外部5V電源の使用を検討してください（Raspberry Piと共通のグランドを確保してください）。

**ステップバイステップの接続手順:**

1. **サーボの接続**:

   - パンサーボのオレンジ色の信号線をGPIO17（物理ピン11）に接続します
   - チルトサーボのオレンジ色の信号線をGPIO18（物理ピン12）に接続します
   - 両方のサーボの赤色のVCC線を5Vピン（物理ピン2または4）に接続します
   - 両方のサーボの茶色のGND線を任意のGNDピン（例：物理ピン6）に接続します

2. **カメラの接続**:

   - CSIカメラコネクタのプラスチッククリップをそっと持ち上げます
   - カメラリボンケーブルの金属接点がイーサネットポートと反対側を向くように挿入します
   - プラスチッククリップを押し下げてケーブルを固定します

サーボのテスト
-------------------------------------------

完全なパン・チルトの例を実行する前に、各サーボを個別にテストして正しく動作することを確認しましょう。

**1. GPIOとI2Cの有効化（必要な場合）:**

.. code-block:: bash

    sudo raspi-config
    # 以下に移動: Interface Options -> I2C -> Enable
    # 有効化後に再起動

**2. シンプルなサーボテストスクリプト:**

テストファイル ``servo_test.py`` を作成します:

.. code-block:: python

    #!/usr/bin/env python3
    # servo_test.py - シンプルなサーボテスト

    from gpiozero import Servo
    import time

    # GPIO17のパンサーボをテスト
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
    
    print("パンサーボ（GPIO17）をテスト中...")
    print("0°位置に移動...")
    pan.value = -1  # 0°
    time.sleep(2)
    
    print("90°位置に移動...")
    pan.value = 0   # 90°
    time.sleep(2)
    
    print("180°位置に移動...")
    pan.value = 1   # 180°
    time.sleep(2)
    
    pan.close()
    print("パンサーボのテスト完了")

**3. テストの実行:**

.. code-block:: bash

    python3 servo_test.py

サーボがすべての位置をスムーズに移動する場合は、ピン番号を18に変更してチルトサーボのテストを繰り返します。

カメラのテスト
-------------------------------------------

**1. カメラインターフェースの有効化:**

.. code-block:: bash

    sudo raspi-config
    # 以下に移動: Interface Options -> Camera -> Enable
    # または新しいシステムの場合: Interface Options -> Legacy Camera -> Enable
    sudo reboot

**2. カメラキャプチャのテスト:**

Raspberry Pi OS Bullseye以降（libcamera使用）の場合:

.. code-block:: bash

    # テスト写真を撮影
    libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480
    
    # カメラフィードをプレビュー
    libcamera-hello -t 0

古いシステム（raspistill使用）の場合:

.. code-block:: bash

    # テスト写真を撮影
    raspistill -o test.jpg -t 2000 -w 640 -h 480
    
    # カメラフィードをプレビュー
    raspivid -t 0

**3. 写真の確認:**

.. code-block:: bash

    ls -l test.jpg
    # 画像を開く（GUIがある場合）
    xdg-open test.jpg

パン・チルトの例
-------------------------------------------

次に、サーボ制御とカメラ機能を組み合わせて、完全なパン・チルト制御プログラムを作成しましょう。この例では、WSADキーを使用してカメラの向きを制御し、Tキーで写真を撮影できます。

**1. パン・チルト制御スクリプトの作成:**

.. code-block:: bash

    nano ptz_wsad_simple.py

以下のコードをコピーします:

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # ptz_wsad_simple.py - WSADキーでPTZを制御、超シンプルバージョン

    from gpiozero import Servo
    import os
    from datetime import datetime

    # サーボの初期化
    # SG90パラメータ: 最小パルス幅0.5ms（0°）、最大パルス幅2.5ms（180°）
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
    tilt = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    # 初期位置（中央）
    pan.value = 0
    tilt.value = 0

    print("\n=== SG90 PTZ 制御 ===")
    print("W: 上")
    print("S: 下")
    print("A: 左")
    print("D: 右")
    print("T: 写真撮影")
    print("C: 中央に戻す")
    print("Q: 終了")
    print("-" * 30)

    def take_photo():
        """写真撮影関数"""
        # 写真ディレクトリが存在しない場合は作成
        photo_dir = "/home/pi/Pictures/ptz"
        os.makedirs(photo_dir, exist_ok=True)
        
        # タイムスタンプ付きのファイル名を生成
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{photo_dir}/ptz_{timestamp}.jpg"
        
        # libcameraを使用して写真を撮影（Raspberry Pi Bullseye以降）
        # 古いシステムの代替: raspistillを使用
        os.system(f"libcamera-jpeg -o {filename} -t 1 --width 640 --height 480")
        
        # 古いシステム用の代替コマンド:
        # os.system(f"raspistill -o {filename} -t 1 -w 640 -h 480")
        
        print(f"写真を保存しました: {filename}")

    try:
        while True:
            # ユーザー入力の取得
            cmd = input("コマンドを入力: ").lower().strip()
            
            if cmd == 'w':
                # 上に移動（チルト角度を増加）
                tilt.value = min(1.0, tilt.value + 0.2)
                print(f"↑ 上 ({tilt.value:.1f})")
                
            elif cmd == 's':
                # 下に移動（チルト角度を減少）
                tilt.value = max(-1.0, tilt.value - 0.2)
                print(f"↓ 下 ({tilt.value:.1f})")
                
            elif cmd == 'a':
                # 左に移動（パン角度を減少）
                pan.value = max(-1.0, pan.value - 0.2)
                print(f"← 左 ({pan.value:.1f})")
                
            elif cmd == 'd':
                # 右に移動（パン角度を増加）
                pan.value = min(1.0, pan.value + 0.2)
                print(f"→ 右 ({pan.value:.1f})")
                
            elif cmd == 't':
                # 写真撮影
                take_photo()
                
            elif cmd == 'c':
                # PTZを中央に戻す
                pan.value = 0
                tilt.value = 0
                print("PTZを中央に戻しました")
                
            elif cmd == 'q':
                # プログラムを終了
                print("プログラムを終了します")
                break
                
            else:
                print("無効なコマンドです。W/S/A/D/T/C/Qを使用してください")
                
    except KeyboardInterrupt:
        print("\nユーザーによってプログラムが中断されました")
        
    finally:
        # GPIOリソースをクリーンアップ
        pan.close()
        tilt.close()
        print("GPIOをクリーンアップしました")

**2. スクリプトを実行可能にする:**

.. code-block:: bash

    chmod +x ptz_wsad_simple.py

**3. パン・チルトコントローラーの実行:**

.. code-block:: bash

    python3 ptz_wsad_simple.py

**4. カメラの制御:**

- **W/S** を押すと上下にチルトします
- **A/D** を押すと左右にパンします
- **T** を押すと写真を撮影します（ `/home/pi/Pictures/ptz/` に保存されます）
- **C** を押すとカメラを中央に戻します
- **Q** を押すと終了します


**カメラキャプチャ:**

スクリプトは ``libcamera-jpeg`` （新しいRaspberry Pi OSバージョン用）を使用して写真を撮影します。写真は上書きを防ぐためにタイムスタンプ付きで自動的に保存されます。