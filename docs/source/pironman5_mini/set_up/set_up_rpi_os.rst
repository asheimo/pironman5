.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Obtenez de l’aide pour les problèmes techniques ou après-vente grâce à notre communauté et notre équipe.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus inédits.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos produits les plus récents.
    - **Promotions et cadeaux festifs** : Participez à des jeux-concours et des offres spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !


Configuration sur Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 Mini en utilisant la ligne de commande. Vous trouverez ci-dessous des tutoriels détaillés.

.. note::

  Avant de procéder à la configuration, vous devez démarrer et vous connecter à votre Raspberry Pi.  
  Si vous n’êtes pas sûr de la procédure de connexion, vous pouvez visiter le site officiel de Raspberry Pi : |link_rpi_get_start|.


Configuration de l’arrêt pour couper l’alimentation GPIO
------------------------------------------------------------------------------

Pour éviter que le ventilateur RGB, alimenté par le GPIO du Raspberry Pi, reste actif après l’arrêt, il est essentiel de configurer le Raspberry Pi afin de désactiver l’alimentation GPIO.

#. Ouvrez l’outil de configuration EEPROM :

   .. code-block::

      sudo raspi-config

#. Accédez à **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Sélectionnez **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Enregistrez les modifications. Il vous sera demandé de redémarrer afin que les nouveaux paramètres prennent effet.

Téléchargement et installation du module ``pironman5``
-----------------------------------------------------------

.. note::

   Pour les systèmes « lite », installez d’abord des outils comme ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procédez au téléchargement du code depuis GitHub et à l’installation du module ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Après une installation réussie, il est nécessaire de redémarrer le système pour activer l’installation. Suivez les instructions à l’écran pour redémarrer.

   Au redémarrage, le service ``pironman5.service`` sera lancé automatiquement.  
   Voici les principales configurations du Pironman 5 Mini :
   
   * Quatre LED WS2812 RGB s’allumeront en bleu avec un effet de respiration.
     
   .. note::
    
     * Les ventilateurs RGB sont configurés par défaut sur **Toujours activé**.  
       Pour définir des températures de déclenchement différentes, consultez :ref:`cc_control_fan_mini`.

#. Vous pouvez utiliser l’outil ``systemctl`` pour ``start``, ``stop``, ``restart`` ou vérifier le ``status`` du service ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart`` : Utilisez cette commande pour appliquer les modifications apportées aux paramètres du Pironman 5 Mini.  
   * ``start/stop`` : Active ou désactive le service ``pironman5.service``.  
   * ``status`` : Vérifie l’état de fonctionnement du programme ``pironman5`` à l’aide de l’outil ``systemctl``.

.. note::

   À ce stade, vous avez configuré avec succès le Pironman 5 Mini et il est prêt à être utilisé.  
   Pour un contrôle avancé de ses composants, consultez :ref:`control_commands_dashboard_mini`.
