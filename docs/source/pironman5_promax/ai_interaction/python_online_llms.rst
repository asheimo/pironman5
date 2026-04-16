.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _py_online_llm:

5. Verbindung zu Online-LLMs herstellen
==========================================================

In dieser Lektion lernen wir, wie Sie Ihren Pironman 5 Pro MAX (oder Raspberry Pi) mit verschiedenen **Online Large Language Models (LLMs)** verbinden können.
Jeder Anbieter benötigt einen API-Schlüssel und bietet verschiedene Modelle zur Auswahl an.

Wir werden behandeln, wie man:

* API-Schlüssel sicher erstellt und speichert.
* Ein Modell auswählt, das Ihren Anforderungen entspricht.
* Unser Beispielprogramm ausführt, um mit den Modellen zu chatten.

Gehen wir Schritt für Schritt für jeden Anbieter vor.

----

OpenAI
----------

OpenAI bietet leistungsstarke Modelle wie **GPT-4o** und **GPT-4.1**, die sowohl für Text- als auch für Bildaufgaben verwendet werden können.

So richten Sie es ein:

**API-Schlüssel abrufen und speichern**

#. Gehen Sie zu |link_openai_platform| und melden Sie sich an. Klicken Sie auf der Seite **API keys** auf **Create new secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create.png

#. Füllen Sie die Details aus (Owner, Name, Project und Berechtigungen falls erforderlich), dann klicken Sie auf **Create secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create_confirm.png

#. Sobald der Schlüssel erstellt wurde, kopieren Sie ihn sofort — Sie werden ihn nicht wieder sehen können. Wenn Sie ihn verlieren, müssen Sie einen neuen generieren.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_copy.png

#. Erstellen Sie in Ihrem Projektordner (z.B.: ``/``) eine Datei namens ``secret.py``:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie Ihren Schlüssel wie folgt in die Datei ein:

   .. code-block:: python

       # secret.py
       # Speichern Sie hier Geheimnisse. Committen Sie diese Datei niemals in Git.
       OPENAI_API_KEY = "sk-xxx"

**Abrechnung aktivieren und Modelle überprüfen**

#. Bevor Sie den Schlüssel verwenden, gehen Sie zur Seite **Billing** in Ihrem OpenAI-Konto, fügen Sie Ihre Zahlungsdetails hinzu und laden Sie einen kleinen Betrag an Guthaben auf.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_billing.png

#. Gehen Sie dann zur Seite **Limits**, um zu überprüfen, welche Modelle für Ihr Konto verfügbar sind, und kopieren Sie die genaue Modell-ID zur Verwendung in Ihrem Code.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_models.png

**Mit Beispielcode testen**

#. Öffnen Sie unseren Beispielcode:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_openai.py

#. Ersetzen Sie den Inhalt mit dem untenstehenden Code und aktualisieren Sie ``model="xxx"`` auf das gewünschte Modell (z.B. ``gpt-4o``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import OpenAI
      from secret import OPENAI_API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = OpenAI(
         api_key=OPENAI_API_KEY,
         model="gpt-4o",
      )

   Speichern und beenden (``Strg+X``, dann ``Y``, dann ``Enter``).

#. Führen Sie abschließend den Test aus:

   .. code-block:: bash

       sudo python3 llm_openai.py


----

Gemini
------------------

Gemini ist Googles Familie von KI-Modellen. Es ist schnell und großartig für allgemeine Aufgaben geeignet.

**API-Schlüssel abrufen und speichern**

#. Melden Sie sich bei |link_google_ai| an und gehen Sie dann zur Seite API Keys.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_get.png

#. Klicken Sie oben rechts auf die Schaltfläche **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_create.png

#. Sie können einen Schlüssel für ein bestehendes Projekt oder ein neues erstellen.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_choose.png

#. Kopieren Sie den generierten API-Schlüssel.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_copy.png

