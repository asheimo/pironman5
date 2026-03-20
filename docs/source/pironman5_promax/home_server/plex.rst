.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





Plexの設定
=======================================

Plexは、映画、テレビ番組、音楽、写真を整理し、複数のデバイスでストリーミングしてアクセスできる強力なメディアサーバープラットフォームです。Raspberry Piを搭載したPironman5シリーズにPlexを設定することで、24時間365日稼働する、手頃な価格でエネルギー効率の高いホームメディアセンターを作成できます。Raspberry Piのコンパクトなサイズ、低消費電力、柔軟性は、Plexをホストするための優れた選択肢となり、あなたのPiを自宅のネットワークから、あるいはリモートからもアクセス可能なパーソナルエンターテインメントハブに変身させます。


**準備**

* MicroSDカード（16GB以上、Class 10推奨）
* Raspberry Pi公式システム Raspberry Pi OS（またはRaspberry Pi OS Lite）
* 安定したネットワーク接続（有線イーサネット推奨）
* 外部ハードドライブまたはUSBスティック（ストレージ拡張用）


**Portainerのインストール**

ターミナルを開き、以下のコマンドを入力します：

1. Dockerのインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainerのインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash


3. Raspberry Piを再起動します。（その後、以下の手順を **すぐに** 完了してください。）



4. Raspberry Piが起動したら、Webブラウザを開き、Portainerのアドレスにアクセスします： ``http://<your-rpi-ip-address>:9443`` 。



5. デフォルトでは、サイトが既知の認証局（CA）によって発行されていない自己署名SSL/TLS証明書を使用しているという警告が表示される場合があります。ほとんどのWebブラウザはこのような警告を表示します。この場合、警告を無視してリスクを受け入れ、続行しても問題ありません。

   .. image:: img/home_server_app/private_save.png


#. 初回ログイン時には、管理者パスワードを設定するように求められます。

   .. image:: img/home_server_app/ptn_new_admin.png

#. 管理者アカウントを作成すると、Portainerのインターフェースに入ります。左側のナビゲーションバーから **Setting -> General** に移動し、 **App Templates** を見つけ、フィールドに以下のURLを入力します： ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. **Save Application Settings** をクリックします。設定には約10秒かかります。


**Plexのインストール**


1. 左側のナビゲーションバーから **Home -> local** をクリックします。

   .. image:: img/home_server_app/ptn_home_local.png

2. **Templates -> Application** に移動します。右上の検索バーに *nextcloud* と入力し、クリックします。

   .. image:: img/home_server_app/ptn_temp_nextcloud.png


#. ネットワークモードを **host** に設定します。

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. **Show advanced options** を展開します。

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. **volume mapping** セクションで、メディアファイルのストレージパスを設定し、Plexに読み取り/書き込み権限を付与します。デフォルトのパスは ``/portainer/TV`` と ``/portainer/Movies`` で、どちらも読み取り/書き込みアクセスが有効になっています。

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. **Deploy** をクリックし、Plexのインストールが完了するまで待ちます。


**Plexサーバーの設定**

1. ブラウザを開き、次のアドレスを入力します： ``http://<your_ip>:32400/web`` 。これでPlexのインターフェースが表示されます。

   .. image:: img/home_server_app/plex_visit.png

2. プレミアムサブスクリプションの申し出はスキップします。

3. 次に、 **Server Setup** 画面が表示されます。*Allow me to access my media outside my home* にチェックを入れることができます。現時点では、このチェックは外しておき、必要に応じて後で設定することをお勧めします。

   .. image:: img/home_server_app/plex_server_setup1.png

4. 次に、メディアを整理するように促されます。 *Skip* を選択し、後で設定からメディアを追加することもできます。ただし、Portainerのボリュームマッピングで設定したストレージパスを直接追加して、Plexが自動的にメディアをスキャンしてインポートできるようにすることをお勧めします。

   .. image:: img/home_server_app/plex_server_setup2.png

5. メディアライブラリのタイプを選択し、ライブラリに名前を付け、言語を選択します。

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. フォルダを追加します。先ほど設定したメディアストレージパスを見つけ、 **Add Library** をクリックします。

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. **Finish** をクリックします。Raspberry PiのPlexサーバーの設定が完了しました。

   .. image:: img/home_server_app/plex_server_setup3.png

8. Plexサーバーのホームページにメディアファイルが表示されるはずです。

   .. image:: img/home_server_app/plex_index.png