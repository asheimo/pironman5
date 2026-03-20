.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



6. ローカル音声チャットボット
=========================================

このレッスンでは、これまで学んだすべて — **音声認識 (STT)**、  
**テキスト読み上げ (TTS)**、そして **ローカルLLM (Ollama)** — を組み合わせて、  
Pironman 5 Pro MAX 上で完全にオフライン動作する **音声チャットボット** を構築します。

ワークフローはシンプルです：

#. **聴く** — マイクが音声をキャプチャし、 **Vosk** でテキストに変換します。
#. **考える** — テキストは Ollama で動作する **ローカルLLM** （例： ``llama3.2:3b``）に送信されます。
#. **話す** — チャットボットは **Piper TTS** を使用して回答を音声で出力します。

これにより、リアルタイムで理解し応答できる **ハンズフリー対話ロボット** が実現します。

----

始める前に
----------------

以下の準備が整っていることを確認してください：

* **Piper TTS** をテストし (:ref:`test_piper`)、動作する音声モデルを選択していること。
* **Vosk STT** をテストし (:ref:`test_vosk`)、適切な言語パック（例： ``en-us``）を選択していること。
* Pi または別のコンピュータに **Ollama** をインストールし (:ref:`download_ollama`)、 ``llama3.2:3b`` などのモデルをダウンロードしていること（メモリが限られている場合は ``moondream:1.8b`` などのより小さいモデルでも可）。

----

コードの実行
--------------

#. サンプルスクリプトを開きます：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano local_voice_chatbot.py

#. 必要に応じてパラメータを更新します：

   * ``stt = Vosk(language="en-us")``： アクセントや言語パックに合わせて変更します（例： ``en-us``、 ``zh-cn``、 ``es``）。
   * ``tts.set_model("en_US-amy-low")``： :ref:`test_piper` で確認した Piper 音声モデルに置き換えます。
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``： ご自身の設定に合わせて ``ip`` と ``model`` の両方を更新します。

     * ``ip``： Ollama が **同じ Pi** で動作している場合は ``localhost`` を使用します。Ollama が LAN 内の別のコンピュータで動作している場合は、Ollama で **Expose to network** を有効にし、そのコンピュータの LAN IP を ``ip`` に設定します。
     * ``model``： Ollama でダウンロード・有効化したモデル名と完全に一致している必要があります。

#. スクリプトを実行します：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo python3 local_voice_chatbot.py

#. 実行後、以下の動作が確認できます：

   * ボットが音声でウェルカムメッセージを出力します。
   * 音声入力を待機します。
   * Vosk が音声をテキストに変換します。
   * テキストが Ollama に送信され、回答がストリーム出力されます。
   * 回答がクリーンアップされ（隠れた推論を除去）、Piper によって音声出力されます。
   * プログラムは ``Ctrl+C`` でいつでも停止できます。

----

コード
---------------------

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.lm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

   # 音声認識の初期化
   stt = Vosk(language="en-us")

   # TTSの初期化
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # LLMへの指示文
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Ollama接続の初期化
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # ユーティリティ：隠れた推論の除去
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 聴取中... (停止するには Ctrl+C を押してください)")

               # Voskから最終的な文字起こしを収集
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[あなた] {text}")
                   else:
                       print(f"[あなた] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[情報] 認識されませんでした。もう一度お試しください。")
                   time.sleep(0.1)
                   continue

               # ストリーミングでOllamaに問い合わせ
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # クリーンアップして発話
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[情報] 停止中...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

コード分析
-------------

**インポートとグローバル設定**

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.lm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

これまで構築した3つのサブシステムをインポートします： **Vosk** （音声認識）、 **Ollama** （LLM）、 **Piper** （テキスト読み上げ）。



**STT (Vosk) の初期化**

.. code-block:: python

   stt = Vosk(language="en-us")

米国英語用の Vosk モデルをロードします。  
精度を高めるために、言語コード（例： ``zh-cn``、 ``es``）を音声パックに合わせて変更します。



**TTS (Piper) の初期化**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Piper エンジンを作成し、特定の音声を選択します。  
:ref:`test_piper` でテスト済みのモデルを選択してください。低品質の音声は高速で CPU 使用率も低くなります。



**LLMの指示文とウェルカムメッセージ**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

2つの重要な UX の選択：

* **回答を短く直接的に** 保ちます（TTS の明瞭さに役立ちます）。
* 「思考の連鎖」タグを明示的に禁止し、ノイズの多い出力を減らします。



**Ollamaへの接続と会話範囲の設定**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` は Ollama サーバーが同じ Pi 上で動作していることを前提とします。別の LAN マシンで動作する場合は、そのコンピュータの **LAN IP** を設定し、Ollama で *Expose to network* を有効にします。
* ``set_max_messages(20)`` は短い会話履歴を保持します。メモリやレイテンシに余裕がない場合はこの値を小さくします。

**発話前に隠れた推論／タグを除去**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

一部のモデルは内部スタイルのタグ（例： ``<think>…``）を出力することがあります。  
この関数はそれらを除去し、 **TTS が最終的な回答のみを** 発話するようにします。

**ヒント：** 画面上に他のアーティファクトが表示される場合（生のトークンをストリーム出力しているため）、この関数により **音声出力** は確実にクリーンな状態に保たれます。

**メインループ：一度挨拶し、その後 聴く → 考える → 話す を繰り返す**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

ターミナルとスピーカーでユーザーに挨拶します。起動時に一度だけ行われます。

**聴く（部分認識を含むストリーミングSTT）**

.. code-block:: python

   print("\n🎤 聴取中... (停止するには Ctrl+C を押してください)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[あなた] {text}")
       else:
           print(f"[あなた] {result['partial']}", end="\r", flush=True)

* ``stream=True`` は即時フィードバックのための **部分認識** と、発話終了時の **最終認識** を返します。
* 最終認識テキストは ``text`` に格納され、一度だけ表示されます。

**ガード：** 何も認識されなかった場合は LLM 呼び出しをスキップします：

.. code-block:: python

   if not text:
       print("[情報] 認識されませんでした。もう一度お試しください。")
       time.sleep(0.1)
       continue

これにより、空のプロンプトがモデルに送信されるのを防ぎます（時間とトークンの節約になります）。

**考える（ストリーム出力付きLLM）**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* 最終認識テキストをローカル LLM に送信し、 **トークンが到着次第表示** して低遅延を実現します。
* 一方で、後処理のために完全な回答を ``reply_accum`` に蓄積します。

**注記：** 生トークンを **表示しない** 場合は、 ``stream=False`` に設定し、最終文字列のみを表示します。

**話す（最初にクリーンアップし、TTS を一度だけ実行）**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* 最終テキストをクリーンアップして隠れたタグを除去し、 **一度だけ音声出力** します。
* TTS を1回だけにすることで、[LLM] / [SAY] のような繰り返しプロンプトを避けます。


**終了と後処理**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[情報] 停止中...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

**Ctrl+C** を使用して停止します。ボットは短い別れの挨拶をして、正常終了を知らせます。


----

トラブルシューティング & FAQ
-------------------------------------------

* **モデルが大きすぎる（メモリエラー）**

  ``moondream:1.8b`` などのより小さいモデルを使用するか、より強力なコンピュータで Ollama を実行します。

* **Ollama からの応答がない**

  Ollama が実行中であることを確認します（ ``ollama serve`` またはデスクトップアプリが起動していること）。リモートの場合は **Expose to network** を有効にし、IP アドレスを確認します。

* **Vosk が音声を認識しない**

  マイクが動作していることを確認します。必要に応じて別の言語パック（ ``zh-cn``、 ``es`` など）を試します。

* **Piper が無音またはエラー**

  選択した音声モデルがダウンロードされ、:ref:`test_piper` でテスト済みであることを確認します。

* **回答が長すぎる、または的外れ**

  ``INSTRUCTIONS`` を編集して **「回答は簡潔に要点を押さえてください。」** を追加します。