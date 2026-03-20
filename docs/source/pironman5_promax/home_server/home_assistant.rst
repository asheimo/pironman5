.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message






Home Assistantの設定
======================================

Home Assistantは、中央ハブ（Raspberry Pi、PCなど）上で動作するホームオートメーションプラットフォームです。照明やサーモスタットからセキュリティカメラやスマート家電まで、あらゆる種類のデバイスを制御および監視するために使用できます。

**準備**

始める前に、以下のものを用意してください：

* Home Assistantを実行できるRaspberry Pi
* 安定したインターネット接続
* Home Assistant Cloudのアカウント（オプションですが、リモートアクセスには推奨）

**インストール**

ターミナルを開き、以下のコマンドを入力します：

1. Dockerのインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash


2. Home Assistantのインストール

.. code-block:: bash

   sudo docker pull homeassistant/home-assistant


**Home Assistantコンテナの実行**

ここでは、Docker Composeを使用してHome Assistantを実行します。Docker Composeは「自動化スクリプト」のようなものと考えることができます。イメージ名、ポート、ボリュームマウント、環境変数などのすべての設定を ``docker-compose.yml`` ファイルに記述します。その後、単純なコマンド ``docker compose up -d`` だけで、Dockerはこの「スクリプト」に従って設定されたすべてのコンテナを自動的に作成し、起動します。


1.  **プロジェクトディレクトリに移動します**：そのフォルダに移動します。

   .. code-block:: bash

      cd ~/homeassistant


2.  **設定ファイルを作成します**： ``~/homeassistant`` ディレクトリ内に、 ``docker-compose.yml`` という名前のファイルを作成し、上記の設定をコピーします。

   .. code-block:: bash

      sudo nano docker-compose.yml


3. 以下の内容を ``docker-compose.yml`` ファイルに貼り付けます：

   .. note:: ``- TZ=Asia/Shanghai`` はお住まいのタイムゾーンに置き換えてください。

   .. code-block:: bash

      version: '3'
      services:
      homeassistant:
         image: ghcr.io/home-assistant/raspberrypi5-64-homeassistant:stable
         container_name: homeassistant
         restart: unless-stopped
         privileged: true
         network_mode: host
         environment:
            - TZ=Asia/Shanghai
         volumes:
            - ./config:/config

4. ``Ctrl+X`` でエディタを終了し、 ``Y`` を押して変更を保存します。

5.  **Home Assistantを起動します**： ``~/homeassistant`` ディレクトリで、以下のコマンドを実行します。Docker Composeは自動的にイメージをプルし、コンテナを起動します。

   .. code-block:: bash

      sudo docker compose up -d

   * ``up``： サービスを作成して起動します。
   * ``-d``： バックグラウンドで実行します（デタッチドモード）。


6.  **実行ステータスを確認します**：

    .. code-block:: bash

      docker compose ps

   ``homeassistant`` のステータスが ``Up`` と表示されるはずです。

7.  **ログを表示します** （起動時に問題がある場合）：

   .. code-block:: bash

      docker compose logs -f

8. その他のコマンドについては、以下を確認してください：

   .. code-block:: bash

      docker compose --help

**設定**

これで、お使いのコンピューターのブラウザを開き、 ``http://<Your Raspberry Pi Address>:8123`` にアクセスしてHome Assistantにアクセスできます。

.. image:: img/home_assistant/ha_welcome.png

**CREATE MY SMART HOME** を選択し、アカウントを作成します。

.. image:: img/home_assistant/ha_onboarding.png

プロンプトに従って、場所やその他の設定を選択します。完了すると、Home Assistantのダッシュボードが表示されます。

.. image:: img/home_assistant/ha_overview.png