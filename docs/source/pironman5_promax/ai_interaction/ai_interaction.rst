.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



9. 思考・対話・駆動 —  AI搭載、マルチLLM対応
------------------------------------------------------------


``sunfounder-voice-assistant`` パッケージは、Pironman 5 Pro MAX ハードウェアを操作するために必要なライブラリとツールを提供します。

以下のインストールコマンドを実行してください。

.. code-block:: bash


    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    sudo pip install ./sunfounder-voice-assistant --break


ここでは、テキスト読み上げ（TTS）、音声認識（STT）、大規模言語モデル（LLM）を活用し、Pironman 5 Pro MAX がまるでスマートロボットのように話しかけ、聞き取り、さらには会話できるようにする方法を探求します。



.. toctree:: 
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant
