.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

9. Denken · Sprechen · Fahren – KI-gestützt mit Multi-LLMs
------------------------------------------------------------

Das Paket ``sunfounder-voice-assistant`` enthält die notwendigen Bibliotheken und Werkzeuge für den Betrieb der Pironman 5 Pro MAX Hardware.

Führen Sie den folgenden Installationsbefehl aus:

.. code-block:: bash

    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    pip install ./sunfounder-voice-assistant --break


Hier erkunden Sie Text-to-Speech (TTS), Speech-to-Text (STT) und große Sprachmodelle (LLMs), um Ihren Pironman 5 Pro MAX zum Sprechen, Zuhören und sogar zum Chatten mit Ihnen wie ein intelligenter Roboter zu bringen.

.. toctree::
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant
