.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _py_online_llm:

5. Connexion aux LLM en ligne
===============================

Dans cette leçon, nous allons apprendre comment connecter votre Pironman 5 Pro MAX (ou Raspberry Pi) à différents **grands modèles de langage (LLM) en ligne**.
Chaque fournisseur nécessite une clé API et propose différents modèles parmi lesquels vous pouvez choisir.

Nous allons couvrir comment :

* Créer et sauvegarder vos clés API en toute sécurité.
* Choisir un modèle qui correspond à vos besoins.
* Exécuter notre exemple de code pour discuter avec les modèles.

Passons en revue chaque fournisseur étape par étape.

----

OpenAI
----------

OpenAI fournit des modèles puissants comme **GPT-4o** et **GPT-4.1** qui peuvent être utilisés pour des tâches de texte et de vision.

Voici comment le configurer :

**Obtenir et sauvegarder votre clé API**

#. Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create.png

#. Remplissez les détails (Propriétaire, Nom, Projet et autorisations si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devrez en générer une nouvelle.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/``), créez un fichier appelé ``secret.py`` :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Collez votre clé dans le fichier comme ceci :

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Activer la facturation et vérifier les modèles**

#. Avant d'utiliser la clé, allez sur la page **Billing** de votre compte OpenAI, ajoutez vos coordonnées de paiement et rechargez un petit montant de crédits.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_billing.png

#. Ensuite, allez sur la page **Limits** pour vérifier quels modèles sont disponibles pour votre compte et copiez l'ID exact du modèle à utiliser dans votre code.

   .. image:: /pironman5_promax/ai_interaction/img/llm_openai_models.png

**Tester avec l'exemple de code**

#. Ouvrez notre exemple de code :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_openai.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle de votre choix (par exemple, ``gpt-4o``) :

   .. code-block:: python

      from sunfounder_voice_assistant.llm import OpenAI
      from secret import OPENAI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = OpenAI(
         api_key=OPENAI_API_KEY,
         model="gpt-4o",
      )

   Sauvegardez et quittez (``Ctrl+X``, puis ``Y``, puis ``Enter``).

#. Enfin, exécutez le test :

   .. code-block:: bash

       sudo python3 llm_openai.py

----

Gemini
------------------

Gemini est la famille de modèles d'IA de Google. Il est rapide et excellent pour les tâches généralistes.

**Obtenir et sauvegarder votre clé API**

#. Connectez-vous à |link_google_ai|, puis allez sur la page API Keys.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_get.png

#. Cliquez sur le bouton **Create API key** dans le coin supérieur droit.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_create.png

#. Vous pouvez créer une clé pour un projet existant ou un nouveau.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_choose.png

#. Copiez la clé API générée.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Collez la clé :

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**Vérifier les modèles disponibles**

Allez sur la page officielle |link_gemini_model|, vous y verrez la liste des modèles, leurs ID API exacts et pour quel cas d'utilisation chacun est optimisé.

   .. image:: /pironman5_promax/ai_interaction/img/llm_gemini_model.png

**Tester avec l'exemple de code**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_gemini.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle de votre choix (par exemple, ``gemini-2.5-flash``) :

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Gemini
      from secret import GEMINI_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Gemini(
         api_key=GEMINI_API_KEY,
         model="gemini-2.5-flash",
      )

#. Sauvegardez et exécutez :

   .. code-block:: bash

       sudo python3 llm_gemini.py

----

Qwen
------------------

Qwen est une famille de grands modèles de langage et multimodaux fournis par Alibaba Cloud.
Ces modèles prennent en charge la génération de texte, le raisonnement et la compréhension multimodale (comme l'analyse d'images).

**Obtenir une clé API**

Pour appeler les modèles Qwen, vous avez besoin d'une **clé API**.
La plupart des utilisateurs internationaux doivent utiliser la console **DashScope International (Model Studio)**.
Les utilisateurs de Chine continentale peuvent utiliser la console **Bailian (百炼)**.

* **Pour les utilisateurs internationaux**

  #. Allez sur la page officielle |link_qwen_inter| sur **Alibaba Cloud**.
  #. Connectez-vous ou créez un compte **Alibaba Cloud**.
  #. Naviguez vers **Model Studio** (choisissez la région Singapour ou Pékin).

      * Si une invite « Activate Now » apparaît en haut de la page, cliquez dessus pour activer Model Studio et recevoir le quota gratuit (Singapour uniquement).
      * L'activation est gratuite — vous ne serez facturé qu'après utilisation de votre quota gratuit.
      * Si aucune invite d'activation n'apparaît, le service est déjà actif.

  #. Allez sur la page **Key Management**. Dans l'onglet **API Key**, cliquez sur **Create API Key**.
  #. Après la création, copiez votre clé API et conservez-la en sécurité.

    .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Les utilisateurs de Hong Kong, Macao et Taïwan doivent également choisir l'option **International (Model Studio)**.

* **Pour les utilisateurs de Chine continentale**

  Si vous êtes en Chine continentale, vous pouvez utiliser la console **Alibaba Cloud Bailian (百炼)** :

  #. Connectez-vous à |link_aliyun| (console Bailian) et complétez la vérification du compte.
  #. Sélectionnez **Create API Key**. Si vous êtes invité à activer les services de modèle, cliquez sur **Activate**, acceptez les conditions et réclamez votre quota gratuit. Après activation, le bouton **Create API Key** sera activé.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_create.png

  #. Cliquez à nouveau sur **Create API Key**, vérifiez votre compte, puis cliquez sur **Confirm**.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_confirm.png

  #. Une fois créée, copiez votre clé API.

     .. image:: /pironman5_promax/ai_interaction/img/llm_qwen_aliyun_copy.png

**Sauvegarder votre clé API**

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Collez votre clé comme ceci :

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        QWEN_API_KEY = "sk-xxx"

**Tester avec l'exemple de code**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_qwen.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle de votre choix (par exemple, ``qwen-plus``) :

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
         api_key=QWEN_API_KEY,
         model="qwen-plus",
      )

#. Exécutez avec :

   .. code-block:: bash

       sudo python3 llm_qwen.py

Grok (xAI)
------------------
Grok est l'IA conversationnelle de xAI, créée par l'équipe d'Elon Musk. Vous pouvez vous y connecter via l'API xAI.

**Obtenir et sauvegarder votre clé API**

#. Inscrivez-vous pour un compte ici : |link_grok_ai|. Ajoutez d'abord des crédits à votre compte — sinon l'API ne fonctionnera pas.

#. Allez sur la page API Keys, cliquez sur **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_create.png

#. Entrez un nom pour la clé, puis cliquez sur **Create API key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_name.png

#. Copiez la clé générée et conservez-la en sécurité.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Collez votre clé comme ceci :

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        GROK_API_KEY = "xai-xxx"

**Vérifier les modèles disponibles**

Allez sur la page Models dans la console xAI. Vous pouvez y voir tous les modèles disponibles pour votre équipe, ainsi que leurs ID API exacts — utilisez ces ID dans votre code.

   .. image:: /pironman5_promax/ai_interaction/img/llm_grok_model.png

**Tester avec l'exemple de code**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_grok.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle de votre choix (par exemple, ``grok-4-latest``) :

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Grok
      from secret import GROK_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Grok(
         api_key=GROK_API_KEY,
         model="grok-4-latest",
      )

#. Exécutez avec :

   .. code-block:: bash

       sudo python3 llm_grok.py

----

DeepSeek
------------------

DeepSeek est un fournisseur chinois de LLM offrant des modèles abordables et performants.

**Obtenir et sauvegarder votre clé API**

#. Connectez-vous à |link_deepseek|.

#. Dans le menu en haut à droite, sélectionnez **API Keys → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_create.png

#. Entrez un nom, cliquez sur **Create**, puis copiez la clé.

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Ajoutez votre clé :

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Activer la facturation**

Vous devrez d'abord recharger votre compte. Commencez par un petit montant (comme 10 ¥ RMB).

   .. image:: /pironman5_promax/ai_interaction/img/llm_deepseek_chognzhi.png

**Modèles disponibles**

Au moment de la rédaction (2025-09-12), DeepSeek propose :

* ``deepseek-chat``
* ``deepseek-reasoner``

**Tester avec l'exemple de code**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_deepseek.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle de votre choix (par exemple, ``deepseek-chat``) :

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

#. Exécutez :

   .. code-block:: bash

       sudo python3 llm_deepseek.py

----

Doubao
------------------
Doubao est la plateforme de modèles d'IA de ByteDance (Volcengine Ark).

**Obtenir et sauvegarder votre clé API**

#. Connectez-vous à |link_doubao|.

#. Dans le menu de gauche, descendez jusqu'à **API Key Management → Create API Key**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_create.png

#. Choisissez un nom et cliquez sur **Create**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_name.png

#. Cliquez sur l'icône **Show API Key** et copiez-la.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano secret.py

#. Ajoutez votre clé :

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Choisir un modèle**

#. Allez sur le marché des modèles et choisissez un modèle.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model_select.png

#. Par exemple, choisissez **Doubao-seed-1.6**, puis cliquez sur **API 接入**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_model.png

#. Sélectionnez votre clé API et cliquez sur **Use API**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_use_api.png

#. Cliquez sur **Enable Model**.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_kaitong.png

#. Survolez l'ID du modèle pour le copier.

   .. image:: /pironman5_promax/ai_interaction/img/llm_doubao_copy_id.png

**Tester avec l'exemple de code**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/sunfounder-voice-assistant/examples
       sudo nano llm_doubao.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle de votre choix (par exemple, ``doubao-seed-1-6-250615``) :

   .. code-block:: python

      from sunfounder_voice_assistant.llm import Doubao
      from secret import DOUBAO_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Doubao(
         api_key=DOUBAO_API_KEY,
         model="doubao-seed-1-6-250615",
      )

#. Exécutez avec :

   .. code-block:: bash

       sudo python3 llm_doubao.py

Général
--------------

Ce projet prend en charge la connexion à plusieurs plateformes LLM via une interface unifiée.
Nous avons une compatibilité intégrée avec :

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

De plus, vous pouvez vous connecter à **tout autre service LLM compatible avec le format d'API OpenAI**.
Pour ces plateformes, vous devrez obtenir manuellement votre **clé API** et le bon ``base_url``.

**Obtenir et sauvegarder votre clé API**

#. Obtenez une **clé API** auprès de la plateforme que vous souhaitez utiliser. (Consultez la console officielle de chaque plateforme pour plus de détails.)

#. Dans votre dossier de projet, créez un nouveau fichier :

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      nano secret.py

#. Ajoutez votre clé dans ``secret.py`` :

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. attention::

   Gardez votre clé API privée. Ne téléversez pas ``secret.py`` dans des dépôts publics.

**Tester avec l'exemple de code**

#. Ouvrez le fichier de test :

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano llm_others.py

#. Remplacez le contenu d'un fichier Python par l'exemple suivant, et remplissez le bon ``base_url`` et ``model`` pour votre plateforme :

   .. note::

      À propos de ``base_url`` :
      Nous prenons en charge le **format d'API OpenAI**, ainsi que toute API **compatible** avec celui-ci.
      Chaque fournisseur a son propre ``base_url``. Veuillez consulter sa documentation.

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

#. Exécutez le programme :

   .. code-block:: bash

      sudo python3 llm_others.py
