
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





Configurer NextCloudPi
=======================================

NextCloud est une solution de stockage cloud privé open-source, similaire à Google Drive ou Dropbox. Il peut être utilisé pour stocker des fichiers, partager des documents, synchroniser des photos et gérer des calendriers et des contacts.
Contrairement aux services cloud publics, NextCloud donne aux utilisateurs un contrôle total sur leurs données, ce qui le rend idéal pour les particuliers et les petites équipes qui accordent de l'importance à la confidentialité et à la sécurité des données.

La série Pironman5 alimentée par Raspberry Pi offre une faible consommation d'énergie, une taille compacte et des performances fiables, ce qui en fait un excellent choix pour un serveur cloud privé domestique. Combiné avec NextCloud, il peut servir de système NAS économique.

**Préparation**

* Carte MicroSD (16 Go+, Classe 10 recommandée)
* Système officiel Raspberry Pi OS (ou Raspberry Pi OS Lite)
* Connexion réseau stable (Ethernet filaire recommandé)
* Disque dur externe ou clé USB (pour le stockage étendu)

**Installer Portainer**

Ouvrez le terminal et entrez les commandes suivantes :

1. Installer Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installer Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Redémarrez votre Raspberry Pi. (Effectuez ensuite les étapes suivantes **IMMÉDIATEMENT**.)

4. Après le démarrage de votre Raspberry Pi, ouvrez un navigateur web et visitez l'adresse de votre Portainer : ``https://<adresse-ip-de-votre-rpi>:9443``.

5. Par défaut, vous verrez un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé non émis par une autorité de certification (CA) connue. La plupart des navigateurs web afficheront un avertissement concernant ces certificats. Dans ce cas, vous pouvez ignorer l'avertissement en toute sécurité, accepter le risque et continuer.

   .. image:: img/home_server_app/private_save.png

#. Lors de la première connexion, vous devrez définir un mot de passe administrateur.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Après avoir enregistré le compte administrateur, vous entrerez dans l'interface Portainer. Dans la barre de navigation de gauche, cliquez sur **Setting -> General**, trouvez **App Templates**, et entrez l'URL suivante dans le champ : ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Cliquez sur **Save Application Settings**. La configuration prendra environ 10 secondes.

**Installer NextCloud**

1. Dans la barre de navigation de gauche, cliquez sur **Home -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. Allez dans **Templates -> Application**. Dans la barre de recherche en haut à droite, tapez *nextcloud* et cliquez dessus.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Cliquez sur **Deploy the stack**, et attendez la fin du déploiement. Cela prend généralement environ deux minutes.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Une fois terminé, NextCloud sera installé.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**Utiliser NextCloud**

1. Ouvrez votre navigateur et visitez l'adresse de votre NextCloud : ``https://<adresse-ip-de-votre-rpi>:32768``.

.. note::

   De même, vous verrez un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé non émis par une autorité de certification (CA) connue. La plupart des navigateurs web afficheront un avertissement concernant ces certificats.
   Dans ce cas, vous pouvez ignorer l'avertissement en toute sécurité, accepter le risque et continuer.

   .. image:: img/home_server_app/private_save.png

2. Lors de la première connexion, vous devrez définir un mot de passe administrateur.

   .. image:: img/home_server_app/nc_admin_install.png

3. Après l'enregistrement, vous pouvez commencer à utiliser NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png
