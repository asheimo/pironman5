.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



9. Think · Talk · Drive —  AI-Powered with Multi-LLMs
------------------------------------------------------------


The ``sunfounder-voice-assistant`` package provides the necessary libraries and tools for operating the Pironman 5 Pro MAX hardware.

Run the following installation command:

.. code-block:: bash

    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    sudo pip install sunfounder-voice-assistant --break

Here you will explore text-to-speech (TTS), speech-to-text (STT), and large language models (LLMs) to make your Pironman 5 Pro MAX talk, listen, and even chat with you like a smart robot.



.. toctree:: 
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant