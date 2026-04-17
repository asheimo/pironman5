.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

6. Chatbot de Voz Local
===========================

En esta lección, combinará todo lo que ha aprendido — **reconocimiento de voz (STT)**,
**conversión de texto a voz (TTS)** y un **LLM local (Ollama)** — para construir un **chatbot de voz** completamente offline
que se ejecuta en su Pironman 5 Pro MAX.

El flujo de trabajo es simple:

#. **Escuchar** — El micrófono captura su voz y la transcribe con **Vosk**.
#. **Pensar** — El texto se envía a un **LLM** local ejecutándose en Ollama (por ejemplo, ``llama3.2:3b``).
#. **Hablar** — El chatbot responde en voz alta usando **Piper TTS**.

Esto crea un **robot conversacional manos libres** que puede entender y responder en tiempo real.

----

Antes de Empezar
----------------

Asegúrese de haber preparado lo siguiente:

* Probado **Piper TTS** (:ref:`test_piper`) y elegido un modelo de voz que funcione.
* Probado **Vosk STT** (:ref:`test_vosk`) y elegido el paquete de idioma correcto (por ejemplo, ``en-us``).
* Instalado **Ollama** (:ref:`download_ollama`) en su Pi o en otro ordenador, y descargado un modelo como ``llama3.2:3b`` (o uno más pequeño como ``moondream:1.8b`` si la memoria es limitada).

----

Ejecutar el Código
------------------

#. Abra el script de ejemplo:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano local_voice_chatbot.py

#. Actualice los parámetros según sea necesario:

   * ``stt = Vosk(language="en-us")``: Cambie esto para que coincida con su acento/paquete de idioma (por ejemplo, ``en-us``, ``zh-cn``, ``es``).
   * ``tts.set_model("en_US-amy-low")``: Reemplácelo con el modelo de voz de Piper que verificó en :ref:`test_piper`.
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Actualice tanto ``ip`` como ``model`` según su propia configuración.

     * ``ip``: Si Ollama se ejecuta en el **mismo Pi**, use ``localhost``. Si Ollama se ejecuta en otro ordenador de su LAN, active **Expose to network** en Ollama y configure ``ip`` con la IP LAN de ese ordenador.
     * ``model``: Debe coincidir exactamente con el nombre del modelo que descargó/activó en Ollama.

#. Ejecute el script:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo python3 local_voice_chatbot.py

#. Después de ejecutarlo, debería ver:

   * El bot lo saluda con un mensaje de bienvenida hablado.
   * Espera la entrada de voz.
   * Vosk transcribe su voz a texto.
   * El texto se envía a Ollama, que transmite una respuesta.
   * La respuesta se limpia (eliminando razonamientos ocultos) y se reproduce en voz alta con Piper.
   * Detenga el programa en cualquier momento con ``Ctrl+C``.

----

Código
------

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.llm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

   # Inicializar reconocimiento de voz
   stt = Vosk(language="en-us")

   # Inicializar TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instrucciones para el LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Inicializar conexión con Ollama
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utilidad: limpiar razonamientos ocultos
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
               print("\n🎤 Escuchando... (Presione Ctrl+C para detener)")

               # Recopilar transcripción final de Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[TÚ] {text}")
                   else:
                       print(f"[TÚ] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] No se reconoció nada. Intente de nuevo.")
                   time.sleep(0.1)
                   continue

               # Consultar Ollama con streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Limpiar y hablar
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Deteniendo...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

Análisis del Código
-------------------

**Importaciones y configuración global**

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.llm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

Incorpora los tres subsistemas que construyó anteriormente:
**Vosk** para voz a texto (STT), **Ollama** para el LLM y **Piper** para texto a voz (TTS).

**Inicializar STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Carga el modelo de Vosk para inglés estadounidense.
Cambie el código de idioma (por ejemplo, ``zh-cn``, ``es``) para que coincida con su paquete de voz y obtener mejor precisión.

