
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



9. Think · Talk · Drive —  Potenciado por IA con Múltiples LLM
---------------------------------------------------------------

El paquete ``sunfounder-voice-assistant`` proporciona las bibliotecas y herramientas necesarias para operar el hardware del Pironman 5 Pro MAX.

Ejecute el siguiente comando de instalación:

.. code-block:: bash

    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    sudo pip install ./sunfounder-voice-assistant --break

Aquí explorará texto a voz (TTS), voz a texto (STT) y modelos de lenguaje de gran tamaño (LLM) para hacer que su Pironman 5 Pro MAX hable, escuche e incluso converse con usted como un robot inteligente.



.. toctree:: 
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant
