.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Raspberry Pi OSのインストール
================================================================================

Micro SDカードまたはNVMe SSDのいずれかを使用できるかどうかに応じて、インストール方法を選択できます。

**Micro SDカードのみを使用する場合**

  Micro SDカードのみを使用する場合は、以下の最初の方法に従ってください。

**M.2 NVMe SSDを使用する場合**

  * **M.2 NVMe SSDエンクロージャアダプター** をお持ちの場合は、アダプターを使用してSSDをコンピューターに接続し、2番目の方法でOSをインストールできます。

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * 上記のアダプターをお持ちでない場合は、最初の方法でMicro SDカードにOSをインストールし、3番目の方法でシステムをMicro SDカードからM.2 NVMe SSDにコピーできます。

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi