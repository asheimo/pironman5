.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message





Configurer Plex
=======================================

Plex est une plateforme de serveur multimédia puissante qui vous permet d'organiser, de diffuser et d'accéder à vos films, émissions de télévision, musique et photos sur plusieurs appareils. En installant Plex sur la série Pironman5 alimentée par Raspberry Pi, vous pouvez créer un centre multimédia domestique abordable et économe en énergie qui fonctionne 24h/24 et 7j/7. La taille compacte du Raspberry Pi, sa faible consommation d'énergie et sa flexibilité en font un excellent choix pour héberger Plex, transformant votre Pi en un hub de divertissement personnel accessible depuis votre réseau domestique ou même à distance.

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

4. Après le démarrage de votre Raspberry Pi, ouvrez un navigateur web et visitez l'adresse de votre Portainer : ``http://<adresse-ip-de-votre-rpi>:9443``.

5. Par défaut, vous pourriez voir un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé non émis par une autorité de certification (CA) connue. La plupart des navigateurs web afficheront un tel avertissement. Dans ce cas, vous pouvez l'ignorer en toute sécurité, accepter le risque et continuer.

   .. image:: img/home_server_app/private_save.png

#. Lors de votre première connexion, il vous sera demandé de définir un mot de passe administrateur.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Après avoir créé le compte administrateur, vous entrerez dans l'interface Portainer. Dans la barre de navigation de gauche, allez dans **Setting -> General**, trouvez **App Templates**, et entrez l'URL suivante dans le champ : ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Cliquez sur **Save Application Settings**. La configuration prendra environ 10 secondes.

**Installer Plex**

1. Dans la barre de navigation de gauche, cliquez sur **Home -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Allez dans **Templates -> Application**. Dans la barre de recherche en haut à droite, tapez *nextcloud* et cliquez dessus.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

#. Définissez le mode réseau sur **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. Développez **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. Dans la section **volume mapping**, configurez les chemins de stockage pour vos fichiers multimédia et accordez à Plex les autorisations de lecture/écriture. Les chemins par défaut sont ``/portainer/TV`` et ``/portainer/Movies``, tous deux avec accès en lecture/écriture activé.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. Cliquez sur **Deploy** et attendez que Plex termine l'installation.

**Configurer le serveur Plex**

1. Ouvrez votre navigateur et entrez : ``http://<votre_ip>:32400/web``. Vous devriez maintenant voir l'interface Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Ignorez l'offre d'abonnement premium.

3. Ensuite, vous verrez l'écran **Server Setup**. Vous pouvez cocher *Allow me to access my media outside my home*. Pour l'instant, il est recommandé de laisser cela décoché et de le configurer plus tard si nécessaire.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Il vous sera alors demandé d'organiser vos médias. Vous pouvez choisir *Skip* et ajouter des médias plus tard via les paramètres. Cependant, il est recommandé d'ajouter directement les chemins de stockage que vous avez configurés dans le mappage de volumes de Portainer afin que Plex puisse automatiquement scanner et importer vos médias.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Sélectionnez le type de votre bibliothèque multimédia, donnez un nom à votre bibliothèque et choisissez la langue.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Ajoutez des dossiers. Localisez les chemins de stockage des médias que vous avez définis précédemment et cliquez sur **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Cliquez sur **Finish**. Votre serveur Plex sur Raspberry Pi est maintenant entièrement configuré.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Vous devriez maintenant voir vos fichiers multimédia affichés sur la page d'accueil du serveur Plex.

   .. image:: img/home_server_app/plex_index.png