**Inicializar TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Crea un motor Piper y selecciona una voz específica.
Elija un modelo que haya probado en :ref:`test_piper`. Las voces de menor calidad son más rápidas y usan menos CPU.

**Instrucciones del LLM y mensaje de bienvenida**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Dos decisiones clave de UX:

* Mantener **respuestas cortas y directas** (ayuda con la claridad del TTS).
* Prohibir explícitamente etiquetas de “cadena de pensamiento” ocultas para reducir salidas ruidosas.

**Conectar a Ollama y establecer el alcance de la conversación**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` asume que el servidor Ollama se ejecuta en el mismo Pi. Si se ejecuta en otra máquina de la LAN, ponga la **IP LAN** de ese ordenador y active *Expose to network* en Ollama.
* ``set_max_messages(20)`` mantiene un historial de conversación corto. Reduzca esto si la memoria/latencia es un problema.

**Eliminar razonamientos o etiquetas ocultas antes de hablar**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Algunos modelos pueden emitir etiquetas de estilo interno (por ejemplo, ``<think>…``).
Esta función las elimina para que su TTS **solo** hable la respuesta final.

**Consejo:** Si ve otros artefactos en pantalla (porque transmite tokens sin procesar), esta función ya garantiza que la salida **hablada** se mantenga limpia.

**Bucle principal: saludar una vez, luego escuchar → pensar → hablar**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Saluda al usuario por terminal y altavoz. Ocurre una vez al inicio.

**Escuchar (STT con streaming y parciales en vivo)**

.. code-block:: python

   print("\n🎤 Escuchando... (Presione Ctrl+C para detener)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[TÚ] {text}")
       else:
           print(f"[TÚ] {result['partial']}", end="\r", flush=True)

* ``stream=True`` produce transcripciones **parciales** para retroalimentación inmediata y una transcripción **final** cuando termina la expresión.
* El texto reconocido final se almacena en ``text`` y se imprime una vez.

**Protección:** Si no se reconoce nada, se omite la llamada al LLM:

.. code-block:: python

   if not text:
       print("[INFO] No se reconoció nada. Intente de nuevo.")
       time.sleep(0.1)
       continue

Esto evita enviar mensajes vacíos al modelo (ahorra tiempo y tokens).

**Pensar (LLM) con impresión en streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Envía la transcripción final al LLM local e **imprime los tokens a medida que llegan** para baja latencia.
* Mientras tanto, acumula la respuesta completa en ``reply_accum`` para su post-procesamiento.

**Nota:** Si prefiere **no mostrar** los tokens sin procesar, establezca ``stream=False`` y simplemente imprima la cadena final.

**Hablar (limpiar primero, luego TTS una vez)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Limpia el texto final para eliminar etiquetas ocultas, luego **habla exactamente una vez**.
* Mantener el TTS en un solo paso evita mensajes repetidos como “[LLM] / [SAY]”.

**Salida y limpieza**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Deteniendo...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Use **Ctrl+C** para detener. El bot dice una breve despedida para señalar una salida limpia.

----

Solución de Problemas y Preguntas Frecuentes
--------------------------------------------

* **El modelo es demasiado grande (error de memoria)**

  Use un modelo más pequeño como ``moondream:1.8b`` o ejecute Ollama en un ordenador más potente.

* **Sin respuesta de Ollama**

  Asegúrese de que Ollama esté ejecutándose (``ollama serve`` o la aplicación de escritorio abierta). Si es remoto, active **Expose to network** y verifique la dirección IP.

* **Vosk no reconoce la voz**

  Verifique que su micrófono funcione. Pruebe otro paquete de idioma (``zh-cn``, ``es``, etc.) si es necesario.

* **Piper silencioso o con errores**

  Confirme que el modelo de voz elegido esté descargado y probado en :ref:`test_piper`.

* **Respuestas demasiado largas o fuera de tema**

  Edite ``INSTRUCTIONS`` para agregar: **“Keep answers short and to the point.”**