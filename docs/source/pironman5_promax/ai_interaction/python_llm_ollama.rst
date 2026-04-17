.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

4. Conversación con Visión y Texto usando Ollama
=================================================

En esta lección, aprenderá a usar **Ollama**, una herramienta para ejecutar modelos de lenguaje y visión de gran tamaño localmente.  
Le mostraremos cómo instalar Ollama, descargar un modelo y conectar Pironman 5 Pro MAX a él.

Con esta configuración, Pironman 5 Pro MAX puede tomar una foto con la cámara y el modelo **verá y describirá** —  
puede hacer cualquier pregunta sobre la imagen, y el modelo responderá en lenguaje natural.

.. _download_ollama:

1. Instalar Ollama (LLM) y Descargar un Modelo
-------------------------------------------------

Puede elegir dónde instalar **Ollama**:

* En su Raspberry Pi (ejecución local)
* O en otro ordenador (Mac/Windows/Linux) en la **misma red local**

**Modelos recomendados vs hardware**

Puede elegir cualquier modelo disponible en |link_ollama_hub|.  
Los modelos vienen en diferentes tamaños (3B, 7B, 13B, 70B...).  
Los modelos más pequeños funcionan más rápido y requieren menos memoria, mientras que los más grandes ofrecen mejor calidad pero necesitan hardware potente.

Consulte la tabla a continuación para decidir qué tamaño de modelo se adapta a su dispositivo.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Tamaño del modelo
     - RAM mínima requerida
     - Hardware recomendado
   * - ~3B parámetros
     - 8GB (mejor 16GB)
     - Raspberry Pi 5 (16GB) o PC/Mac de gama media
   * - ~7B parámetros
     - 16GB+
     - Pi 5 (16GB, apenas usable) o PC/Mac de gama media
   * - ~13B parámetros
     - 32GB+
     - PC de escritorio / Mac con alta RAM
   * - 30B+ parámetros
     - 64GB+
     - Estación de trabajo / Servidor / GPU recomendada
   * - 70B+ parámetros
     - 128GB+
     - Servidor de gama alta con múltiples GPUs

**Instalar en Raspberry Pi**

Si desea ejecutar Ollama directamente en su Raspberry Pi:

* Use **Raspberry Pi OS de 64 bits**
* Muy recomendado: **Raspberry Pi 5 (16GB RAM)**

Ejecute los siguientes comandos:

.. code-block:: bash

   # Instalar Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Descargar un modelo ligero (bueno para pruebas)
   ollama pull llama3.2:3b

   # Prueba rápida de ejecución (escriba 'hi' y presione Enter)
   ollama run llama3.2:3b

   # Servir la API (puerto predeterminado 11434)
   # Consejo: establezca OLLAMA_HOST=0.0.0.0 para permitir acceso desde la LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Instalar en Mac / Windows / Linux (Aplicación de Escritorio)**

1. Descargue e instale Ollama desde |link_ollama|

   .. image:: img/llm_ollama_download.png

2. Abra la aplicación Ollama, vaya al **Selector de Modelos** y use la barra de búsqueda para encontrar un modelo. Por ejemplo, escriba ``llama3.2:3b`` (un modelo pequeño y ligero para empezar).

   .. image:: img/llm_ollama_choose.png

3. Después de que la descarga se complete, escriba algo simple como “Hi” en la ventana de chat. Ollama comenzará a descargarlo automáticamente la primera vez que lo use.

   .. image:: img/llm_olama_llama_download.png

4. Vaya a **Configuración** → active **Expose Ollama to the network**. Esto permite que su Raspberry Pi se conecte a través de la LAN.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Si ve un error como:

   ``Error: model requires more system memory ...``

   El modelo es demasiado grande para su máquina.  
   Use un **modelo más pequeño** o cambie a un ordenador con más RAM.

2. Probar Ollama
----------------

Una vez que Ollama esté instalado y su modelo esté listo, puede probarlo rápidamente con un bucle de chat mínimo.

**Ejecutar el programa**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 llm_ollama.py

Ahora puede chatear con Pironman 5 Pro MAX directamente desde la terminal.

   * Puede elegir **cualquier modelo** disponible en |link_ollama_hub|, pero se recomiendan modelos más pequeños (por ejemplo, ``moondream:1.8b``, ``phi3:mini``) si solo tiene 8–16GB de RAM.
   * Asegúrese de que el modelo que especifica en el código coincida con el modelo que ya ha descargado en Ollama.
   * Escriba ``exit`` o ``quit`` para detener el programa.
   * Si no puede conectarse, asegúrese de que Ollama esté ejecutándose y de que ambos dispositivos estén en la misma LAN si está usando un host remoto.

**Código**

