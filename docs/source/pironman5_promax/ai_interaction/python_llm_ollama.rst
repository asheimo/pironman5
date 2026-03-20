.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



4. Ollamaによるテキストビジョントーク
==================================================

このレッスンでは、大規模言語モデルと視覚モデルをローカルで実行するツールである **Ollama** の使用方法を学びます。  
Ollamaのインストール方法、モデルのダウンロード方法、そしてPironman 5 Pro MAXをOllamaに接続する方法を紹介します。

この設定により、Pironman 5 Pro MAXはカメラでスナップショットを撮影し、モデルが **画像を「見て」説明する** ことができます —  
画像について任意の質問をすると、モデルが自然言語で回答します。

.. _download_ollama:

1. Ollama (LLM) のインストールとモデルのダウンロード
---------------------------------------------------------------

**Ollama** のインストール先は選択できます：

* Raspberry Pi上（ローカル実行）
* または、 **同じローカルネットワーク** 内の別のコンピュータ（Mac/Windows/Linux）

**推奨モデルとハードウェア**

|link_ollama_hub| で利用可能な任意のモデルを選択できます。  
モデルにはさまざまなサイズ（3B、7B、13B、70B...）があります。  
小さいモデルは高速でメモリ消費も少なく、大きいモデルは高品質ですが、強力なハードウェアが必要です。

以下の表を参考に、お使いのデバイスに適したモデルサイズを選択してください。

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - モデルサイズ
     - 必要最小RAM
     - 推奨ハードウェア
   * - ~3B パラメータ
     - 8GB (16GB推奨)
     - Raspberry Pi 5 (16GB) または中級PC/Mac
   * - ~7B パラメータ
     - 16GB以上
     - Pi 5 (16GB、動作は可能) または中級PC/Mac
   * - ~13B パラメータ
     - 32GB以上
     - 高RAM搭載デスクトップPC / Mac
   * - 30B以上 パラメータ
     - 64GB以上
     - ワークステーション / サーバー / GPU推奨
   * - 70B以上 パラメータ
     - 128GB以上
     - 複数GPU搭載のハイエンドサーバー

**Raspberry Piへのインストール**

OllamaをRaspberry Pi上で直接実行する場合：

* **64-bit Raspberry Pi OS** を使用してください
* 強く推奨：**Raspberry Pi 5 (16GB RAM)**

以下のコマンドを実行します：

.. code-block:: bash

   # Ollamaのインストール
   curl -fsSL https://ollama.com/install.sh | sh

   # 軽量モデルのダウンロード（テストに最適）
   ollama pull llama3.2:3b

   # 簡単な動作テスト（'hi'と入力してEnter）
   ollama run llama3.2:3b

   # APIの起動（デフォルトポート11434）
   # ヒント：LANからのアクセスを許可するには OLLAMA_HOST=0.0.0.0 を設定
   OLLAMA_HOST=0.0.0.0 ollama serve

**Mac / Windows / Linuxへのインストール（デスクトップアプリ）**

1. |link_ollama| からOllamaをダウンロードしてインストールします

   .. image:: img/llm_ollama_download.png

2. Ollamaアプリを開き、 **Model Selector** に移動して検索バーでモデルを探します。例えば、 ``llama3.2:3b`` （初心者向けの小型軽量モデル）と入力します。

   .. image:: img/llm_ollama_choose.png

3. ダウンロードが完了したら、チャットウィンドウに「Hi」のような簡単な文章を入力します。初回使用時にOllamaは自動的にダウンロードを開始します。

   .. image:: img/llm_olama_llama_download.png

4. **Settings** → **Expose Ollama to the network** を有効にします。これにより、Raspberry PiがLAN経由で接続できるようになります。

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   以下のようなエラーが表示された場合：

   ``Error: model requires more system memory ...``

   モデルがお使いのマシンに対して大きすぎます。  
   **より小さいモデル** を使用するか、より多くのRAMを搭載したコンピュータに切り替えてください。

2. Ollamaのテスト
------------------------------

Ollamaがインストールされ、モデルの準備ができたら、最小限のチャットループで簡単にテストできます。

**プログラムの実行**

  .. code-block:: bash
  
      cd ~/sunfounder-voice-assistant/examples
      sudo python3 llm_ollama.py

これで、ターミナルから直接Pironman 5 Pro MAXとチャットできるようになります。

   * |link_ollama_hub| で利用可能な **任意のモデル** を選択できますが、8〜16GBのRAMしかない場合は、より小さいモデル（例： ``moondream:1.8b``、 ``phi3:mini``）をお勧めします。
   * コードで指定したモデルが、Ollamaで既にダウンロード済みのモデルと一致していることを確認してください。
   * プログラムを停止するには ``exit`` または ``quit`` と入力します。
   * 接続できない場合は、Ollamaが実行中であり、リモートホストを使用している場合は両方のデバイスが同じLAN上にあることを確認してください。

**コード**

