.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _ai_voice_assistant_car:

7. Asistente de Voz con IA
===========================

Esta lección convierte su Pironman 5 Pro MAX en un **asistente de IA basado en voz**.  
Con el código proporcionado, el robot: **esperará una palabra de activación**, **transcribirá su voz** con Vosk, la enviará a un **LLM de OpenAI** y **responderá hablando** usando Piper TTS.

----

Antes de Empezar
----------------

Asegúrese de tener:

* :ref:`test_piper` — La voz de Piper funciona (por ejemplo, puede reproducir “Hello”).  
* :ref:`test_vosk` — Vosk STT funciona para su idioma (por ejemplo, ``en-us``).  
* :ref:`py_online_llm` — Su **clave API de OpenAI** guardada en ``secret.py`` como ``OPENAI_API_KEY``.  
* Un **micrófono** y **altavoz** funcionando en Pironman 5 Pro MAX.  
* Una conexión de red estable (el LLM está en línea).

----

Ejecutar el Ejemplo
-------------------

.. code-block:: bash

   cd ~/sunfounder-voice-assistant/examples/
   sudo python3 voice_assistant.py

**Configuración utilizada por el código:**

* LLM: **OpenAI** (``gpt-4o-mini``)  
* TTS: **Piper** (``en_US-ryan-low``)  
* STT: **Vosk** (``en-us``)  
* Palabra de activación: ``"hey buddy"``  
* Entrada por teclado: **habilitada** (entrada manual opcional)  
* Modo imagen: **habilitado** (``WITH_IMAGE=True``) — requiere un LLM multimodal si decide usar imágenes más adelante

**Qué sucede:**

1. El asistente muestra un mensaje de bienvenida con la frase de activación.  
2. Escucha **“hey buddy”**.  
3. Después de la activación, su voz se transcribe (Vosk → texto).  
4. El texto se envía a **OpenAI (gpt-4o-mini)** para obtener una respuesta.  
5. La respuesta se reproduce con **Piper** (``en_US-ryan-low``).

**Ejemplo de interacción**

.. code-block:: text

   Usted: Hey Buddy
   Robot: ¡Hola!

   Usted: ¿Cuál es la capital de Italia?
   Robot: La capital de Italia es Roma.

Código
-----------------

.. code-block:: python

  from sunfounder_voice_assistant.voice_assistant import VoiceAssistant
  from sunfounder_voice_assistant.llm import OpenAI as LLM
  from secret import OPENAI_API_KEY as API_KEY

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Nombre del robot
  NAME = "Buddy"

  # Habilitar imagen, necesita configurar un modelo de lenguaje multimodal
  WITH_IMAGE = True

  # Configurar modelos e idiomas
  LLM_MODEL = "gpt-4o-mini"
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

  # Habilitar entrada por teclado
  KEYBOARD_ENABLE = True

  # Habilitar palabra de activación
  WAKE_ENABLE = True
  WAKE_WORD = [f"hey {NAME.lower()}"]
  # Configurar respuesta a la activación, dejar vacío para deshabilitar
  ANSWER_ON_WAKE = "Hi there"

  # Mensaje de bienvenida
  WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

  # Configurar instrucciones
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

**Explicación del código:**

* ``OpenAI(..., model="gpt-4o-mini")`` — Usa **OpenAI** como único LLM en esta lección.  
* ``NAME`` / ``WAKE_WORD`` — Personaliza el asistente (“Buddy”, “hey buddy”).  
* ``WITH_IMAGE=True`` — Habilita el modo imagen en el asistente (sin lógica de entrada/salida de imágenes aquí).  
* ``TTS_MODEL="en_US-ryan-low"`` — Voz de Piper utilizada para las respuestas.  
* ``STT_LANGUAGE="en-us"`` — Idioma de Vosk para el reconocimiento.  
* ``KEYBOARD_ENABLE=True`` — Permite entrada manual de texto opcional durante la depuración.  
* ``WELCOME`` / ``INSTRUCTIONS`` — Mensaje de inicio y personalidad del asistente/indicaciones del sistema.  
* ``va.run()`` — Inicia el bucle: **activación → escuchar → LLM → hablar**.


Cambiar a Otros LLM o TTS
--------------------------

Puede cambiar fácilmente a otros LLM, TTS o idiomas de STT con solo unas pocas ediciones:

* LLM compatibles:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Consulte los idiomas compatibles con **Piper TTS**.  
* :ref:`test_vosk` — Consulte los idiomas compatibles con **Vosk STT**.  

Para cambiar, simplemente modifique la parte de inicialización en el código:

.. code-block:: python

   from sunfounder_voice_assistant.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Configurar modelos e idiomas
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"



----

Solución de Problemas
-----------------------------

* **El robot no responde a la palabra de activación**

  - Verifique que el micrófono funcione.  
  - Asegúrese de que ``WAKE_ENABLE = True``.  
  - Ajuste la palabra de activación para que coincida con su pronunciación.  
  - Reduzca el ruido de fondo y hable claramente.

* **No sale sonido del altavoz**

  - Verifique el nombre del modelo TTS (por ejemplo, ``en_US-ryan-low``).  
  - Pruebe Piper o Espeak manualmente.  
  - Verifique la conexión del altavoz y el volumen.

* **Error de clave API o tiempo de espera**

  - Verifique su clave en ``secret.py``.  
  - Asegúrese de que su conexión de red sea estable.  
  - Confirme que el modelo LLM sea compatible (por ejemplo, ``gpt-4o-mini``).

* **La palabra de activación funciona pero no hay respuesta**

  - Verifique que el idioma de STT coincida con su acento.  
  - Asegúrese de que el modelo se haya descargado correctamente.  
  - Intente imprimir registros de depuración para confirmar que STT está funcionando.

* **TTS funciona pero no hay respuesta del LLM**

  - Verifique que la clave API sea válida.  
  - Verifique el nombre del modelo y la configuración del LLM.  
  - Asegure la conectividad a Internet.