.. code-block:: python

   from sunfounder_voice_assistant.llm import Ollama

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # Cambie esto a la IP de su ordenador. Si lo ejecuta en su pi, cámbielo a localhost
   llm = Ollama(
      ip="localhost",
      model="llama3.2:3b"
   )

   # Establecer cuántos mensajes conservar
   llm.set_max_messages(20)
   # Establecer instrucciones
   llm.set_instructions(INSTRUCTIONS)
   # Establecer mensaje de bienvenida
   llm.set_welcome(WELCOME)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # Respuesta sin stream
      # response = llm.prompt(input_text)
      # print(f"response: {response}")

      # Respuesta con stream
      response = llm.prompt(input_text, stream=True)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")


3. Conversación con Visión usando Ollama
-----------------------------------------

En esta demo, la cámara del Pi toma una foto **cada vez que escribe una pregunta**.  
El programa envía **su texto escrito + la nueva foto** a un modelo de visión local a través de Ollama,  
y luego transmite la respuesta del modelo en inglés simple.  
Esta es una base mínima de “ver y describir” que luego puede ampliar con verificaciones de color/cara/QR.

**Antes de Empezar**

#. Abra la aplicación **Ollama** (o ejecute el servicio) y asegúrese de haber descargado un modelo **con capacidad de visión**.

   * Si tiene suficiente memoria (≥16GB RAM), puede probar ``llava:7b``.
   * Si solo tiene **8GB RAM**, prefiera un modelo más pequeño como ``moondream:1.8b`` o ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Ejecutar la Demo**

#. Vaya a la carpeta de ejemplos y ejecute el script:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      python3 llm_ollama_with_image.py

#. Qué sucede cuando se ejecuta:

   * El programa imprime una línea de bienvenida y espera su entrada (``>>>``).
   * **Cada vez que escribe algo** (por ejemplo, “hello”, “Is there yellow?”, “Any faces?”, “What is on the desk?”):

     * **captura una foto** de la cámara del Pi (guardada en ``/tmp/llm-img.jpg``),
     * **envía su texto + la foto** al modelo de visión a través de Ollama,
     * **transmite de vuelta** la respuesta del modelo a la terminal.

   * Escriba ``exit`` o ``quit`` para finalizar el programa.

**Código**

.. code-block:: python

   from sunfounder_voice_assistant.llm import Ollama
   from picamera2 import Picamera2
   import time

   '''
   Necesita configurar ollama primero, vea llm_local.py

   Necesita al menos 8GB de RAM para ejecutar el gran modelo multimodal llava:7b
   '''

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   llm = Ollama(
      ip="localhost",          # ej., "192.168.100.145" si es remoto
      model="llava:7b"         # cambie a "moondream:1.8b" o "granite3.2-vision:2b" para 8GB RAM
   )

   # Establecer cuántos mensajes conservar
   llm.set_max_messages(20)
   # Establecer instrucciones
   llm.set_instructions(INSTRUCTIONS)
   # Establecer mensaje de bienvenida
   llm.set_welcome(WELCOME)

   # Inicializar cámara
   camera = Picamera2()
   config = camera.create_still_configuration(
      main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
      input_text = input(">>> ")

      # Capturar imagen
      img_path = '/tmp/llm-img.jpg'
      camera.capture_file(img_path)

      # Respuesta sin stream
      # response = llm.prompt(input_text, image_path=img_path)
      # print(f"response: {response}")

      # Respuesta con stream
      response = llm.prompt(input_text, stream=True, image_path=img_path)
      for next_word in response:
         if next_word:
               print(next_word, end="", flush=True)
      print("")


Solución de Problemas
---------------------

* **Recibo un error como: `model requires more system memory ...`.**

  * Esto significa que el modelo es demasiado grande para su dispositivo.
  * Use un modelo más pequeño como ``moondream:1.8b`` o ``granite3.2-vision:2b``.
  * O cambie a una máquina con más RAM y exponga Ollama a la red.

* **El código no puede conectarse a Ollama (connection refused).**

  Verifique lo siguiente:

  * Asegúrese de que Ollama esté ejecutándose (``ollama serve`` o la aplicación de escritorio está abierta).
  * Si usa un ordenador remoto, active **Expose to network** en la configuración de Ollama.
  * Verifique que el ``ip="..."`` en su código coincida con la IP correcta de la LAN.
  * Confirme que ambos dispositivos estén en la misma red local.

* **Mi cámara Pi no captura nada.**

  * Verifique que ``Picamera2`` esté instalado y funcionando con un script de prueba simple.
  * Compruebe que el cable de la cámara esté correctamente conectado y habilitado en ``raspi-config``.
  * Asegúrese de que su script tenga permiso para escribir en la ruta de destino (``/tmp/llm-img.jpg``).

* **La salida es demasiado lenta.**

  * Los modelos más pequeños responden más rápido, pero con respuestas más simples.
  * Puede reducir la resolución de la cámara (por ejemplo, 640×480 en lugar de 1280×720) para acelerar el procesamiento de imágenes.
  * Cierre otros programas en su Pi para liberar CPU y RAM.