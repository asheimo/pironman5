.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





.. _promax_omv_5_promax:


OpenMediaVaultの設定
=====================================

.. warning::

   OpenMediaVaultは、Raspberry Pi OSデスクトップへのインストールを **サポートしていません**。

   ⚠️ **Raspberry Pi OS Lite バージョン 11 (Bullseye) および 12 (Bookworm) のみがサポートされています。**

   正しいオペレーティングシステムがインストールされ、ネットワークが設定されていることを確認してください。
   ここでの手順は :ref:`install_os_sd_rpi_promax` と一貫していますが、イメージを選択する際は、Raspberry Pi OS (other) から Raspberry Pi OS Lite を選択してください。

   .. image:: img/omv/omv-install-1.png

OpenMediaVault（略称 OMV）は、Debian Linux をベースにしたオープンソースのネットワークアタッチドストレージ（NAS）オペレーティングシステムで、ホームユーザーや小規模オフィス環境向けに設計されており、ストレージ管理を簡素化し、豊富なネットワークサービス機能を提供することを目的としています。

以下の手順に従って、Raspberry Pi に OpenMediaVault をインストールしてください：

1. SSHを使用してRaspberry Piに接続する
-----------------------------------------------------------

   ターミナルで以下のコマンドを入力します：

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Windowsを使用している場合は、PuTTY または他の SSH クライアントを使用して Raspberry Pi に接続します。

2. OpenMediaVaultのインストール
------------------------------------------------

   ターミナルで以下のコマンドを入力します：

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   これにより、OpenMediaVault のインストールスクリプトがダウンロードされ、実行されます。インストール後は Raspberry Pi を再起動しないでください。

3. OpenMediaVaultへのアクセス
-----------------------------

   ブラウザに以下のURLを入力して OpenMediaVault にアクセスします：

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: 上記のURLにアクセスできない場合は、代わりにIPアドレス（例：http://192.168.1.100）を使用してみてください。

   ログインページが表示されますので、デフォルトのユーザー名とパスワードでログインします。デフォルトのユーザー名は ``admin``、パスワードは ``openmediavault`` です。

   .. image:: img/omv/omv-login.png

   ログイン後、OpenMediaVault のメインインターフェースが表示されます。

   .. image:: img/omv/omv-main.png

   これで、OpenMediaVault のインストールとアクセスに成功しました。ストレージの設定と管理を開始できます。


4. RAIDの設定（オプション）
---------------------------------------

   NVMe RAID は、複数の NVMe ソリッドステートドライブ（SSD）を RAID 技術で組み合わせるストレージソリューションであり、NVMe プロトコルの高速性能と RAID の冗長性／性能向上機能を最大限に活用することを目的としています。一般的なモードには RAID 0、1、5、10 などがあります。2台の NVMe SSD の場合、RAID 0 と RAID 1 が最も一般的に使用されるモードです。

   * RAID 0 はストライピング技術で、データを複数のストライプに分割し、これらのストライプを複数のハードドライブに分散させることで、より高い読み取り／書き込み速度を実現します。RAID 0 は冗長性を提供しないため、いずれかのハードドライブが故障すると、すべてのデータが失われます。

   * RAID 1 はミラーリング技術で、データを複数のハードドライブにコピーすることで、冗長性を提供します。RAID 1 の読み取り／書き込み速度は単一のハードドライブの速度に依存します。これは、複数のハードドライブからデータを読み取る必要があるためです。いずれかのハードドライブが故障しても、他のドライブがデータを提供し続けることができます。

   .. note:: RAID 0 または RAID 1 を構成するには、少なくとも2台のディスクをマウントする必要があります。RAID 0 では、RAID ボリュームの容量はすべてのディスクの容量の合計になります。RAID 1 では、RAID ボリュームの容量は最小のディスクの容量と同じになります。

   1. ``System`` メニューで ``Plugins`` オプションをクリックし、``openmediavault-md`` プラグインを検索してインストールします。

   .. image:: img/omv/omv-raid-1.png

   2. ``Storage`` メニューで ``Disks`` オプションをクリックし、2台のSSDを消去します。
   
   .. image:: img/omv/omv-raid-2.png

   3. この操作によりハードドライブ上のすべてのデータが消去されることに注意してください。重要なデータはすべてバックアップされていることを確認してください。

   .. image:: img/omv/omv-raid-3.png

   4. 消去モードは ``QUICK`` を選択すれば十分です。

   .. image:: img/omv/omv-raid-4.png

   5. ``Multiple Device`` タブに入り、``Create`` をクリックします。

   .. image:: img/omv/omv-raid-5.png

   6. Level オプションで、Stripe (RAID 0) または Mirror (RAID 1) を選択できます。Devices オプションで、消去したばかりのハードドライブを選択します。``Save`` をクリックし、RAID の設定が完了するまで待ちます。

   .. image:: img/omv/omv-raid-6.png

   .. note:: エラーレポート（500 - Internal Server Error）が表示された場合は、OMV システムを再起動してみてください。

   7. ``Apply`` ボタンをクリックして設定を適用します。

   .. image:: img/omv/omv-raid-7.png

   8. RAID の設定が完了したら、RAID の状態が ``100%`` になるまで待つ必要があります。

   .. image:: img/omv/omv-raid-8.png

   9. RAID の設定が完了すると、ハードドライブは RAID 0 または RAID 1 構成になり、単一のストレージデバイスとして使用できるようになります。

