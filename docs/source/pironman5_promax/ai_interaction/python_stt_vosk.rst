.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

3. STT con Vosk (Offline)
==============================================

Vosk es un motor de voz a texto (STT) ligero que soporta muchos idiomas y se ejecuta completamente **sin conexión** en Raspberry Pi.
Solo necesita acceso a internet una vez para descargar un modelo de idioma. Después de eso, todo funciona sin conexión de red.

En esta lección, instalaremos y probaremos Vosk con un modelo de idioma elegido.

.. _test_vosk:

Probar Vosk
--------------------------

**Ejecutar el programa**

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 stt_vosk_stream.py

La primera vez que ejecute este código con un nuevo idioma, Vosk:

* **Descargará automáticamente el modelo de idioma** (por defecto, la versión pequeña).
* **Imprimirá la lista de idiomas soportados**.
* Comenzará a **escuchar** la entrada de audio a través del micrófono.

Verá algo como esto en la terminal:

.. code-block:: text

         vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
         ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
         Say something

Esto significa:

   * El archivo del modelo (``vosk-model-small-en-us-0.15``) ha sido descargado.
   * Se ha impreso la lista de idiomas soportados.
   * El sistema ahora está escuchando — diga algo en el micrófono del Pironman 5 Pro MAX, y el texto reconocido aparecerá en la terminal.

**Consejos:**

* Mantenga el micrófono a unos **15–30 cm** de distancia para mayor precisión.
* Elija un **modelo que coincida con su idioma y acento**.
* Use un ambiente silencioso para mejorar el reconocimiento.

**Código**

.. code-block:: python

   from sunfounder_voice_assistant.stt import Vosk as STT

   stt = STT(language="en-us")

   while True:
      print("Say something")
      for result in stt.listen(stream=True):
         if result["done"]:
               print(f"final:   {result['final']}")
         else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

**Explicación del código:**

* ``stt.listen(stream=True)`` — Inicia el reconocimiento de voz en streaming y produce resultados intermedios mientras habla.
* ``result["partial"]`` — Muestra el **texto reconocido en tiempo real** (actualizado continuamente).
* ``result["final"]`` — Muestra la **oración final reconocida** cuando deja de hablar.
* El bucle se ejecuta continuamente, permitiendo **transcripción en tiempo real sin manos**.

Consejo: Este modo de streaming es perfecto para **asistentes de voz**, **control por comandos** o **transcripción en vivo**.

Solución de Problemas
---------------------

* **No such file or directory (al ejecutar `arecord`)**

  Puede haber usado el número de tarjeta/dispositivo incorrecto.
  Ejecute:

  .. code-block:: bash

     arecord -l

  y reemplace ``1,0`` con los números mostrados para su micrófono USB.

* **El archivo grabado no tiene sonido**

  Abra el mezclador y verifique el volumen del micrófono:

  .. code-block:: bash

     alsamixer

  * Presione **F6** para seleccionar su micrófono USB.
  * Asegúrese de que **Mic/Capture** no esté silenciado (**[OO]** en lugar de **[MM]**).
  * Aumente el nivel con la tecla ↑.

* **Vosk no reconoce la voz**

  * Asegúrese de que el **código de idioma** coincida con su modelo (por ejemplo, ``en-us`` para inglés, ``zh-cn`` para chino).
  * Mantenga el micrófono a 15–30 cm de distancia y evite el ruido de fondo.
  * Hable clara y lentamente.

* **Alta latencia / reconocimiento lento**

  * La descarga automática por defecto es un **modelo pequeño** (más rápido, pero menos preciso).
  * Si aún es lento, cierre otros programas para liberar CPU.