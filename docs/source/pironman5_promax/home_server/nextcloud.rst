.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





NextCloudPiの設定
=======================================

NextCloudは、Google DriveやDropboxと同様のオープンソースのプライベートクラウドストレージソリューションです。ファイルの保存、ドキュメントの共有、写真の同期、カレンダーや連絡先の管理に使用できます。
パブリッククラウドサービスとは異なり、NextCloudはユーザーにデータの完全な制御を提供するため、プライバシーとデータセキュリティを重視する個人や小規模チームに最適です。

Raspberry Piを搭載したPironman5シリーズは、低消費電力、コンパクトなサイズ、信頼性の高いパフォーマンスを提供し、ホームプライベートクラウドサーバーとして優れた選択肢となります。NextCloudと組み合わせることで、コスト効率の高いNASシステムとして機能します。


**準備**

* MicroSDカード（16GB以上、Class 10推奨）
* Raspberry Pi公式システム Raspberry Pi OS（またはRaspberry Pi OS Lite）
* 安定したネットワーク接続（有線イーサネット推奨）
* 外部ハードドライブまたはUSBスティック（ストレージ拡張用）


**portainerのインストール**

ターミナルを開き、以下のコマンドを入力します：

1. dockerのインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. portainerのインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash


 
3. Raspberry Piを再起動します。（その後、以下の手順を **すぐに** 完了してください。）



4. Raspberry Piが起動したら、Webブラウザを開き、Portainerのアドレスにアクセスします： ``https://<your-rpi-ip-address>:9443`` 。

5. デフォルトでは、サイトが既知の認証局（CA）によって発行されていない自己署名SSL/TLS証明書を使用しているという警告が表示されます。ほとんどのWebブラウザは、このような証明書について警告を表示します。この場合、警告を無視してリスクを受け入れ、続行しても問題ありません。

   .. image:: img/home_server_app/private_save.png


#. 初回ログイン時には、管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/ptn_new_admin.png

#. 管理者アカウントを登録すると、Portainerのインターフェースに入ります。左側のナビゲーションバーから **Setting -> General** をクリックし、 **App Templates** を見つけ、フィールドに以下のURLを入力します： ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. **Save Application Settings** をクリックします。設定には約10秒かかります。


**NextCloudのインストール**


1. 左側のナビゲーションバーから **Home -> local** をクリックします。

   .. image:: img/home_server_app/ptn_home_local.png

2. **Templates -> Application** に移動します。右上の検索バーに *nextcloud* と入力し、クリックします。

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. **Deploy the stack** をクリックし、デプロイが完了するまで待ちます。通常、これには約2分かかります。

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. 完了すると、NextCloudがインストールされます。

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png


**NextCloudの使用**

1. ブラウザを開き、NextCloudのアドレスにアクセスします： ``https://<your-rpi-ip-address>:32768`` 。

.. note::

   同様に、サイトが既知の認証局（CA）によって発行されていない自己署名SSL/TLS証明書を使用しているという警告が表示されます。ほとんどのWebブラウザは、このような証明書について警告を表示します。
   この場合、警告を無視してリスクを受け入れ、続行しても問題ありません。

   .. image:: img/home_server_app/private_save.png

2. 初回ログイン時には、管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/nc_admin_install.png

3. 登録後、NextCloudの使用を開始できます。

   .. image:: img/home_server_app/nc_dashboard.png