5. ストレージの設定
-----------------------

   OpenMediaVault のメインインターフェースで、左側のメニューの ``Storage`` オプションをクリックします。``Storage`` ページで、``Disks`` タブをクリックします。``Disks`` ページには、Raspberry Pi 上のすべてのディスクが表示されます。NVMe PIP にハードドライブが接続されていることを確認してください。

   .. image:: img/omv/omv-disk.png

   1. サイドバーで ``File System`` オプションをクリックします。次に、ファイルシステムを作成してマウントします。ファイルシステムタイプとして ``ext4`` を選択します。

   .. image:: img/omv/omv-mount.png

   2. デバイスを選択し、保存します。
   
   .. note:: RAID を設定している場合は、リストに RAID デバイスが表示されます。それを選択して保存します。

   .. image:: img/omv/omv-mount-2.png

   3. ファイルシステムが作成されていることを知らせるウィンドウが表示されますので、しばらくお待ちください。

   .. image:: img/omv/omv-mount-3.png

   4. 完了したら、``Mount`` インターフェースに入り、作成したばかりのファイルシステムを選択し、Raspberry Pi にマウントします。

   .. image:: img/omv/omv-mount-4.png

   .. note:: デュアルハードドライブを使用している場合（かつ RAID を使用していない場合）、上記の手順を繰り返して2台目のハードドライブも Raspberry Pi にマウントする必要があります。

   5. マウント後、Apply をクリックすると、ファイルシステム内のハードドライブ上のデータを確認できます。

   .. image:: img/omv/omv-mount-5.png

   この時点で、OpenMediaVault の設定とハードドライブのマウントに成功しました。これで OpenMediaVault を使用してストレージを管理できます。


6. 共有フォルダの作成
---------------------------------------

   1. ``Storage`` ページで、``Shared Folders`` タブに移動します。そして ``Create`` ボタンをクリックします。

   .. image:: img/omv/omv-share-1.png

   2. ``Create Shared Folder`` ページで、共有フォルダの名前を入力し、共有するハードドライブ、共有フォルダのパス、共有フォルダの権限を設定します。その後 ``Save`` ボタンをクリックします。

   .. image:: img/omv/omv-share-2.png

   3. これで、作成したばかりの共有フォルダが表示されます。正しいことを確認し、適用します。

   .. image:: img/omv/omv-share-3.png

   これで、共有フォルダの作成に成功しました。