#. In Ihrem Projektordner:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie den Schlüssel ein:

   .. code-block:: python

        # secret.py
        # Speichern Sie hier Geheimnisse. Committen Sie diese Datei niemals in Git.
       GEMINI_API_KEY = "AIxxx"

**Verfügbare Modelle überprüfen**

Gehen Sie zur offiziellen |link_gemini_model| Seite, hier sehen Sie die Liste der Modelle, ihre genauen API-IDs und für welchen Anwendungsfall jedes optimiert ist.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_model.png

**Mit Beispielcode testen**

#. Öffnen Sie die Testdatei:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_gemini.py

#. Ersetzen Sie den Inhalt mit dem untenstehenden Code und aktualisieren Sie ``model="xxx"`` auf das gewünschte Modell (z.B. ``gemini-2.5-flash``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Gemini
      from secret import GEMINI_API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = Gemini(
         api_key=GEMINI_API_KEY,
         model="gemini-2.5-flash",
      )

#. Speichern und ausführen:

   .. code-block:: bash

       sudo python3 llm_gemini.py

----

Qwen
------------------

Qwen ist eine Familie von großen Sprach- und multimodalen Modellen, die von Alibaba Cloud bereitgestellt werden.
Diese Modelle unterstützen Textgenerierung, Argumentation und multimodales Verständnis (wie Bildanalyse).

**API-Schlüssel abrufen**

Um Qwen-Modelle aufzurufen, benötigen Sie einen **API-Schlüssel**.
Die meisten internationalen Benutzer sollten die **DashScope International (Model Studio)**-Konsole verwenden.
Benutzer in Festlandchina können stattdessen die **Bailian (百炼)**-Konsole verwenden.

* **Für internationale Benutzer**

  #. Gehen Sie zur offiziellen |link_qwen_inter| Seite auf **Alibaba Cloud**.
  #. Melden Sie sich an oder erstellen Sie ein **Alibaba Cloud**-Konto.
  #. Navigieren Sie zu **Model Studio** (wählen Sie die Region Singapur oder Peking).

      * Wenn oben auf der Seite eine "Activate Now"-Eingabeaufforderung erscheint, klicken Sie darauf, um Model Studio zu aktivieren und das kostenlose Kontingent zu erhalten (nur Singapur).
      * Die Aktivierung ist kostenlos — Ihnen werden erst Kosten berechnet, nachdem Ihr kostenloses Kontingent aufgebraucht ist.
      * Wenn keine Aktivierungsaufforderung erscheint, ist der Dienst bereits aktiv.

  #. Gehen Sie zur Seite **Key Management**. Klicken Sie auf dem Tab **API Key** auf **Create API Key**.
  #. Kopieren Sie nach der Erstellung Ihren API-Schlüssel und bewahren Sie ihn sicher auf.

    .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Benutzer in Hongkong, Macau und Taiwan sollten ebenfalls die Option **International (Model Studio)** wählen.

* **Für Benutzer in Festlandchina**

  Wenn Sie sich in Festlandchina befinden, können Sie stattdessen die **Alibaba Cloud Bailian (百炼)**-Konsole verwenden:

  #. Melden Sie sich bei |link_aliyun| (Bailian-Konsole) an und schließen Sie die Kontoverifizierung ab.
  #. Wählen Sie **Create API Key**. Wenn Sie aufgefordert werden, dass Modelldienste nicht aktiviert sind, klicken Sie auf **Activate**, stimmen Sie den Bedingungen zu und fordern Sie Ihr kostenloses Kontingent an. Nach der Aktivierung wird die Schaltfläche **Create API Key** aktiviert.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_create.png

  #. Klicken Sie erneut auf **Create API Key**, überprüfen Sie Ihr Konto und klicken Sie dann auf **Confirm**.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_confirm.png

  #. Sobald es erstellt wurde, kopieren Sie Ihren API-Schlüssel.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_copy.png

**API-Schlüssel speichern**

