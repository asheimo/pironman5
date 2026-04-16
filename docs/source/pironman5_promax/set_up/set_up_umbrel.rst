
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _set_up_umbrel_promax:

Configuration sur Umbrel OS
======================================================================

Si vous avez installé Umbrel OS sur votre Raspberry Pi 5, vous devrez configurer le Pironman 5 Pro MAX en utilisant la ligne de commande. Des instructions détaillées sont fournies ci-dessous :

#. Connectez votre Raspberry Pi 5 à votre réseau à l'aide d'un câble Ethernet. Cette étape est essentielle pour garantir que votre Raspberry Pi a accès à Internet.

#. Dans votre navigateur, visitez : ``http://umbrel.local``. Si la page ne s'ouvre pas, vérifiez sur votre routeur l'adresse IP du périphérique Umbrel, par exemple : ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Créez votre compte Umbrel en définissant un nom d'utilisateur et un mot de passe. Ce mot de passe sera utilisé pour les futurs accès distants à Umbrel, alors assurez-vous de vous en souvenir.

   .. image:: img/umbrel_account.png

#. Cliquez sur **Suivant** pour terminer la configuration d'Umbrel et accéder à l'environnement de bureau.

   .. image:: img/umbrel_desktop.png

#. Ouvrez le Terminal. Depuis le bureau, cliquez sur l'icône **Paramètres**, puis sélectionnez **Paramètres avancés** et cliquez sur **Ouvrir**.

   .. image:: img/umbrel_setting.png

#. Cliquez sur **Ouvrir le terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Vous pouvez choisir d'ouvrir le Terminal dans Umbrel OS ou dans une application spécifique. L'une ou l'autre option vous mènera à l'interface du terminal.

   .. image:: img/umbrel_terminal.png

#. Procédez au téléchargement du code depuis GitHub et à l'installation du module ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Après la fin de l'installation, entrez la commande suivante pour redémarrer votre Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Au redémarrage, le ``pironman5.service`` démarrera automatiquement. Voici les principales configurations du Pironman 5 Pro MAX :

   * L'écran OLED affiche le CPU, la RAM, l'utilisation du disque, la température du CPU et l'adresse IP du Raspberry Pi.
   * Quatre LEDs RGB WS2812 s'allumeront en bleu avec un mode de respiration.

#. Vous pouvez utiliser l'outil ``systemctl`` pour ``démarrer``, ``arrêter``, ``redémarrer`` ou vérifier le ``statut`` de ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart`` : Utilisez cette commande pour appliquer les modifications apportées aux paramètres du Pironman 5 Pro MAX.
   * ``start/stop`` : Activez ou désactivez le ``pironman5.service``.
   * ``status`` : Vérifiez l'état de fonctionnement du programme ``pironman5`` en utilisant l'outil ``systemctl``.

.. note::

   À ce stade, vous avez configuré avec succès le Pironman 5 Pro MAX, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_promax`.
