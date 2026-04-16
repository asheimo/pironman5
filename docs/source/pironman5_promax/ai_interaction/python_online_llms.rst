.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _py_online_llm:

5. オンラインLLMへの接続
================================

このレッスンでは、Pironman 5 Pro MAX（またはRaspberry Pi）を様々な **オンライン大規模言語モデル（LLM）** に接続する方法を学びます。
各プロバイダーはAPIキーを必要とし、選択可能な異なるモデルを提供しています。

以下の方法を説明します：

* APIキーを安全に作成して保存する方法
* ニーズに合ったモデルを選択する方法
* サンプルコードを実行してモデルとチャットする方法

各プロバイダーごとにステップバイステップで見ていきましょう。

----

OpenAI
----------

OpenAIは、テキスト処理と視覚認識の両方に使用できる **GPT-4o** や **GPT-4.1** などの強力なモデルを提供しています。

セットアップ方法は以下の通りです：

**APIキーの取得と保存**

#. |link_openai_platform| にアクセスしてログインします。 **API keys** ページで、 **Create new secret key** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create.png

#. 詳細情報（Owner、Name、Project、必要に応じて権限）を入力し、 **Create secret key** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create_confirm.png

#. キーが作成されたら、すぐにコピーします — 二度と表示することはできません。紛失した場合は、新しいキーを生成する必要があります。

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_copy.png

#. プロジェクトフォルダ内（例： ``/``）に、 ``secret.py`` というファイルを作成します：

   .. code-block:: bash
   
       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. 以下のようにキーをファイルに貼り付けます：

   .. code-block:: python
   
       # secret.py
       # シークレット情報をここに保存します。このファイルをGitにコミットしないでください。
       OPENAI_API_KEY = "sk-xxx"

**請求設定とモデルの確認**

#. キーを使用する前に、OpenAIアカウントの **Billing** ページで支払い情報を追加し、少額のクレジットをチャージします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_billing.png

#. 次に **Limits** ページで、自分のアカウントで利用可能なモデルを確認し、コードで使用する正確なモデルIDをコピーします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_models.png

**サンプルコードでテスト**

#. サンプルコードを開きます：

   .. code-block:: bash
   
       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_openai.py

#. 内容を以下のコードに置き換え、 ``model="xxx"`` を使用したいモデルに更新します（例： ``gpt-4o``）：

   .. code-block:: python
   
      from sunfounder_voice_assistant.llm import OpenAI
      from secret import OPENAI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = OpenAI(
         api_key=OPENAI_API_KEY,
         model="gpt-4o",
      )
  
   保存して終了します（ ``Ctrl+X``、次に ``Y``、そして ``Enter``）。

#. 最後に、テストを実行します：

   .. code-block:: bash
   
       sudo python3 llm_openai.py
   

----

Gemini
------------------

GeminiはGoogleのAIモデルファミリーです。高速で、汎用的なタスクに最適です。

**APIキーの取得と保存**

#. |link_google_ai| にログインし、API Keysページに移動します。

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_get.png

#. 右上隅の **Create API key** ボタンをクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_create.png

#. 既存のプロジェクト用または新規プロジェクト用のキーを作成できます。

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_choose.png

#. 生成されたAPIキーをコピーします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_copy.png

#. プロジェクトフォルダ内で：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. キーを貼り付けます：

   .. code-block:: python

        # secret.py
        # シークレット情報をここに保存します。このファイルをGitにコミットしないでください。
       GEMINI_API_KEY = "AIxxx"

**利用可能なモデルの確認**

公式の |link_gemini_model| ページにアクセスすると、モデルの一覧、正確なAPI ID、各モデルが最適化されているユースケースが表示されます。

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_gemini.py

#. 内容を以下のコードに置き換え、 ``model="xxx"`` を使用したいモデルに更新します（例： ``gemini-2.5-flash``）：

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Gemini
      from secret import GEMINI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Gemini(
         api_key=GEMINI_API_KEY,
         model="gemini-2.5-flash",
      )

