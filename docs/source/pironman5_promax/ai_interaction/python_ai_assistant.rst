.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _ai_voice_assistant_car:

7. AI音声アシスタント
===========================

このレッスンでは、Pironman 5 Pro MAX を **音声ファーストのAIアシスタント** に変身させます。  
提供されたコードを使用することで、ロボットは以下の動作を行います： **ウェイクワードを待機し**、 **Vosk で音声をテキスト変換**し、それを **OpenAI LLM** に送信し、 **Piper TTS** を使用して音声で応答します。

----

始める前に
----------------

以下の準備が整っていることを確認してください：

* :ref:`test_piper` — Piper 音声が動作していること（例：「Hello」と再生できること）
* :ref:`test_vosk` — Vosk STT が使用する言語（例：``en-us``）で動作していること
* :ref:`py_online_llm` — **OpenAI APIキー** が ``secret.py`` に ``OPENAI_API_KEY`` として保存されていること
* Pironman 5 Pro MAX で動作する **マイク** と **スピーカー**
* 安定したネットワーク接続（LLMはオンラインで動作します）

----

サンプルの実行
---------------

.. code-block:: bash

   cd ~/sunfounder-voice-assistant/examples/
   sudo python3 voice_assistant.py

**コードで使用される設定:**

* LLM: **OpenAI** (``gpt-4o-mini``)  
* TTS: **Piper** (``en_US-ryan-low``)  
* STT: **Vosk** (``en-us``)  
* ウェイクワード: ``"hey buddy"``  
* キーボード入力: **有効** (オプションで手動入力可能) 
* 画像モード: **有効** (``WITH_IMAGE=True``) — 後で画像を使用する場合、マルチモーダル対応のLLMが必要です

**動作の流れ:**

1. アシスタントがウェイクフレーズとともにウェルカムメッセージを表示します。
2. **「hey buddy」** を聞き取るまで待機します。
3. ウェイク後、音声がテキスト変換されます（Vosk → テキスト）。
4. テキストは応答生成のために **OpenAI (gpt-4o-mini)** に送信されます。
5. 回答が **Piper** (``en_US-ryan-low``) によって音声出力されます。

**対話例**

.. code-block:: text

   あなた: Hey Buddy
   ロボット: Hi there!

   あなた: What’s the capital of Italy?
   ロボット: The capital of Italy is Rome.

コード
-----------------

.. code-block:: python

  from sunfounder_voice_assistant.voice_assistant import VoiceAssistant
  from sunfounder_voice_assistant.lm import OpenAI as LLM
  from secret import OPENAI_API_KEY as API_KEY

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # ロボットの名前
  NAME = "Buddy"

  # 画像を有効にする。マルチモーダル言語モデルの設定が必要
  WITH_IMAGE = True

  # モデルと言語の設定
  LLM_MODEL = "gpt-4o-mini"
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

  # キーボード入力を有効にする
  KEYBOARD_ENABLE = True

  # ウェイクワードを有効にする
  WAKE_ENABLE = True
  WAKE_WORD = [f"hey {NAME.lower()}"]
  # ウェイクワード応答の設定。空に設定すると無効化
  ANSWER_ON_WAKE = "Hi there"

  # ウェルカムメッセージ
  WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

  # 指示文の設定
  INSTRUCTIONS = f"""
  You are a helpful assistant, named {NAME}.
  """

  va = VoiceAssistant(
      llm,
      name=NAME,
      with_image=WITH_IMAGE,
      tts_model=TTS_MODEL,
      stt_language=STT_LANGUAGE,
      keyboard_enable=KEYBOARD_ENABLE,
      wake_enable=WAKE_ENABLE,
      wake_word=WAKE_WORD,
      answer_on_wake=ANSWER_ON_WAKE,
      welcome=WELCOME,
      instructions=INSTRUCTIONS,
  )

  if __name__ == "__main__":
      va.run()

**コードの説明:**

* ``OpenAI(..., model="gpt-4o-mini")`` — このレッスンでは **OpenAI** を唯一のLLMとして使用します。
* ``NAME`` / ``WAKE_WORD`` — アシスタントをカスタマイズします（「Buddy」、「hey buddy」）。
* ``WITH_IMAGE=True`` — アシスタントで画像モードを有効にします（このコードには画像入出力のロジックは含まれていません）。
* ``TTS_MODEL="en_US-ryan-low"`` — 応答に使用するPiper音声です。
* ``STT_LANGUAGE="en-us"`` — 認識に使用するVoskの言語です。
* ``KEYBOARD_ENABLE=True`` — デバッグ時に手動テキスト入力を可能にします。
* ``WELCOME`` / ``INSTRUCTIONS`` — 起動メッセージとアシスタントのペルソナ／システムプロンプトです。
* ``va.run()`` — **ウェイク → 聴取 → LLM → 発話** のループを開始します。


他のLLMやTTSへの切り替え
------------------------------

いくつかの編集だけで、他のLLM、TTS、STT言語に簡単に切り替えることができます：

* サポートされているLLM:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — **Piper TTS** のサポート言語を確認してください。
* :ref:`test_vosk` — **Vosk STT** のサポート言語を確認してください。

切り替えるには、コードの初期化部分を以下のように変更するだけです：

.. code-block:: python

   from sunfounder_voice_assistant.lm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # モデルと言語の設定
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"



----

トラブルシューティング
-----------------------------

* **ロボットがウェイクワードに反応しない**

  - マイクが動作しているか確認してください。
  - ``WAKE_ENABLE = True`` になっていることを確認してください。
  - ウェイクワードを自分の発音に合わせて調整してください。
  - 背景ノイズを減らし、はっきりと話してください。

* **スピーカーから音が出ない**

  - TTSモデル名（例：``en_US-ryan-low``）を確認してください。
  - Piper または Espeak を手動でテストしてください。
  - スピーカーの接続と音量を確認してください。

* **APIキーのエラーまたはタイムアウト**

  - ``secret.py`` 内のキーを確認してください。
  - ネットワーク接続が安定していることを確認してください。
  - LLMモデルがサポートされていること（例：``gpt-4o-mini``）を確認してください。

* **ウェイクワードは動作するが応答がない**

  - STT言語が自分のアクセントに合っているか確認してください。
  - モデルが正しくダウンロードされていることを確認してください。
  - デバッグログを出力してSTTが動作していることを確認してみてください。

* **TTSは動作するがLLMからの応答がない**

  - APIキーが有効であることを確認してください。
  - モデル名とLLM設定を確認してください。
  - インターネット接続を確認してください。