.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



3. VoskによるSTT（オフライン）
==============================================

Vosk は、多くの言語をサポートし、Raspberry Pi上で完全に **オフライン** で動作する軽量な音声認識（STT）エンジンです。
インターネット接続が必要なのは、言語モデルをダウンロードする一度だけです。その後は、ネットワーク接続なしですべてが動作します。

このレッスンでは、Vosk をインストールし、選択した言語モデルでテストします。

.. 1. マイクの確認
.. --------------------------

.. 音声認識を使用する前に、USBマイクが正しく動作することを確認してください。

.. #. 利用可能な録音デバイスを一覧表示します：

..    .. code-block:: bash

..       arecord -l

..    ``card 1: ... device 0`` のような行を探します。

.. #. 短いサンプルを録音します（見つけた番号で ``1,0`` を置き換えます）：

..    .. code-block:: bash

..       arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

..    * 例：デバイスが ``card 2, device 0`` の場合、以下を使用します：

..    .. code-block:: bash

..       arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

.. #. 再生して録音を確認します：

..    .. code-block:: bash

..       aplay test.wav

.. #. 必要に応じてマイクの音量を調整します：

..    .. code-block:: bash

..       alsamixer

..    * **F6** を押して USB マイクを選択します。
..    * **Mic** または **Capture** チャンネルを見つけます。
..    * ミュートになっていないことを確認します（**[MM]** はミュート、 ``M`` を押して解除 → **[OO]** と表示されます）。
..    * ↑ / ↓ 矢印キーを使用して録音音量を変更します。


.. _test_vosk:

Voskのテスト
--------------------------

**プログラムの実行**

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 stt_vosk_stream.py

新しい言語でこのコードを初めて実行すると、Vosk は以下を行います：

* **言語モデルを自動的にダウンロード** します（デフォルトでは小規模バージョン）。
* **サポートされている言語のリストを出力** します。
* マイクからの音声入力を **待機** します。

ターミナルには以下のような表示がされます：

.. code-block:: text

         vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
         ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
         Say something

これは以下を意味します：

   * モデルファイル（ ``vosk-model-small-en-us-0.15`` ）がダウンロードされました。
   * サポートされている言語のリストが出力されました。
   * システムは現在待機状態です — Pironman 5 Pro MAX のマイクに向かって話すと、認識されたテキストがターミナルに表示されます。

**ヒント：**

* マイクは **15～30 cm** 離して使用すると精度が向上します。
* **言語とアクセントに合ったモデル** を選択してください。
* 認識精度を高めるために、静かな環境で使用してください。

**コード**

.. code-block:: python

   from sunfounder_voice_assistant.stt import Vosk as STT

   stt = STT(language="en-us")

   while True:
      print("Say something")
      for result in stt.listen(stream=True):
         if result["done"]:
               print(f"final:   {result['final']}")
         else:
               print(f"partial: {result['partial']}", end="\r", flush=True)


**コードの説明：**

* ``stt.listen(stream=True)`` — ストリーミング音声認識を開始し、話している途中の途中結果を逐次返します。
* ``result["partial"]`` — **リアルタイムの認識テキスト** を表示します（継続的に更新されます）。
* ``result["final"]`` — 話すのを止めたときに **最終的な認識文** を表示します。
* ループは継続的に実行され、**ハンズフリーのリアルタイム文字起こし** を可能にします。

ヒント：このストリーミングモードは、**音声アシスタント**、**コマンド制御**、または **ライブ文字起こし** に最適です。

トラブルシューティング
-----------------------------------------

* **No such file or directory（ `arecord` 実行時）**

  誤ったカード/デバイス番号を使用している可能性があります。
  以下を実行します：

  .. code-block:: bash

     arecord -l

  表示された USB マイクの番号で ``1,0`` を置き換えてください。

* **録音ファイルに音声がない**

  ミキサーを開き、マイクの音量を確認します：

  .. code-block:: bash

     alsamixer

  * **F6** を押して USB マイクを選択します。
  * **Mic/Capture** がミュートされていないことを確認します（**[MM]** ではなく **[OO]** と表示されます）。
  * ↑ キーでレベルを上げます。

* **Voskが音声を認識しない**

  * **言語コード** がモデルと一致していることを確認してください（例：英語の場合は ``en-us``、中国語の場合は ``zh-cn``）。
  * マイクを 15～30 cm 離し、背景ノイズを避けてください。
  * はっきりとゆっくり話してください。

* **高遅延 / 認識が遅い**

  * デフォルトの自動ダウンロードは **小規模モデル** です（高速ですが、精度は低めです）。
  * それでも遅い場合は、他のプログラムを終了して CPU を解放してください。