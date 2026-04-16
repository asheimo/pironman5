
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _py_online_llm:

5. Connessione a LLM Online
================================

In questa lezione impareremo come connettere il tuo Pironman 5 Pro MAX (o Raspberry Pi) a diversi **modelli linguistici di grandi dimensioni (LLM) online**.
Ogni fornitore richiede una chiave API e offre diversi modelli tra cui scegliere.

Tratteremo come:

* Creare e salvare le tue chiavi API in modo sicuro.
* Scegliere un modello che si adatti alle tue esigenze.
* Eseguire il nostro codice di esempio per chattare con i modelli.

Procediamo passo dopo passo per ogni fornitore.

----

OpenAI
----------

OpenAI fornisce modelli potenti come **GPT-4o** e **GPT-4.1** che possono essere utilizzati sia per attività testuali che visive.

Ecco come configurarlo:

**Ottieni e Salva la tua Chiave API**

#. Vai su |link_openai_platform| e accedi. Nella pagina **API keys**, clicca su **Create new secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create.png

#. Compila i dettagli (Owner, Name, Project, e permessi se necessari), poi clicca su **Create secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create_confirm.png

#. Una volta creata la chiave, copiala immediatamente — non potrai più vederla. Se la perdi, dovrai generarne una nuova.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_copy.png

#. Nella tua cartella di progetto (ad esempio: ``/``), crea un file chiamato ``secret.py``:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Incolla la tua chiave nel file in questo modo:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Abilita la fatturazione e controlla i modelli**

#. Prima di utilizzare la chiave, vai alla pagina **Billing** nel tuo account OpenAI, aggiungi i tuoi dati di pagamento e ricarica una piccola quantità di crediti.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_billing.png

#. Poi vai alla pagina **Limits** per controllare quali modelli sono disponibili per il tuo account e copia l'ID esatto del modello da utilizzare nel tuo codice.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_models.png

**Test con codice di esempio**

#. Apri il nostro codice di esempio:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_openai.py

#. Sostituisci il contenuto con il codice qui sotto, e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``gpt-4o``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import OpenAI
      from secret import OPENAI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = OpenAI(
         api_key=OPENAI_API_KEY,
         model="gpt-4o",
      )

   Salva ed esci (``Ctrl+X``, poi ``Y``, poi ``Enter``).

#. Infine, esegui il test:

   .. code-block:: bash

       sudo python3 llm_openai.py

----

Gemini
------------------

Gemini è la famiglia di modelli AI di Google. È veloce e ottimo per attività generiche.

**Ottieni e Salva la tua Chiave API**

#. Accedi a |link_google_ai|, poi vai alla pagina API Keys.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_get.png

#. Clicca sul pulsante **Create API key** nell'angolo in alto a destra.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_create.png

#. Puoi creare una chiave per un progetto esistente o per uno nuovo.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_choose.png

#. Copia la chiave API generata.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Incolla la chiave:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**Controlla i modelli disponibili**

Vai alla pagina ufficiale |link_gemini_model|, qui vedrai l'elenco dei modelli, i loro ID API esatti e per quale caso d'uso è ottimizzato ciascuno.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_model.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_gemini.py

#. Sostituisci il contenuto con il codice qui sotto, e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``gemini-2.5-flash``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Gemini
      from secret import GEMINI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Gemini(
         api_key=GEMINI_API_KEY,
         model="gemini-2.5-flash",
      )

#. Salva ed esegui:

   .. code-block:: bash

       sudo python3 llm_gemini.py

----

Qwen
------------------

Qwen è una famiglia di modelli linguistici e multimodali di grandi dimensioni fornita da Alibaba Cloud.
Questi modelli supportano la generazione di testo, il ragionamento e la comprensione multimodale (come l'analisi delle immagini).

**Ottieni una Chiave API**

Per chiamare i modelli Qwen, hai bisogno di una **Chiave API**.
La maggior parte degli utenti internazionali dovrebbe utilizzare la console **DashScope International (Model Studio)**.
Gli utenti della Cina continentale possono invece utilizzare la console **Bailian (百炼)**.

* **Per Utenti Internazionali**

  #. Vai alla pagina ufficiale |link_qwen_inter| su **Alibaba Cloud**.
  #. Accedi o crea un account **Alibaba Cloud**.
  #. Naviga verso **Model Studio** (scegli la regione Singapore o Beijing).

      * Se appare un prompt "Activate Now" nella parte superiore della pagina, cliccaci sopra per attivare Model Studio e ricevere la quota gratuita (solo Singapore).
      * L'attivazione è gratuita — ti verrà addebitato solo dopo aver utilizzato la tua quota gratuita.
      * Se non appare alcun prompt di attivazione, il servizio è già attivo.

  #. Vai alla pagina **Key Management**. Nella scheda **API Key**, clicca su **Create API Key**.
  #. Dopo la creazione, copia la tua Chiave API e conservala in un luogo sicuro.

    .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Gli utenti di Hong Kong, Macao e Taiwan dovrebbero anch'essi scegliere l'opzione **International (Model Studio)**.

* **Per Utenti della Cina Continentale**

  Se sei nella Cina continentale, puoi invece utilizzare la console **Alibaba Cloud Bailian (百炼)**:

  #. Accedi a |link_aliyun| (console Bailian) e completa la verifica dell'account.
  #. Seleziona **Create API Key**. Se viene visualizzato un messaggio che indica che i servizi del modello non sono attivati, clicca su **Activate**, accetta i termini e richiedi la tua quota gratuita. Dopo l'attivazione, il pulsante **Create API Key** sarà abilitato.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_create.png

  #. Clicca di nuovo su **Create API Key**, controlla il tuo account, poi clicca su **Confirm**.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_confirm.png

  #. Una volta creata, copia la tua Chiave API.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_copy.png

**Salva la tua Chiave API**

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Incolla la tua chiave in questo modo:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        QWEN_API_KEY = "sk-xxx"

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_qwen.py

#. Sostituisci il contenuto con il codice qui sotto, e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``qwen-plus``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
         api_key=QWEN_API_KEY,
         model="qwen-plus",
      )