#. 保存して実行します：

   .. code-block:: bash

       sudo python3 llm_gemini.py

----

Qwen
------------------

Qwenは、Alibaba Cloudが提供する大規模言語モデルとマルチモーダルモデルのファミリーです。
これらのモデルは、テキスト生成、推論、マルチモーダル理解（画像分析など）をサポートしています。

**APIキーの取得**

Qwenモデルを呼び出すには、 **APIキー** が必要です。
ほとんどの海外ユーザーは **DashScope International (Model Studio)** コンソールを使用してください。
中国本土のユーザーは代わりに **Bailian (百炼)** コンソールを使用できます。

* **海外ユーザー向け**

  #. **Alibaba Cloud** の公式 |link_qwen_inter| ページにアクセスします。
  #. **Alibaba Cloud** アカウントにサインインするか、新規作成します。
  #. **Model Studio** に移動します（シンガポールまたは北京リージョンを選択）。

      * ページ上部に「Activate Now」というプロンプトが表示された場合は、それをクリックしてModel Studioを有効化し、無料枠を受け取ります（シンガポールのみ）。
      * 有効化は無料です — 無料枠を使用した後でのみ課金されます。
      * アクティベーションプロンプトが表示されない場合は、サービスは既に有効です。

  #. **Key Management** ページに移動します。 **API Key** タブで、 **Create API Key** をクリックします。
  #. 作成後、APIキーをコピーして安全に保管します。

    .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_api_key.png
        :width: 800

  .. note::
     香港、マカオ、台湾のユーザーも **International (Model Studio)** オプションを選択してください。

* **中国本土ユーザー向け**

  中国本土にいる場合は、代わりに **Alibaba Cloud Bailian (百炼)** コンソールを使用できます：

  #. |link_aliyun| (Bailian コンソール) にログインし、アカウント認証を完了します。
  #. **Create API Key** を選択します。モデルサービスが有効化されていないというプロンプトが表示された場合は、 **Activate** をクリックし、利用規約に同意して無料枠を請求します。有効化後、 **Create API Key** ボタンが有効になります。

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_create.png

  #. もう一度 **Create API Key** をクリックし、アカウントを確認してから **Confirm** をクリックします。

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_confirm.png

  #. 作成後、APIキーをコピーします。

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_copy.png

**APIキーの保存**

#. プロジェクトフォルダ内で：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # シークレット情報をここに保存します。このファイルをGitにコミットしないでください。
        
        QWEN_API_KEY = "sk-xxx"

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_qwen.py

#. 内容を以下のコードに置き換え、 ``model="xxx"`` を使用したいモデルに更新します（例： ``qwen-plus``）：

   .. code-block:: python
   
      from sunfounder_voice_assistant.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
         api_key=QWEN_API_KEY,
         model="qwen-plus",
      )

#. 実行します：

   .. code-block:: bash
   
       sudo python3 llm_qwen.py

Grok (xAI)
------------------
Grokは、Elon Muskのチームによって作成されたxAIの対話型AIです。xAI APIを通じて接続できます。

**APIキーの取得と保存**

#. |link_grok_ai| でアカウントにサインアップします。まずアカウントにクレジットを追加してください — そうしないとAPIは動作しません。

#. API Keysページに移動し、 **Create API key** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_create.png

#. キーの名前を入力し、 **Create API key** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_name.png

#. 生成されたキーをコピーし、安全に保管します。

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_copy.png

#. プロジェクトフォルダ内で：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # シークレット情報をここに保存します。このファイルをGitにコミットしないでください。
        
        GROK_API_KEY = "xai-xxx"

**利用可能なモデルの確認**

xAIコンソールのModelsページに移動します。ここでは、チームで利用可能なすべてのモデルと、その正確なAPI IDを確認できます — これらのIDをコードで使用します。

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_grok.py

