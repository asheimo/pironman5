.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



9. Think · Talk · Drive —  AI-Powered con Multi-LLM
------------------------------------------------------------

Il pacchetto ``sunfounder-voice-assistant`` fornisce le librerie e gli strumenti necessari per operare con l'hardware Pironman 5 Pro MAX.

Eseguire il seguente comando di installazione:

.. code-block:: bash

    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    sudo pip install sunfounder-voice-assistant --break

Qui esplorerai la sintesi vocale (TTS), il riconoscimento vocale (STT) e i modelli linguistici di grandi dimensioni (LLM) per far sì che il tuo Pironman 5 Pro MAX parli, ascolti e possa persino conversare con te come un robot intelligente.



.. toctree:: 
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant