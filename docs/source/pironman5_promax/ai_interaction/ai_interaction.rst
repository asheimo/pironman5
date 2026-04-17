
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



9. Penser · Parler · Conduire —  Alimenté par l'IA avec Multi-LLMs
---------------------------------------------------------------------------------


Le package ``sunfounder-voice-assistant`` fournit les bibliothèques et outils nécessaires pour faire fonctionner le matériel Pironman 5 Pro MAX.

Exécutez la commande d'installation suivante :

.. code-block:: bash

    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    sudo pip install ./sunfounder-voice-assistant --break

Vous explorerez ici la synthèse vocale (TTS), la reconnaissance vocale (STT) et les grands modèles de langage (LLMs) pour faire parler, écouter et même discuter avec vous votre Pironman 5 Pro MAX, comme un robot intelligent.

.. toctree:: 
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant
