.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _set_up_umbrel_promax:

Umbrel OSでの設定
======================================================================

Raspberry Pi 5にUmbrel OSをインストールした場合は、コマンドラインを使用してPironman 5 Pro MAXを設定する必要があります。詳細な手順は以下に示します：

#. Ethernetケーブルを使用してRaspberry Pi 5をネットワークに接続します。この手順は、Raspberry Piがインターネットにアクセスできることを確認するために不可欠です。

#. ブラウザで、 ``http://umbrel.local`` にアクセスします。ページが開かない場合は、ルーターでUmbrelデバイスのIPアドレスを確認してください（例： ``http://192.168.1.50`` ）。

   .. image:: img/umbrel_local.png

#. ユーザー名とパスワードを設定してUmbrelアカウントを作成します。このパスワードは将来Umbrelにリモートアクセスする際に使用されるため、忘れないようにしてください。

   .. image:: img/umbrel_account.png

#. **Next** をクリックしてUmbrelのセットアップを完了し、デスクトップ環境に入ります。

   .. image:: img/umbrel_desktop.png

#. ターミナルを開きます。デスクトップから **Settings** アイコンをクリックし、 **Advanced Settings** を選択して **Open** をクリックします。

   .. image:: img/umbrel_setting.png

#. **Open Terminal** をクリックします。

   .. image:: img/umbrel_open_terminal.png

#. Umbrel OS内または特定のアプリ内でターミナルを開くかを選択できます。どちらのオプションを選択しても、ターミナルインターフェースに移動します。

   .. image:: img/umbrel_terminal.png

#. GitHubからコードをダウンロードし、 ``pironman5`` モジュールをインストールします。

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. インストールが完了したら、以下のコマンドを入力してRaspberry Piを再起動します。

   .. code-block:: shell

      sudo reboot

#. 再起動すると、 ``pironman5.service`` が自動的に起動します。Pironman 5 Pro MAXの主な設定は以下の通りです：
   
   * OLED画面には、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色でブリージングモードに点灯します。


#. ``systemctl`` ツールを使用して、 ``pironman5.service`` の ``start``、 ``stop``、 ``restart``、または ``status`` の確認ができます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``： Pironman 5 Pro MAXの設定に変更を加えた場合に、このコマンドを使用して適用します。
   * ``start/stop``： ``pironman5.service`` を有効化または無効化します。
   * ``status``： ``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   この時点で、Pironman 5 Pro MAXのセットアップは正常に完了し、使用可能な状態になりました。
   
   コンポーネントの高度な制御については、 :ref:`control_commands_dashboard_promax` を参照してください。