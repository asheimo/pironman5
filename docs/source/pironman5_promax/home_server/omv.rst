
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





.. _promax_omv_5_promax:


Configurer OpenMediaVault
=====================================

.. attention::

   OpenMediaVault **ne prend pas en charge** l'installation sur le bureau Raspberry Pi OS.

   ⚠️ **Seules les versions Lite de Raspberry Pi OS 11 (Bullseye) et 12 (Bookworm) sont supportées.**

   Veuillez vous assurer d'avoir installé le bon système d'exploitation et configuré le réseau.
   La procédure ici est cohérente avec :ref:`install_os_sd_rpi_promax`, mais lors de la sélection d'une image, veuillez choisir Raspberry Pi OS Lite dans Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (abrégé en OMV) est un système d'exploitation NAS (Network Attached Storage) open-source basé sur Debian Linux, conçu pour les utilisateurs domestiques et les environnements de petits bureaux, visant à simplifier la gestion du stockage et à fournir des fonctionnalités de services réseau riches.

Veuillez suivre ces étapes pour installer OpenMediaVault sur votre Raspberry Pi :

1. Connectez-vous à votre Raspberry Pi en utilisant SSH
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

   Entrez la commande suivante dans le terminal :

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Si vous utilisez Windows, utilisez PuTTY ou un autre client SSH pour vous connecter à votre Raspberry Pi.

2. Installer OpenMediaVault
--------------------------------------------------------------

   Entrez la commande suivante dans le terminal :

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install
      chmod +x install
      sudo ./install -n

   Cela téléchargera et exécutera le script d'installation d'OpenMediaVault. Ne redémarrez pas votre Raspberry Pi après l'installation.

3. Accéder à OpenMediaVault
---------------------------------------------------------------

   Entrez l'URL suivante dans votre navigateur pour accéder à OpenMediaVault :

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Si vous ne pouvez pas accéder à l'URL ci-dessus, essayez d'utiliser l'adresse IP à la place, par exemple, http://192.168.1.100.

   Vous verrez une page de connexion, connectez-vous en utilisant le nom d'utilisateur et le mot de passe par défaut. Le nom d'utilisateur par défaut est ``admin`` et le mot de passe est ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Après vous être connecté, vous verrez l'interface principale d'OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Vous avez maintenant installé et accédé avec succès à OpenMediaVault, vous pouvez commencer à configurer et gérer votre stockage.

4. Configurer le RAID (Optionnel)
-----------------------------------------------------------------------------------------------------------

   Le RAID NVMe est une solution de stockage qui combine plusieurs disques SSD NVMe en utilisant la technologie RAID, visant à maximiser les performances à haute vitesse du protocole NVMe et les fonctionnalités de redondance/amélioration des performances du RAID. Les modes courants incluent RAID 0, 1, 5, 10, etc. Pour les SSD NVMe doubles, les modes RAID 0 et RAID 1 sont les plus couramment utilisés.

   * RAID 0 est une technologie de répartition qui divise les données en plusieurs bandes et distribue ces bandes sur plusieurs disques durs, permettant ainsi d'atteindre des vitesses de lecture/écriture plus élevées. RAID 0 ne fournit pas de protection par redondance, donc si l'un des disques durs tombe en panne, toutes les données seront perdues.

   * RAID 1 est une technologie de miroir qui copie les données sur plusieurs disques durs, fournissant ainsi une protection par redondance. Les vitesses de lecture/écriture du RAID 1 dépendent de la vitesse d'un seul disque dur, car les données doivent être lues sur plusieurs disques durs. Si l'un des disques durs tombe en panne, les autres peuvent continuer à fournir les données.

   .. note:: Montez au moins 2 disques pour le RAID 0 ou RAID 1. Dans le RAID 0, la capacité du volume RAID sera la somme des capacités de tous les disques. Dans le RAID 1, la capacité du volume RAID sera la même que la capacité du plus petit disque.

   1. Dans le menu ``System``, cliquez sur l'option ``Plugins``, recherchez le plugin ``openmediavault-md`` et installez-le.

   .. image:: img/omv/omv-raid-1.png

   2. Dans le menu ``Storage``, cliquez sur l'option ``Disks``, effacez deux SSD.

   .. image:: img/omv/omv-raid-2.png

   3. Veuillez noter que cette action effacera toutes les données des disques durs, assurez-vous d'avoir sauvegardé toutes les données importantes.

   .. image:: img/omv/omv-raid-3.png

   4. Le mode d'effacement ``QUICK`` est suffisant.

   .. image:: img/omv/omv-raid-4.png

   5. Entrez dans l'onglet ``Multiple Device``, cliquez sur ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. Dans l'option Level, vous pouvez choisir Stripe (RAID 0) ou Mirror (RAID 1). Dans l'option Devices, sélectionnez les disques durs que vous venez d'effacer. Cliquez sur ``Save`` et attendez la fin de la configuration RAID.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Si un rapport d'erreur (500 - Internal Server Error) apparaît, essayez de redémarrer le système OMV.

   7. Appliquez la configuration en cliquant sur le bouton ``Apply``.

   .. image:: img/omv/omv-raid-7.png

   8. Une fois la configuration RAID terminée, vous devez attendre que l'état du RAID soit à ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. Une fois la configuration RAID terminée, vos disques durs sont maintenant en configuration RAID 0 ou RAID 1, et vous pouvez les utiliser comme un seul périphérique de stockage.

5. Configurer le stockage
---------------------------------------------------------

   Dans l'interface principale d'OpenMediaVault, cliquez sur l'option ``Storage`` dans le menu de gauche. Sur la page ``Storage``, cliquez sur l'onglet ``Disks``. Sur la page ``Disks``, vous verrez tous les disques de votre Raspberry Pi. Assurez-vous que votre NVMe PIP a un disque dur connecté.

   .. image:: img/omv/omv-disk.png

   1. Dans la barre latérale, cliquez sur l'option ``File System``. Créez et montez un système de fichiers. Choisissez ``ext4`` comme type de système de fichiers.

   .. image:: img/omv/omv-mount.png

   2. Sélectionnez le périphérique, et sauvegardez.

   .. note:: Si vous avez configuré le RAID, vous verrez le périphérique RAID dans la liste. Sélectionnez-le et sauvegardez.

   .. image:: img/omv/omv-mount-2.png

   3. Une fenêtre apparaîtra, vous informant que le système de fichiers est en cours de création, veuillez patienter un moment.

   .. image:: img/omv/omv-mount-3.png

   4. Une fois terminé, vous entrerez dans l'interface ``Mount``, sélectionnez le système de fichiers que vous venez de créer, et montez-le sur votre Raspberry Pi.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Si vous utilisez deux disques durs (et pas de RAID), vous devez répéter les étapes ci-dessus pour également monter le deuxième disque dur sur votre Raspberry Pi.

   5. Après le montage, veuillez appliquer, et vous pourrez voir les données sur vos disques durs dans le système de fichiers.

   .. image:: img/omv/omv-mount-5.png

   À ce stade, vous avez configuré avec succès OpenMediaVault et monté vos disques durs. Vous pouvez maintenant utiliser OpenMediaVault pour gérer votre stockage.

6. Créer un dossier partagé
-----------------------------------------------------------------------------------------------------------

   1. Sur la page ``Storage``, allez dans l'onglet ``Shared Folders``. Et cliquez sur le bouton ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. Sur la page ``Create Shared Folder``, entrez le nom du dossier partagé, sélectionnez le disque dur que vous voulez partager, le chemin du dossier partagé, et définissez les permissions du dossier partagé. Cliquez ensuite sur le bouton ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Vous pouvez maintenant voir le dossier partagé que vous venez de créer. Confirmez qu'il est correct, puis appliquez.

   .. image:: img/omv/omv-share-3.png

   Vous avez maintenant créé avec succès un dossier partagé.