#. In Ihrem Projektordner:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie Ihren Schlüssel wie folgt ein:

   .. code-block:: python

        # secret.py
        # Speichern Sie hier Geheimnisse. Committen Sie diese Datei niemals in Git.

        QWEN_API_KEY = "sk-xxx"

**Mit Beispielcode testen**

#. Öffnen Sie die Testdatei:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_qwen.py

#. Ersetzen Sie den Inhalt mit dem untenstehenden Code und aktualisieren Sie ``model="xxx"`` auf das gewünschte Modell (z.B. ``qwen-plus``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = Qwen(
         api_key=QWEN_API_KEY,
         model="qwen-plus",
      )

#. Ausführen mit:

   .. code-block:: bash

       sudo python3 llm_qwen.py

Grok (xAI)
------------------
Grok ist xAIs konversationelle KI, erstellt von Elon Musks Team. Sie können über die xAI-API eine Verbindung herstellen.

**API-Schlüssel abrufen und speichern**

#. Registrieren Sie sich hier für ein Konto: |link_grok_ai|. Fügen Sie zuerst etwas Guthaben zu Ihrem Konto hinzu — sonst funktioniert die API nicht.

#. Gehen Sie zur Seite API Keys, klicken Sie auf **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_create.png

#. Geben Sie einen Namen für den Schlüssel ein und klicken Sie dann auf **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_name.png

#. Kopieren Sie den generierten Schlüssel und bewahren Sie ihn sicher auf.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_copy.png

#. In Ihrem Projektordner:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie Ihren Schlüssel wie folgt ein:

   .. code-block:: python

        # secret.py
        # Speichern Sie hier Geheimnisse. Committen Sie diese Datei niemals in Git.

        GROK_API_KEY = "xai-xxx"

**Verfügbare Modelle überprüfen**

Gehen Sie zur Models-Seite in der xAI-Konsole. Hier sehen Sie alle Modelle, die Ihrem Team zur Verfügung stehen, zusammen mit ihren genauen API-IDs — verwenden Sie diese IDs in Ihrem Code.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_model.png

**Mit Beispielcode testen**

#. Öffnen Sie die Testdatei:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_grok.py

#. Ersetzen Sie den Inhalt mit dem untenstehenden Code und aktualisieren Sie ``model="xxx"`` auf das gewünschte Modell (z.B. ``grok-4-latest``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Grok
      from secret import GROK_API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = Grok(
         api_key=GROK_API_KEY,
         model="grok-4-latest",
      )

#. Ausführen mit:

   .. code-block:: bash

       sudo python3 llm_grok.py

----

DeepSeek
------------------

DeepSeek ist ein chinesischer LLM-Anbieter, der erschwingliche und leistungsfähige Modelle anbietet.

**API-Schlüssel abrufen und speichern**

#. Melden Sie sich bei |link_deepseek| an.

#. Wählen Sie im Menü oben rechts **API Keys → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_create.png

#. Geben Sie einen Namen ein, klicken Sie auf **Create** und kopieren Sie dann den Schlüssel.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_copy.png

#. In Ihrem Projektordner:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie Ihren Schlüssel hinzu:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Abrechnung aktivieren**

Sie müssen zuerst Ihr Konto aufladen. Beginnen Sie mit einem kleinen Betrag (z.B. 10 RMB).

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_chognzhi.png

**Verfügbare Modelle**

Zum Zeitpunkt der Erstellung (2025-09-12) bietet DeepSeek:

* ``deepseek-chat``
* ``deepseek-reasoner``

**Mit Beispielcode testen**

#. Öffnen Sie die Testdatei:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_deepseek.py

#. Ersetzen Sie den Inhalt mit dem untenstehenden Code und aktualisieren Sie ``model="xxx"`` auf das gewünschte Modell (z.B. ``deepseek-chat``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Deepseek
      from secret import DEEPSEEK_API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = Deepseek(
         api_key=DEEPSEEK_API_KEY,
         model="deepseek-chat",
         max_messages=20,
      )

