.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _py_online_llm:

5. Conectando a LLMs en Línea
================================

En esta lección, aprenderemos cómo conectar su Pironman 5 Pro MAX (o Raspberry Pi) a diferentes **Modelos de Lenguaje de Gran Tamaño (LLM) en línea**.  
Cada proveedor requiere una clave API y ofrece diferentes modelos entre los que puede elegir.

Cubriremos cómo:

* Crear y guardar sus claves API de forma segura.
* Elegir un modelo que se adapte a sus necesidades.
* Ejecutar nuestro código de ejemplo para chatear con los modelos.

Vamos paso a paso para cada proveedor.

----

OpenAI
----------

OpenAI proporciona modelos potentes como **GPT-4o** y **GPT-4.1** que pueden usarse tanto para tareas de texto como de visión.

Aquí está cómo configurarlo:

**Obtener y Guardar su Clave API**

#. Vaya a |link_openai_platform| e inicie sesión. En la página **API keys**, haga clic en **Create new secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create.png

#. Complete los detalles (Owner, Name, Project y permisos si es necesario), luego haga clic en **Create secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create_confirm.png

#. Una vez creada la clave, cópiela de inmediato — no podrá volver a verla. Si la pierde, deberá generar una nueva.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_copy.png

#. En la carpeta de su proyecto (por ejemplo: ``/``), cree un archivo llamado ``secret.py``:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Pegue su clave en el archivo de esta manera:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Habilitar facturación y verificar modelos**

#. Antes de usar la clave, vaya a la página **Billing** en su cuenta de OpenAI, agregue sus datos de pago y cargue una pequeña cantidad de crédito.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_billing.png

#. Luego vaya a la página **Limits** para verificar qué modelos están disponibles para su cuenta y copie el ID exacto del modelo para usar en su código.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_models.png

**Probar con el código de ejemplo**

#. Abra nuestro código de muestra:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_openai.py

#. Reemplace el contenido con el código a continuación, y actualice ``model="xxx"`` al modelo que desee (por ejemplo, ``gpt-4o``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import OpenAI
      from secret import OPENAI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = OpenAI(
         api_key=OPENAI_API_KEY,
         model="gpt-4o",
      )

   Guarde y salga (``Ctrl+X``, luego ``Y``, luego ``Enter``).

#. Finalmente, ejecute la prueba:

   .. code-block:: bash

       sudo python3 llm_openai.py

----

Gemini
------------------

Gemini es la familia de modelos de IA de Google. Es rápido y excelente para tareas de propósito general.

**Obtener y Guardar su Clave API**

#. Inicie sesión en |link_google_ai|, luego vaya a la página de API Keys.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_get.png

#. Haga clic en el botón **Create API key** en la esquina superior derecha.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_create.png

#. Puede crear una clave para un proyecto existente o uno nuevo.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_choose.png

#. Copie la clave API generada.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_copy.png

#. En la carpeta de su proyecto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Pegue la clave:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**Verificar modelos disponibles**

Vaya a la página oficial |link_gemini_model|, aquí verá la lista de modelos, sus IDs exactos de API y para qué caso de uso está optimizado cada uno.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_model.png

**Probar con el código de ejemplo**

#. Abra el archivo de prueba:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_gemini.py

#. Reemplace el contenido con el código a continuación, y actualice ``model="xxx"`` al modelo que desee (por ejemplo, ``gemini-2.5-flash``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Gemini
      from secret import GEMINI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Gemini(
         api_key=GEMINI_API_KEY,
         model="gemini-2.5-flash",
      )

#. Guarde y ejecute:

   .. code-block:: bash

       sudo python3 llm_gemini.py

----

Qwen
------------------

Qwen es una familia de modelos de lenguaje grande y multimodales proporcionados por Alibaba Cloud.
Estos modelos soportan generación de texto, razonamiento y comprensión multimodal (como análisis de imágenes).

**Obtener una Clave API**

Para llamar a los modelos Qwen, necesita una **Clave API**.
La mayoría de los usuarios internacionales deben usar la consola **DashScope International (Model Studio)**.
Los usuarios de China continental pueden usar en su lugar la consola **Bailian (百炼)**.

* **Para Usuarios Internacionales**

  #. Vaya a la página oficial |link_qwen_inter| en **Alibaba Cloud**.
  #. Inicie sesión o cree una cuenta de **Alibaba Cloud**.
  #. Navegue a **Model Studio** (elija la región Singapur o Beijing).

      * Si aparece un mensaje “Activate Now” en la parte superior de la página, haga clic en él para activar Model Studio y recibir la cuota gratuita (solo Singapur).
      * La activación es gratuita — solo se le cobrará después de usar su cuota gratuita.
      * Si no aparece ningún mensaje de activación, el servicio ya está activo.

  #. Vaya a la página **Key Management**. En la pestaña **API Key**, haga clic en **Create API Key**.
  #. Después de la creación, copie su Clave API y guárdela de forma segura.

    .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Los usuarios de Hong Kong, Macao y Taiwán también deben elegir la opción **International (Model Studio)**.

* **Para Usuarios de China Continental**

  Si está en China Continental, puede usar la consola **Alibaba Cloud Bailian (百炼)**:

  #. Inicie sesión en |link_aliyun| (consola Bailian) y complete la verificación de la cuenta.
  #. Seleccione **Create API Key**. Si aparece un mensaje indicando que los servicios de modelo no están activados, haga clic en **Activate**, acepte los términos y reclame su cuota gratuita. Después de la activación, el botón **Create API Key** se habilitará.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_create.png

  #. Haga clic en **Create API Key** nuevamente, verifique su cuenta y luego haga clic en **Confirm**.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_confirm.png

  #. Una vez creada, copie su Clave API.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_copy.png

**Guardar su Clave API**

#. En la carpeta de su proyecto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Pegue su clave de esta manera:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        QWEN_API_KEY = "sk-xxx"

**Probar con el código de ejemplo**

#. Abra el archivo de prueba:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_qwen.py

#. Reemplace el contenido con el código a continuación, y actualice ``model="xxx"`` al modelo que desee (por ejemplo, ``qwen-plus``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
         api_key=QWEN_API_KEY,
         model="qwen-plus",
      )

#. Ejecute con:

   .. code-block:: bash

       sudo python3 llm_qwen.py

Grok (xAI)
------------------
Grok es la IA conversacional de xAI, creada por el equipo de Elon Musk. Puede conectarse a través de la API de xAI.

**Obtener y Guardar su Clave API**

#. Regístrese para obtener una cuenta aquí: |link_grok_ai|. Agregue algo de crédito a su cuenta primero — de lo contrario la API no funcionará.

#. Vaya a la página de API Keys, haga clic en **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_create.png

#. Ingrese un nombre para la clave, luego haga clic en **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_name.png

#. Copie la clave generada y guárdela de forma segura.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_copy.png

#. En la carpeta de su proyecto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Pegue su clave de esta manera:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        GROK_API_KEY = "xai-xxx"

**Verificar modelos disponibles**

Vaya a la página Models en la consola de xAI. Aquí puede ver todos los modelos disponibles para su equipo, junto con sus IDs exactos de API — use estos IDs en su código.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_model.png

**Probar con el código de ejemplo**

#. Abra el archivo de prueba:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_grok.py

#. Reemplace el contenido con el código a continuación, y actualice ``model="xxx"`` al modelo que desee (por ejemplo, ``grok-4-latest``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Grok
      from secret import GROK_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Grok(
         api_key=GROK_API_KEY,
         model="grok-4-latest",
      )

#. Ejecute con:

   .. code-block:: bash

       sudo python3 llm_grok.py

----

DeepSeek
------------------

DeepSeek es un proveedor chino de LLM que ofrece modelos asequibles y capaces.

**Obtener y Guardar su Clave API**

#. Inicie sesión en |link_deepseek|.

