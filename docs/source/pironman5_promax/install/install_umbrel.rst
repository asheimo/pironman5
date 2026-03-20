Installing Umbrel OS
============================================

Umbrelは、オープンソースのセルフホスト型ホームサーバープラットフォーム/OSです。これを使用すると、独自のBitcoinノードを実行したり、ワンクリックでセルフホスト型のさまざまなアプリをインストールしたり、ハードウェアを個人用のホームクラウドに変えることができます。自己管理とプライバシーを重視する方にとって、最適な入門方法です。

**必要なもの**

* パーソナルコンピューター
* NVMe SSD
* NVMe to USB アダプター
* Micro SDカードとリーダー

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. NVMe SSDへのOSインストール
-----------------------------------

これで、 **NVMe SSD** にオペレーティングシステムをインストールする準備が整いました。
以下の手順に注意深く従ってください。このガイドは初心者向けに書かれており、簡単に理解できます。

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. 最新の **Umbrel OS** イメージをダウンロードし、ファイルを展開します。特定のバージョンを使用したい場合は、|link_umbrel_release| ページにアクセスすることもできます。

   * :download:`最新のUmbrel OSイメージ <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. **NVMe to USBアダプター** を使用して **NVMe SSD** をコンピューターに挿入します。

#. **Raspberry Pi Imager** を開きます。 **Device** 画面で、リストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

#. **OS** セクションに移動し、下部までスクロールして **Use custom** を選択します。

   .. image:: img/imager_use_custom.png
      :width: 90%

#. 先ほどダウンロードして展開した **Umbrel OSイメージファイル** を選択し、 **開く** をクリックします。

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. **Next** をクリックして続行します。

   .. image:: img/imager_custom_next.png
      :width: 90%

#. **Storage** セクションで、 **NVMe SSD** を選択します。NVMe SSDを選択していることを確認し、コンピューター上の他のドライブを誤って選択しないようにしてください。

   .. image:: img/nvme_storage.png
      :width: 90%

#. すべての設定を慎重に確認し、 **WRITE** をクリックします。

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. NVMe SSDに既にデータが存在する場合、Raspberry Pi Imagerはすべてのデータが消去されるという警告を表示します。正しいドライブが選択されていることを再確認し、 **I UNDERSTAND, ERASE AND WRITE** をクリックします。

   .. image:: img/imager_erase.png
      :width: 90%

#. **“Write Complete”** メッセージが表示されたら、イメージの書き込みと検証が正常に完了しています。

   .. image:: img/imager_umbrel_finish.png
      :width: 90%