#. Ausführen:

   .. code-block:: bash

       sudo python3 llm_deepseek.py

----

Doubao
------------------
Doubao ist Bytedances KI-Modellplattform (Volcengine Ark).

**API-Schlüssel abrufen und speichern**

#. Melden Sie sich bei |link_doubao| an.

#. Scrollen Sie im linken Menü nach unten zu **API Key Management → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_create.png

#. Wählen Sie einen Namen und klicken Sie auf **Create**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_name.png

#. Klicken Sie auf das Symbol **Show API Key** und kopieren Sie es.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy.png

#. In Ihrem Projektordner:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Fügen Sie Ihren Schlüssel hinzu:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Ein Modell auswählen**

#. Gehen Sie zum Modell-Marktplatz und wählen Sie ein Modell aus.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model_select.png

#. Wählen Sie zum Beispiel **Doubao-seed-1.6** und klicken Sie dann auf **API 接入**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model.png

#. Wählen Sie Ihren API-Schlüssel aus und klicken Sie auf **Use API**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_use_api.png

#. Klicken Sie auf **Enable Model**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_kaitong.png

#. Bewegen Sie die Maus über die Modell-ID, um sie zu kopieren.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy_id.png

**Mit Beispielcode testen**

#. Öffnen Sie die Testdatei:

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_doubao.py

#. Ersetzen Sie den Inhalt mit dem untenstehenden Code und aktualisieren Sie ``model="xxx"`` auf das gewünschte Modell (z.B. ``doubao-seed-1-6-250615``):

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Doubao
      from secret import DOUBAO_API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = Doubao(
         api_key=DOUBAO_API_KEY,
         model="doubao-seed-1-6-250615",
      )

#. Ausführen mit:

   .. code-block:: bash

       sudo python3 llm_doubao.py


Allgemein
--------------

Dieses Projekt unterstützt die Verbindung zu mehreren LLM-Plattformen über eine einheitliche Schnittstelle.
Wir haben integrierte Kompatibilität mit:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

Darüber hinaus können Sie eine Verbindung zu **jedem anderen LLM-Dienst herstellen, der mit dem OpenAI-API-Format kompatibel ist**.
Für diese Plattformen müssen Sie manuell Ihren **API-Schlüssel** und die korrekte **base_url** abrufen.

**API-Schlüssel abrufen und speichern**

#. Besorgen Sie sich einen **API-Schlüssel** von der Plattform, die Sie verwenden möchten. (Details finden Sie in der offiziellen Konsole jeder Plattform.)

#. Erstellen Sie in Ihrem Projektordner eine neue Datei:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      nano secret.py

#. Fügen Sie Ihren Schlüssel in ``secret.py`` ein:

   .. code-block:: python

      # secret.py
      API_KEY = "ihr_api_schluessel_hier"

.. warning::

   Halten Sie Ihren API-Schlüssel geheim. Laden Sie ``secret.py`` nicht in öffentliche Repositories hoch.

**Mit Beispielcode testen**

#. Öffnen Sie die Testdatei:

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano llm_others.py

#. Ersetzen Sie den Inhalt einer Python-Datei mit dem folgenden Beispiel und füllen Sie die korrekte ``base_url`` und ``model`` für Ihre Plattform aus:

   .. note::

      Über ``base_url``:
      Wir unterstützen das **OpenAI-API-Format** sowie jede API, die **kompatibel** damit ist.
      Jeder Anbieter hat seine eigene ``base_url``. Bitte überprüfen Sie deren Dokumentation.

   .. code-block:: python

      from sunfounder_voice_assistant.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "Du bist ein hilfreicher Assistent."
      WELCOME = "Hallo, ich bin ein hilfreicher Assistent. Wie kann ich dir helfen?"

      llm = LLM(
         base_url = f"",
         api_key=API_KEY,
         model="",
      )

#. Führen Sie das Programm aus:

   .. code-block:: bash

      sudo python3 llm_others.py