7. 新しいユーザーの作成
---------------------------------------

   フォルダにアクセスするには、新しいユーザーを作成する必要があります。以下の手順に従ってください：

   1. ``User`` ページで、``Create`` ボタンをクリックします。

   .. image:: img/omv/omv-user-1.png

   2. ``Create User`` ページで、新しいユーザーのユーザー名とパスワードを入力し、``Save`` ボタンをクリックします。

   .. image:: img/omv/omv-user-2.png

   これで、新しいユーザーの作成に成功しました。


8. 新しいユーザーの権限設定
---------------------------------------

   1. ``Shared Folders`` ページで、作成したばかりの共有フォルダをクリックします。次に ``Permissions`` ボタンをクリックします。

   .. image:: img/omv/omv-user-3.png

   2. ``Permissions`` ページで、権限を設定します。その後 ``Save`` ボタンをクリックします。

   .. image:: img/omv/omv-user-4.png

   3. 完了したら、``Apply`` ボタンをクリックします。

   .. image:: img/omv/omv-user-5.png

   これで、この新しいユーザーを使用して共有フォルダにアクセスできるようになりました。


9. SMBサービスの設定
---------------------------------------

   1. ``Services`` ページで、``SMB/CIFS`` > ``Setting`` タブを見つけます。そして ``Enable`` オプションをチェックします。その後 ``Save`` ボタンをクリックします。

   .. image:: img/omv/omv-smb-1.png

   2. ``Apply`` ボタンをクリックして変更を適用します。

   .. image:: img/omv/omv-smb-2.png

   3. ``Shares`` ページに入り、``Create`` ボタンをクリックします。

   .. image:: img/omv/omv-smb-3.png

   4. ``Create Share`` ページで、共有フォルダのパスを選択します。その後 ``Save`` ボタンをクリックします。ちなみに、このページには多くのオプションがあり、必要に応じて設定できます。

   .. image:: img/omv/omv-smb-4.png

   5. ``Apply`` をクリックします。

   .. image:: img/omv/omv-smb-5.png

   SMBサービスの設定に成功しました。これで SMB プロトコルを使用して共有フォルダにアクセスできます。


10. Windowsで共有フォルダにアクセスする
---------------------------------------

   1. ``PC`` を開き、``ネットワークドライブのマウント`` をクリックします。

   .. image:: img/omv/omv-network-location-1.png

   2. 表示されたダイアログボックスで、``フォルダー`` フィールドに Raspberry Pi の IP アドレス（例： ``\\192.168.1.100\``）、または Raspberry Pi のホスト名（例： ``\\pi.local\``）を入力します。

   .. image:: img/omv/omv-network-location-2.png

   3. 参照ボタンをクリックし、アクセスしたい共有フォルダを選択します。この過程で、先ほど作成したユーザー名とパスワードを入力する必要があります。

   .. image:: img/omv/omv-network-location-3.png

   4. ``サインイン時に再接続する`` をチェックし、``完了`` ボタンをクリックします。

   .. image:: img/omv/omv-network-location-4.png
   
   5. これで NAS の共有フォルダにアクセスできるようになりました。

   .. image:: img/omv/omv-network-location-5.png

10. Macで共有フォルダにアクセスする
-------------------------------------

   1. ``移動`` メニューで、``サーバーに接続`` をクリックします。

   .. image:: img/omv/omv-mac-1.png

   2. 表示されたダイアログボックスで、Raspberry Pi の IP アドレス（例： ``smb://192.168.1.100``）、または Raspberry Pi のホスト名（例： ``smb://pi.local``）を入力します。

   .. image:: img/omv/omv-mac-2.png

   3. ``接続`` ボタンをクリックします。

   .. image:: img/omv/omv-mac-3.png

   4. 表示されたダイアログボックスで、先ほど作成したユーザー名とパスワードを入力します。``接続`` ボタンをクリックします。

   .. image:: img/omv/omv-mac-4.png

   5. これで NAS の共有フォルダにアクセスできるようになりました。

   .. image:: img/omv/omv-mac-5.png