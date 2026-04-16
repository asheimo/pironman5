
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Installation d'Umbrel OS
============================================

Umbrel est une plateforme/système d'exploitation open-source et auto-hébergé qui vous permet d'exécuter votre propre nœud Bitcoin, d'installer une variété d'applications auto-hébergées en un clic — et de transformer votre matériel en votre cloud personnel domestique. C'est une excellente façon de commencer avec l'auto-gardiennage et la confidentialité.

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de carte

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installer le système d'exploitation sur le SSD NVMe
-------------------------------------------------------------------------

Vous êtes maintenant prêt à installer le système d'exploitation sur votre **SSD NVMe**.
Suivez simplement attentivement les étapes ci-dessous — ce guide est écrit pour les débutants et est facile à suivre.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Versions d'Umbrel OS</a>

#. Téléchargez la dernière image **Umbrel OS** et extrayez le fichier. Si vous souhaitez utiliser une version spécifique, vous pouvez également visiter la page |link_umbrel_release|.

   * :download:`Dernière image Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Insérez le **SSD NVMe** dans votre ordinateur à l'aide d'un **adaptateur NVMe vers USB**.

#. Ouvrez **Raspberry Pi Imager**. Sur l'écran **Périphérique**, sélectionnez votre modèle **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

#. Allez dans la section **Système d'exploitation**, descendez en bas et sélectionnez **Utiliser un système personnalisé**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Sélectionnez le **fichier image Umbrel OS** que vous avez téléchargé et extrait précédemment, puis cliquez sur **Ouvrir**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Cliquez sur **Suivant** pour continuer.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. Dans la section **Stockage**, sélectionnez votre **SSD NVMe**. Assurez-vous de choisir le SSD NVMe et non un autre disque de votre ordinateur.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Vérifiez attentivement tous les paramètres, puis cliquez sur **ÉCRIRE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Si le SSD NVMe contient déjà des données, Raspberry Pi Imager vous avertira que toutes les données seront effacées. Vérifiez que le bon disque est sélectionné, puis cliquez sur **JE COMPRENDS, EFFACER ET ÉCRIRE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Lorsque le message **« Écriture réussie »** apparaît, l'image a été écrite et vérifiée avec succès.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%
