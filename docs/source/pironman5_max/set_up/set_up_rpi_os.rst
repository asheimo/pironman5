.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances et vos projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes techniques et après-vente grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des conseils et tutoriels pour renforcer vos compétences.
    - **Avant-premières exclusives** : Profitez d’un accès anticipé aux annonces et démonstrations de nouveaux produits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et offres promotionnelles pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_set_up_pi_os:

Configuration sur Raspberry Pi/Ubuntu/Kali/Homebridge OS
===================================================================


.. image:: ../img/pironman5_max.jpg
    :width: 400
    :align: center
    


Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 MAX en utilisant la ligne de commande. Vous trouverez ci-dessous des tutoriels détaillés.

.. note::

  Avant de procéder à la configuration, vous devez démarrer et vous connecter à votre Raspberry Pi.  
  Si vous n’êtes pas sûr de la procédure de connexion, vous pouvez visiter le site officiel de Raspberry Pi : |link_rpi_get_start|.


Configuration de l’arrêt pour couper l’alimentation GPIO
-------------------------------------------------------------------------------

Pour éviter que l’écran OLED et les ventilateurs RGB, alimentés par le GPIO du Raspberry Pi, restent actifs après l’arrêt, il est essentiel de configurer le Raspberry Pi afin de désactiver l’alimentation GPIO.

#. Ouvrez l’outil de configuration EEPROM :

   .. code-block::

      sudo raspi-config

#. Accédez à **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Sélectionnez **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Enregistrez les modifications. Il vous sera demandé de redémarrer afin que les nouveaux paramètres prennent effet.

Download e installazione del modulo ``pironman5``
-----------------------------------------------------------

.. note::

   Per i sistemi “lite”, installa inizialmente strumenti come ``git``, ``python3``, ``pip3``, ``setuptools``, ecc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procedi a scaricare il codice da GitHub e installare il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Dopo un’installazione riuscita, è necessario riavviare il sistema per attivare l’installazione. Segui il prompt a schermo per riavviare.

   Al riavvio, il servizio ``pironman5.service`` verrà avviato automaticamente.  
   Ecco le configurazioni principali di Pironman 5 MAX:
   
   * Lo schermo OLED mostra CPU, RAM, utilizzo del disco, temperatura della CPU e indirizzo IP del Raspberry Pi.

   .. note:: Lo schermo OLED può spegnersi automaticamente dopo un periodo di inattività per risparmiare energia.  
      Puoi toccare delicatamente il case per attivare il sensore di vibrazione e riaccendere lo schermo.

   * Quattro LED WS2812 RGB si illumineranno di blu con un effetto di respirazione.  
   * Le ventole RGB sono impostate di default su **Always On**. Per informazioni sull’impostazione delle temperature di attivazione, consulta :ref:`cc_control_fan_max`.

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` del servizio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa questo comando per applicare eventuali modifiche alle impostazioni di Pironman 5 MAX.  
   * ``start/stop``: Abilita o disabilita il servizio ``pironman5.service``.  
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

.. note::

   A questo punto hai configurato con successo il Pironman 5 MAX ed è pronto per l’uso.  
   Per il controllo avanzato dei suoi componenti, consulta :ref:`control_commands_dashboard_max`.
