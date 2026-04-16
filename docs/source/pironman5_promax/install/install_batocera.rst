
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





Installer le système d'exploitation Batocera
=============================================

Suivez le tutoriel ci-dessous pour installer le système sur votre carte Micro SD.

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de carte

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installer le système d'exploitation sur la carte microSD
---------------------------------------------------------------------------

.. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>

1. Téléchargez la dernière version du système d'exploitation sur le site web de |shared_link_batocera_linux|.

2. Insérez votre carte microSD dans votre ordinateur à l'aide d'un lecteur de carte.
   Avant de continuer, sauvegardez toutes les données importantes sur la carte, car elles seront effacées.

   .. image:: img/insert_sd.png
      :width: 90%

3. Lorsque **Raspberry Pi Imager** s'ouvre, vous verrez la page **Périphérique**.
   Sélectionnez votre modèle **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

4. Allez dans la section **Système d'exploitation**, descendez en bas de la page et sélectionnez **Utiliser un système personnalisé**.

   .. image:: img/imager_use_custom.png
      :width: 90%

5. Choisissez le fichier **batocera-bcmxxxxxxx.img.gz** que vous venez de télécharger et cliquez sur **Ouvrir**.

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. Dans la section **Stockage**, sélectionnez votre carte microSD.
   Par sécurité, il est recommandé de débrancher les autres périphériques de stockage USB afin que seule la carte microSD apparaisse dans la liste.

   .. image:: img/imager_storage.png
      :width: 90%

#. Cliquez sur **SUIVANT** et allez directement à **Écriture**, où le système d'exploitation est écrit sur la carte microSD.

   .. image:: img/imager_betocera_write.png
      :width: 90%

#. Lorsque la fenêtre contextuelle **« Écriture réussie »** apparaît, l'image a été entièrement écrite et vérifiée. Vous pouvez maintenant retirer la carte microSD en toute sécurité et l'utiliser pour démarrer votre Raspberry Pi.

   .. image:: img/imager_betocera_finish.png
      :width: 90%