#. En el menú superior derecho, seleccione **API Keys → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_create.png

#. Ingrese un nombre, haga clic en **Create**, luego copie la clave.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_copy.png

#. En la carpeta de su proyecto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Agregue su clave:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Habilitar facturación**

Necesitará recargar su cuenta primero. Comience con una pequeña cantidad (por ejemplo, ¥10 RMB).

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_chognzhi.png

**Modelos disponibles**

En el momento de escribir esto (2025-09-12), DeepSeek ofrece:

* ``deepseek-chat``
* ``deepseek-reasoner``

**Probar con el código de ejemplo**

#. Abra el archivo de prueba:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_deepseek.py

#. Reemplace el contenido con el código a continuación, y actualice ``model="xxx"`` al modelo que desee (por ejemplo, ``deepseek-chat``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Deepseek
      from secret import DEEPSEEK_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Deepseek(
         api_key=DEEPSEEK_API_KEY,
         model="deepseek-chat",
         max_messages=20,
      )

#. Ejecute:

   .. code-block:: bash

       sudo python3 llm_deepseek.py

----

Doubao
------------------
Doubao es la plataforma de modelos de IA de ByteDance (Volcengine Ark).

**Obtener y Guardar su Clave API**

#. Inicie sesión en |link_doubao|.

#. En el menú izquierdo, desplácese hacia abajo hasta **API Key Management → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_create.png

#. Elija un nombre y haga clic en **Create**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_name.png

#. Haga clic en el icono **Show API Key** y cópielo.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy.png

#. En la carpeta de su proyecto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Agregue su clave:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Elegir un modelo**

#. Vaya al mercado de modelos y elija un modelo.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model_select.png

#. Por ejemplo, elija **Doubao-seed-1.6**, luego haga clic en **API 接入**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model.png

#. Seleccione su Clave API y haga clic en **Use API**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_use_api.png

#. Haga clic en **Enable Model**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_kaitong.png

#. Pase el cursor sobre el ID del modelo para copiarlo.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy_id.png

**Probar con el código de ejemplo**

#. Abra el archivo de prueba:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_doubao.py

#. Reemplace el contenido con el código a continuación, y actualice ``model="xxx"`` al modelo que desee (por ejemplo, ``doubao-seed-1-6-250615``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Doubao
      from secret import DOUBAO_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Doubao(
         api_key=DOUBAO_API_KEY,
         model="doubao-seed-1-6-250615",
      )

#. Ejecute con:

   .. code-block:: bash

       sudo python3 llm_doubao.py

General
--------------

Este proyecto soporta la conexión a múltiples plataformas LLM a través de una interfaz unificada.
Tenemos compatibilidad incorporada con:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

Además, puede conectarse a **cualquier otro servicio LLM que sea compatible con el formato de API de OpenAI**.
Para esas plataformas, deberá obtener manualmente su **Clave API** y la ``base_url`` correcta.

**Obtener y Guardar su Clave API**

#. Obtenga una **Clave API** de la plataforma que desea usar. (Consulte la consola oficial de cada plataforma para más detalles.)

#. En la carpeta de su proyecto, cree un nuevo archivo:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      nano secret.py

#. Agregue su clave en ``secret.py``:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Mantenga su Clave API privada. No suba ``secret.py`` a repositorios públicos.

**Probar con el Código de Ejemplo**

#. Abra el archivo de prueba:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano llm_others.py

#. Reemplace el contenido de un archivo Python con el siguiente ejemplo, y complete la ``base_url`` y el ``model`` correctos para su plataforma:

   .. note::

      Sobre ``base_url``:
      Soportamos el **formato de API de OpenAI**, así como cualquier API que sea **compatible** con él.
      Cada proveedor tiene su propia ``base_url``. Consulte su documentación.

   .. code-block:: python

      from sunfounder_voice_assistant.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
         base_url = f"",
         api_key=API_KEY,
         model="",
      )

#. Ejecute el programa:

   .. code-block:: bash

      sudo python3 llm_others.py