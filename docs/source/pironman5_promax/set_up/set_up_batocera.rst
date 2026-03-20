.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_batocera:

Batocera.linuxでの設定
=========================================================

Batocera.linux OSをインストールした場合は、SSH経由でこのシステムにリモートログインし、以下の手順に従って設定を完了できます。

#. システムが起動したら、sshを使用してPironman5にリモート接続します。Windowsの場合は **Powershell** を開き、Mac OS XとLinuxの場合は直接 **ターミナル** を開きます。

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. batoceraシステムのデフォルトのホスト名は ``batocera`` 、デフォルトのユーザー名は ``root`` 、パスワードは ``linux`` です。したがって、 ``ssh root@batocera.local`` と入力し、パスワード ``linux`` を入力してログインできます。

   .. image:: img/batocera_login.png
      :width: 90%

#. コマンド ``/etc/init.d/S92switch setup`` を実行し、メニュー設定ページに入ります。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 下矢印キーを使用して最後まで移動し、 **Pironman5** サービスを選択して有効化します。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. pironman5サービスを有効化した後、 **OK** を選択します。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. コマンド ``reboot`` を実行してPironman5を再起動します。

   .. code-block:: shell

      reboot

#. 再起動すると、 ``pironman5.service`` が自動的に起動します。Pironman 5 Pro MAXの主な設定は以下の通りです：
   
   * OLED画面には、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色でブリージングモードに点灯します。

これで、Pironman 5 Pro MAXを画面、ゲームコントローラー、ヘッドフォンなどに接続し、ゲームの世界に没頭できます。


.. note::

   この時点で、Pironman 5 Pro MAXのセットアップは正常に完了し、使用可能な状態になりました。
   
   コンポーネントの高度な制御については、 :ref:`control_commands_dashboard_promax` を参照してください。