#. Esegui con:

   .. code-block:: bash

       sudo python3 llm_qwen.py

Grok (xAI)
------------------
Grok è l'AI conversazionale di xAI, creata dal team di Elon Musk. Puoi connetterti ad esso attraverso l'API xAI.

**Ottieni e Salva la tua Chiave API**

#. Registrati per un account qui: |link_grok_ai|. Aggiungi prima alcuni crediti al tuo account — altrimenti l'API non funzionerà.

#. Vai alla pagina API Keys, clicca su **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_create.png

#. Inserisci un nome per la chiave, poi clicca su **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_name.png

#. Copia la chiave generata e conservala in un luogo sicuro.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Incolla la tua chiave in questo modo:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        GROK_API_KEY = "xai-xxx"

**Controlla i modelli disponibili**

Vai alla pagina Models nella console xAI. Qui puoi vedere tutti i modelli disponibili per il tuo team, insieme ai loro ID API esatti — usa questi ID nel tuo codice.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_model.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_grok.py

#. Sostituisci il contenuto con il codice qui sotto, e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``grok-4-latest``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Grok
      from secret import GROK_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Grok(
         api_key=GROK_API_KEY,
         model="grok-4-latest",
      )

#. Esegui con:

   .. code-block:: bash

       sudo python3 llm_grok.py

----

DeepSeek
------------------

DeepSeek è un fornitore cinese di LLM che offre modelli convenienti e capaci.

**Ottieni e Salva la tua Chiave API**

#. Accedi a |link_deepseek|.

#. Nel menu in alto a destra, seleziona **API Keys → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_create.png

#. Inserisci un nome, clicca su **Create**, poi copia la chiave.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Aggiungi la tua chiave:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Abilita la fatturazione**

Dovrai ricaricare il tuo account prima. Inizia con una piccola quantità (come 10 RMB).

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_chognzhi.png

**Modelli disponibili**

Al momento della scrittura (2025-09-12), DeepSeek offre:

* ``deepseek-chat``
* ``deepseek-reasoner``

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_deepseek.py

#. Sostituisci il contenuto con il codice qui sotto, e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``deepseek-chat``):

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

#. Esegui:

   .. code-block:: bash

       sudo python3 llm_deepseek.py

----

Doubao
------------------
Doubao è la piattaforma di modelli AI di ByteDance (Volcengine Ark).

**Ottieni e Salva la tua Chiave API**

#. Accedi a |link_doubao|.

#. Nel menu di sinistra, scorri verso il basso fino a **API Key Management → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_create.png

#. Scegli un nome e clicca su **Create**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_name.png

#. Clicca sull'icona **Show API Key** e copiala.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Aggiungi la tua chiave:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Scegli un modello**

#. Vai al marketplace dei modelli e scegli un modello.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model_select.png

#. Ad esempio, scegli **Doubao-seed-1.6**, poi clicca su **API 接入**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model.png

#. Seleziona la tua Chiave API e clicca su **Use API**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_use_api.png

#. Clicca su **Enable Model**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_kaitong.png

#. Passa il mouse sopra l'ID del modello per copiarlo.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy_id.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_doubao.py

#. Sostituisci il contenuto con il codice qui sotto, e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``doubao-seed-1-6-250615``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Doubao
      from secret import DOUBAO_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Doubao(
         api_key=DOUBAO_API_KEY,
         model="doubao-seed-1-6-250615",
      )

#. Esegui con:

   .. code-block:: bash

       sudo python3 llm_doubao.py

Generale
--------------

Questo progetto supporta la connessione a molteplici piattaforme LLM attraverso un'interfaccia unificata.
Abbiamo compatibilità integrata con:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

Inoltre, puoi connetterti a **qualsiasi altro servizio LLM compatibile con il formato API OpenAI**.
Per quelle piattaforme, dovrai ottenere manualmente la tua **Chiave API** e il corretto ``base_url``.

**Ottieni e Salva la tua Chiave API**

#. Ottieni una **Chiave API** dalla piattaforma che desideri utilizzare. (Vedi la console ufficiale di ciascuna piattaforma per i dettagli.)

#. Nella tua cartella di progetto, crea un nuovo file:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      nano secret.py

#. Aggiungi la tua chiave in ``secret.py``:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Mantieni privata la tua Chiave API. Non caricare ``secret.py`` su repository pubblici.

**Test con Codice di Esempio**

#. Apri il file di test:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano llm_others.py

#. Sostituisci il contenuto di un file Python con il seguente esempio, e inserisci il corretto ``base_url`` e ``model`` per la tua piattaforma:

   .. note::

      Informazioni su ``base_url``:
      Supportiamo il **formato API OpenAI**, così come qualsiasi API che sia **compatibile** con esso.
      Ogni fornitore ha il proprio ``base_url``. Controlla la loro documentazione.

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

#. Esegui il programma:

   .. code-block:: bash

      sudo python3 llm_others.py