.. code-block:: python

   from sunfounder_voice_assistant.lm import Ollama
 
   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # これをコンピュータのIPアドレスに変更してください。Piで実行する場合はlocalhostに変更します
   llm = Ollama(
      ip="localhost",
      model="llama3.2:3b"
   )

   # 保持するメッセージ数を設定
   llm.set_max_messages(20)
   # 指示文を設定
   llm.set_instructions(INSTRUCTIONS)
   # ウェルカムメッセージを設定
   llm.set_welcome(WELCOME)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # ストリームなしの応答
      # response = llm.prompt(input_text)
      # print(f"response: {response}")

      # ストリームありの応答
      response = llm.prompt(input_text, stream=True)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")


3. Ollamaによるビジョントーク
-----------------------------------------

このデモでは、 **質問を入力するたびに** Piカメラがスナップショットを撮影します。  
プログラムは **入力されたテキスト + 新しい写真** を、Ollama経由でローカルの視覚モデルに送信し、
モデルの回答をプレーンテキストでストリーム出力します。  
これは最小限の「見て説明する」ベースラインであり、後で色検出・顔検出・QRコードチェックなどに拡張できます。

**始める前に**

#. **Ollama** アプリを開き（またはサービスを実行し）、 **ビジョン対応モデル** がダウンロードされていることを確認します。

   * 十分なメモリ（≥16GB RAM）がある場合は、 ``llava:7b`` を試すことができます。
   * **8GB RAM** しかない場合は、 ``moondream:1.8b`` や ``granite3.2-vision:2b`` などのより小さいモデルを推奨します。

   .. image:: img/llm_ollama_image_model.png

**デモの実行**

#. サンプルフォルダに移動し、スクリプトを実行します：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      python3 llm_ollama_with_image.py

#. 実行時の動作：

   * プログラムはウェルカムメッセージを表示し、入力待ち状態（ ``>>>``）になります。
   * **何かを入力するたびに** （例：「hello」、「Is there yellow?」、「Any faces?」、「What is on the desk?」）、以下の処理が行われます：

     * Piカメラから **写真を撮影** し（ ``/tmp/llm-img.jpg`` に保存）、
     * **入力テキスト + 写真** を Ollama 経由で視覚モデルに送信し、
     * モデルの **回答をターミナルにストリーム出力** します。

   * ``exit`` または ``quit`` と入力するとプログラムが終了します。

**コード**

.. code-block:: python

   from sunfounder_voice_assistant.lm import Ollama
   from picamera2 import Picamera2
   import time

   '''
   事前に ollama のセットアップが必要です。llm_local.py を参照してください。

   llava:7b のような大規模マルチモーダルモデルを実行するには、少なくとも8GBのRAMが必要です。
   '''

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   llm = Ollama(
      ip="localhost",          # 例: "192.168.100.145"（リモートの場合）
      model="llava:7b"         # 8GB RAMの場合は "moondream:1.8b" または "granite3.2-vision:2b" に変更
   )

   # 保持するメッセージ数を設定
   llm.set_max_messages(20)
   # 指示文を設定
   llm.set_instructions(INSTRUCTIONS)
   # ウェルカムメッセージを設定
   llm.set_welcome(WELCOME)

   # カメラの初期化
   camera = Picamera2()
   config = camera.create_still_configuration(
      main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # 画像の撮影
      img_path = '/tmp/llm-img.jpg'
      camera.capture_file(img_path)

      # ストリームなしの応答
      # response = llm.prompt(input_text, image_path=img_path)
      # print(f"response: {response}")

      # ストリームありの応答
      response = llm.prompt(input_text, stream=True, image_path=img_path)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")


トラブルシューティング
------------------------------------


* **`model requires more system memory ...` のようなエラーが表示されます。**

  * これは、モデルがお使いのデバイスに対して大きすぎることを意味します。
  * ``moondream:1.8b`` や ``granite3.2-vision:2b`` などのより小さいモデルを使用してください。
  * または、より多くのRAMを搭載したマシンに切り替え、Ollamaをネットワークに公開してください。

* **コードがOllamaに接続できません（接続拒否）。**

  以下を確認してください：
  
  * Ollamaが実行中であること（ ``ollama serve`` またはデスクトップアプリが起動していること）。
  * リモートコンピュータを使用している場合、Ollamaの設定で **Expose to network** が有効になっていること。
  * コード内の ``ip="..."`` が正しいLAN IPと一致していることを再確認してください。
  * 両方のデバイスが同じローカルネットワーク上にあることを確認してください。

* **Piカメラが何も撮影しません。**

  * ``Picamera2`` がインストールされ、簡単なテストスクリプトで動作することを確認してください。
  * カメラケーブルが正しく接続され、 ``raspi-config`` で有効になっていることを確認してください。
  * スクリプトにターゲットパス（ ``/tmp/llm-img.jpg``）への書き込み権限があることを確認してください。

* **出力が遅すぎます。**

  * 小さいモデルは応答が速くなりますが、回答はシンプルになります。
  * カメラの解像度を下げる（例：1280×720 ではなく 640×480）ことで、画像処理を高速化できます。
  * Pi上の他のプログラムを終了して、CPUとRAMを解放してください。