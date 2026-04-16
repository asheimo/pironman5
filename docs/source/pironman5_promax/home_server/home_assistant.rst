
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message






Configurer Home Assistant
======================================

Home Assistant est une plateforme d'automatisation domestique fonctionnant sur un hub central (Raspberry Pi, PC, etc.). Elle peut être utilisée pour contrôler et surveiller toutes sortes d'appareils, des lumières et thermostats aux caméras de sécurité et aux appareils électroménagers intelligents.

**Préparation**

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* Un Raspberry Pi capable d'exécuter Home Assistant.
* Une connexion Internet stable.
* Un compte sur Home Assistant Cloud (optionnel, mais recommandé pour l'accès à distance).

**Installation**

Ouvrez le terminal et entrez les commandes suivantes :

1. Installer Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installer Home Assistant

.. code-block:: bash

   sudo docker pull homeassistant/home-assistant

**Exécuter le conteneur Home Assistant**

Ici, nous utilisons Docker Compose pour exécuter Home Assistant. Vous pouvez considérer Docker Compose comme un « script d'automatisation ». Il écrit toutes les configurations (nom de l'image, ports, montages de volumes, variables d'environnement, etc.) dans un fichier ``docker-compose.yml``. Ensuite, avec une simple commande ``docker compose up -d``, Docker créera et démarrera automatiquement tous les conteneurs configurés selon ce « script ».

1. **Entrer dans le répertoire du projet** : Allez dans ce dossier.

   .. code-block:: bash

      cd ~/homeassistant

2. **Créer le fichier de configuration** : Dans le répertoire ``~/homeassistant``, créez un fichier nommé ``docker-compose.yml`` et copiez la configuration ci-dessus dedans.

   .. code-block:: bash

      sudo nano docker-compose.yml

3. Collez le contenu suivant dans le fichier ``docker-compose.yml`` :

   .. note:: Veuillez remplacer ``- TZ=Asia/Shanghai`` par votre fuseau horaire.

   .. code-block:: bash

      version: '3'
      services:
      homeassistant:
         image: ghcr.io/home-assistant/raspberrypi5-64-homeassistant:stable
         container_name: homeassistant
         restart: unless-stopped
         privileged: true
         network_mode: host
         environment:
            - TZ=Asia/Shanghai
         volumes:
            - ./config:/config

4. ``Ctrl+X`` pour quitter l'éditeur, puis appuyez sur ``Y`` pour enregistrer les modifications.

5. **Démarrer Home Assistant** : Dans le répertoire ``~/homeassistant``, exécutez la commande suivante. Docker Compose téléchargera automatiquement l'image et démarrera le conteneur.

   .. code-block:: bash

      sudo docker compose up -d

   * ``up`` : Crée et démarre les services.
   * ``-d`` : S'exécute en arrière-plan (mode détaché).

6. **Vérifier l'état d'exécution** :

    .. code-block:: bash

      docker compose ps

   Vous devriez voir l'état de ``homeassistant`` comme ``Up``.

7. **Afficher les journaux** (en cas de problèmes de démarrage) :

   .. code-block:: bash

      docker compose logs -f

8. Pour plus de commandes, veuillez consulter :

   .. code-block:: bash

      docker compose --help

**Configuration**

Maintenant, vous pouvez ouvrir le navigateur de votre ordinateur et entrer : ``http://<Adresse de votre Raspberry Pi>:8123`` pour accéder à Home Assistant.

.. image:: img/home_assistant/ha_welcome.png

Sélectionnez **CREATE MY SMART HOME**, puis créez votre compte.

.. image:: img/home_assistant/ha_onboarding.png

Suivez les invites pour choisir votre emplacement et d'autres configurations. Une fois terminé, vous accéderez au tableau de bord de Home Assistant.

.. image:: img/home_assistant/ha_overview.png