7. Créer un nouvel utilisateur
-----------------------------------------------------------------------------------------------------------

   Pour accéder au dossier, nous devons créer un nouvel utilisateur, veuillez suivre ces étapes :

   1. Sur la page ``User``, cliquez sur le bouton ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. Sur la page ``Create User``, entrez le nom d'utilisateur et le mot de passe du nouvel utilisateur, puis cliquez sur le bouton ``Save``.

   .. image:: img/omv/omv-user-2.png

   Vous avez maintenant créé avec succès un nouvel utilisateur.

8. Définir les permissions pour le nouvel utilisateur
-----------------------------------------------------------------------------------------------------------

   1. Sur la page ``Shared Folders``, cliquez sur le dossier partagé que vous venez de créer. Cliquez ensuite sur le bouton ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. Sur la page ``Permissions``, définissez les permissions. Cliquez ensuite sur le bouton ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Une fois terminé, cliquez sur le bouton ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Vous pouvez maintenant utiliser ce nouvel utilisateur pour accéder à votre dossier partagé.

9. Configurer le service SMB
-----------------------------------------------------------------------------------------------------------

   1. Sur la page ``Services``, trouvez l'onglet ``SMB/CIFS`` > ``Setting``. Cochez l'option ``Enable``. Cliquez ensuite sur le bouton ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Appliquez les modifications en cliquant sur le bouton ``Apply``.

   .. image:: img/omv/omv-smb-2.png

   3. Entrez dans la page ``Shares``, cliquez sur le bouton ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. Sur la page ``Create Share``, sélectionnez le chemin du dossier partagé. Cliquez ensuite sur le bouton ``Save``. Accessoirement, il y a de nombreuses options sur cette page que vous pouvez configurer selon vos besoins.

   .. image:: img/omv/omv-smb-4.png

   5. Cliquez sur ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Vous avez maintenant configuré avec succès le service SMB. Vous pouvez maintenant utiliser le protocole SMB pour accéder à votre dossier partagé.

10. Accéder au dossier partagé sur Windows
-----------------------------------------------------------------------------------------------------------

   1. Ouvrez ``Ce PC``, puis cliquez sur ``Mapper un lecteur réseau``.

   .. image:: img/omv/omv-network-location-1.png

   2. Dans la boîte de dialogue qui apparaît, entrez l'IP du Raspberry Pi dans le champ ``Dossier``, par exemple, ``\\192.168.1.100\``, ou le nom d'hôte du Raspberry Pi, par exemple, ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Cliquez sur le bouton Parcourir, puis sélectionnez le dossier partagé auquel vous voulez accéder. Pendant ce processus, vous devrez entrer le nom d'utilisateur et le mot de passe que vous avez créés précédemment.

   .. image:: img/omv/omv-network-location-3.png

   4. Cochez « Reconnecter à l'ouverture de session », et cliquez sur le bouton ``Terminer``.

   .. image:: img/omv/omv-network-location-4.png

   5. Vous pouvez maintenant accéder au dossier partagé NAS.

   .. image:: img/omv/omv-network-location-5.png

10. Accéder au dossier partagé sur Mac
-----------------------------------------------------------------------------------------------------------

   1. Dans le menu ``Aller``, cliquez sur ``Se connecter au serveur``.

   .. image:: img/omv/omv-mac-1.png

   2. Dans la boîte de dialogue qui apparaît, entrez l'IP du Raspberry Pi, comme ``smb://192.168.1.100``, ou le nom d'hôte du Raspberry Pi, comme ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Cliquez sur le bouton ``Connecter``.

   .. image:: img/omv/omv-mac-3.png

   4. Dans la boîte de dialogue qui apparaît, entrez le nom d'utilisateur et le mot de passe que vous avez créés précédemment. Cliquez sur le bouton ``Connecter``.

   .. image:: img/omv/omv-mac-4.png

   5. Vous pouvez maintenant accéder au dossier partagé NAS.

   .. image:: img/omv/omv-mac-5.png
