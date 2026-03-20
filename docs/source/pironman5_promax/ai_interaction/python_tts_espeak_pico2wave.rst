.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



1. EspeakとPico2WaveによるTTS
=================================================

このレッスンでは、Raspberry Piに組み込まれた2つのテキスト読み上げ（TTS）エンジン — **Espeak** と **Pico2Wave** — を使用して、Pironman 5 Pro MAX に話しかけさせます。

これら2つのエンジンはどちらもシンプルでオフライン動作しますが、音質は大きく異なります：

* **Espeak**：非常に軽量で高速ですが、音声はロボット的です。速度、ピッチ、音量を調整できます。
* **Pico2Wave**：Espeakよりも滑らかで自然な音声を生成しますが、設定できるオプションは少なめです。

**音声品質** と **機能** の違いを実際に確認してみましょう。

----

1. Espeakのテスト
--------------------

EspeakはRaspberry Pi OSに含まれている軽量なTTSエンジンです。
音声はロボット的ですが、音量、ピッチ、速度などを調整できる高度な設定が可能です。

**プログラムの実行**

  .. code-block:: bash
  
      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_espeak.py

  * Pironman 5 Pro MAX が「Hello! I’m Espeak TTS.」と話すのが聞こえます。
  * コード内の調整パラメータを変更して、 ``amp``、 ``speed``、 ``gap``、 ``pitch`` が音声にどのように影響するか試してみてください。

**コード**

.. code-block:: python
  
  from sunfounder_voice_assistant.tts import Espeak

  # Espeak TTSインスタンスを作成
  tts = Espeak()
  # 振幅 0-200、デフォルト100
  tts.set_amp(200)
  # 速度 80-260、デフォルト150
  tts.set_speed(150)
  # 単語間の間隔 0-200、デフォルト1
  tts.set_gap(1)
  # ピッチ 0-99、デフォルト80
  tts.set_pitch(80)

  tts.say("Hello! I’m Espeak TTS.")

**コードの説明：**

* ``tts.set_amp()`` — 音量を制御します（0–200）。
* ``tts.set_speed()`` — 話す速度を調整します（80–260）。
* ``tts.set_gap()`` — 単語間の間隔を設定します（0–200）。
* ``tts.set_pitch()`` — ピッチを設定します（0–99）。
* ``tts.say()`` — テキストを音声に変換して再生します。

💡 **ヒント：** ピッチと速度を上げるとロボットが明るく聞こえ、下げると真剣な印象になります。

----


2. Pico2Waveのテスト
---------------------

Pico2Waveは、Espeakと比較して **より自然で人間らしい音声** を生成します。
非常に使いやすいですが、柔軟性は低く、**言語の変更** のみが可能で、ピッチや速度、音量は調整できません。
そのため、Pico2Waveは、あまり設定をせずにクリアで滑らかな音声が必要な場合に最適です。

**プログラムの実行**

  .. code-block:: bash
  
      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_pico2wave.py

* Pironman 5 Pro MAX が「Hello! I'm Pico2Wave TTS.」と話すのが聞こえます。
* 言語を変更して（例：スペイン語の ``es-ES``）、音声がどのように変わるか聞いてみてください。

**コード**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Pico2Wave

  # Pico2Wave TTSインスタンスを作成
  tts = Pico2Wave()

  # 言語を設定
  tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
  # 簡単な挨拶（動作確認）
  tts.say("Hello! I'm Pico2Wave TTS.")

**コードの説明：**

* ``tts.set_lang()`` — 音声合成の出力言語を設定します。

  - ``en-US`` （デフォルト）
  - ``en-GB``
  - ``de-DE``
  - ``es-ES``
  - ``fr-FR``
  - ``it-IT``

* ``tts.say()`` — テキストを音声に変換し、すぐに再生します。


----

トラブルシューティング
----------------------------------------

* **EspeakやPico2Wave実行時に音が出ない**

  * スピーカー／ヘッドフォンが接続されており、ミュートになっていないことを確認します。
  * ターミナルで簡単なテストを実行します：

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  音が聞こえない場合は、Pythonコードではなく音声出力に問題があります。

* **Espeakの音声が速すぎる、またはロボット的すぎる**

  * コード内のパラメータを調整してみてください：

    .. code-block:: python

       tts.set_speed(120)   # より遅く
       tts.set_pitch(60)    # 異なるピッチ

* **コード実行時に Permission denied と表示される**

  * ``sudo`` を付けて実行してみてください：

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

比較：Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 機能
     - Espeak
     - Pico2Wave
   * - 音声品質
     - ロボット的、合成音声
     - より自然、人間らしい
   * - 言語
     - デフォルトは英語
     - 少なめだが、一般的な言語
   * - 調整可能性
     - 可能（速度、ピッチなど）
     - 不可（言語のみ）
   * - パフォーマンス
     - 非常に高速、軽量
     - やや低速、やや重い