.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





Batocera OSのインストール
=============================================

以下のチュートリアルに従って、システムをMicro SDカードにインストールします。


**必要なもの**

* パーソナルコンピューター
* Micro SDカードとリーダー

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. OSをmicroSDカードにインストールする
------------------------------------------------


.. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>   


1. |shared_link_batocera_linux| のウェブサイトから最新バージョンのOSをダウンロードします。

2. カードリーダーを使用してmicroSDカードをコンピューターに挿入します。
   続行する前に、カード上の重要なデータは消去されるため、バックアップしてください。

   .. image:: img/insert_sd.png
      :width: 90%

3. **Raspberry Pi Imager** が開くと、 **Device** ページが表示されます。
   リストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

4. **OS** セクションに移動し、ページの下部までスクロールして **Use custom** を選択します。

   .. image:: img/imager_use_custom.png
      :width: 90%

5. ダウンロードした **batocera-bcmxxxxxxx.img.gz** ファイルを選択し、 **開く** をクリックします。

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. **Storage** セクションで、microSDカードを選択します。
   安全のため、他のUSBストレージデバイスを抜いて、リストにmicroSDカードのみが表示されるようにすることをお勧めします。

   .. image:: img/imager_storage.png
      :width: 90%

#. **NEXT** をクリックし、直接 **書き込み** に進みます。ここでOSがmicroSDカードに書き込まれます。


   .. image:: img/imager_betocera_write.png
      :width: 90%

#. **“Write Successful”** のポップアップが表示されたら、イメージの書き込みと検証が完了しています。これでmicroSDカードを安全に取り外し、Raspberry Piを起動するために使用できます。

   .. image:: img/imager_betocera_finish.png
      :width: 90%