#. 内容を以下のコードに置き換え、 ``model="xxx"`` を使用したいモデルに更新します（例： ``grok-4-latest``）：

   .. code-block:: python
   
      from sunfounder_voice_assistant.llm import Grok
      from secret import GROK_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Grok(
         api_key=GROK_API_KEY,
         model="grok-4-latest",
      )

#. 実行します：

   .. code-block:: bash
   
       sudo python3 llm_grok.py
   
----

DeepSeek
------------------

DeepSeekは、手頃な価格で高性能なモデルを提供する中国のLLMプロバイダーです。

**APIキーの取得と保存**

#. |link_deepseek| にログインします。

#. 右上隅のメニューで、 **API Keys → Create API Key** を選択します。

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_create.png

#. 名前を入力し、 **Create** をクリックして、キーをコピーします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_copy.png

#. プロジェクトフォルダ内で：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. キーを追加します：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**請求設定**

まずアカウントにチャージする必要があります。少額（10元など）から始めてください。

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_chognzhi.png

**利用可能なモデル**

本稿執筆時点（2025-09-12）では、DeepSeekは以下を提供しています：

* ``deepseek-chat``
* ``deepseek-reasoner``

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_deepseek.py

#. 内容を以下のコードに置き換え、 ``model="xxx"`` を使用したいモデルに更新します（例： ``deepseek-chat``）：

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

#. 実行します：

   .. code-block:: bash
   
       sudo python3 llm_deepseek.py

----

Doubao
------------------
DoubaoはByteDanceのAIモデルプラットフォーム（Volcengine Ark）です。

**APIキーの取得と保存**

#. |link_doubao| にログインします。

#. 左側のメニューで、 **API Key Management → Create API Key** までスクロールします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_create.png

#. 名前を選択し、 **Create** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_name.png

#. **Show API Key** アイコンをクリックしてコピーします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy.png

#. プロジェクトフォルダ内で：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. キーを追加します：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**モデルの選択**

#. モデルマーケットプレイスに移動し、モデルを選択します。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model_select.png

#. 例えば、 **Doubao-seed-1.6** を選択し、 **API 接入** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model.png

#. APIキーを選択し、 **Use API** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_use_api.png

#. **Enable Model** をクリックします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_kaitong.png

#. モデルIDにカーソルを合わせてコピーします。

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy_id.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_doubao.py

#. 内容を以下のコードに置き換え、 ``model="xxx"`` を使用したいモデルに更新します（例： ``doubao-seed-1-6-250615``）：

   .. code-block:: python
   
      from sunfounder_voice_assistant.llm import Doubao
      from secret import DOUBAO_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Doubao(
         api_key=DOUBAO_API_KEY,
         model="doubao-seed-1-6-250615",
      )

#. 実行します：

   .. code-block:: bash
   
       sudo python3 llm_doubao.py


一般設定
--------------

このプロジェクトは、統一されたインターフェースを通じて複数のLLMプラットフォームへの接続をサポートしています。
以下のプラットフォームとの互換性が組み込まれています：

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

さらに、 **OpenAI API形式と互換性のある他のLLMサービス** にも接続できます。
これらのプラットフォームの場合、 **APIキー** と正しい **base_url** を手動で取得する必要があります。

**APIキーの取得と保存**

#. 使用したいプラットフォームから **APIキー** を取得します。（詳細は各プラットフォームの公式コンソールを参照してください。）

#. プロジェクトフォルダ内で、新しいファイルを作成します：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      nano secret.py

#. ``secret.py`` にキーを追加します：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   APIキーは秘密にしてください。 ``secret.py`` を公開リポジトリにアップロードしないでください。

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano llm_others.py

#. Pythonファイルの内容を以下の例に置き換え、使用するプラットフォームに応じて正しい ``base_url`` と ``model`` を入力します：

   .. note::

      ``base_url`` について：
      **OpenAI API形式** およびそれと **互換性のある** APIをサポートしています。
      各プロバイダーには独自の ``base_url`` があります。それぞれのドキュメントを確認してください。

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

#. プログラムを実行します：

   .. code-block:: bash

      sudo python3 llm_others.py