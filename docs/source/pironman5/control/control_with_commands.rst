.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _view_control_commands:

Contrôler avec des Commandes
============================================
En plus de pouvoir consulter les données du Pironman 5 et de contrôler divers appareils via le tableau de bord, vous pouvez également utiliser des commandes pour les gérer.

.. note::

    * Pour le système **Home Assistant**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via le tableau de bord en ouvrant la page web à l'adresse ``http://<ip>:34001``.

.. * Pour le système **Batocera.linux**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via des commandes. Il est important de noter que toute modification de la configuration nécessite un redémarrage du service à l'aide de la commande ``pironman5 restart`` pour être prise en compte.

Consulter les Configurations de Base
-----------------------------------------

Le module ``pironman5`` propose des configurations de base pour Pironman, que vous pouvez consulter avec la commande suivante.

.. code-block:: shell

  sudo pironman5 -c

Les configurations standard apparaissent comme suit :

.. code-block:: 

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

Personnalisez ces configurations en fonction de vos besoins.

Utilisez ``pironman5`` ou ``pironman5 -h`` pour obtenir des instructions.

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]     
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]]
                          [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

  options:
    -h, --help            show this help message and exit
    -v, --version         Show version
    -c, --config          Show config
    -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                          Debug level
    --background [BACKGROUND]
                          Run in background
    -rd, --remove-dashboard
                          Remove dashboard
    -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                          Config path
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format without # (e.g. 00aabb)
    -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                          RGB brightness 0-100
    -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                          RGB style
    -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                          RGB speed 0-100
    -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                          RGB enable True/False
    -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                          RGB LED count int
    -u [{C,F}], --temperature-unit [{C,F}]
                          Temperature unit
    -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                          GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
    -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                          GPIO fan pin
    -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                          GPIO fan LED state on/off/follow
    -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                          GPIO fan LED pin
    -oe [OLED_ENABLE], --oled-enable [OLED_ENABLE]
                          OLED enable True/true/on/On/1 or False/false/off/Off/0
    -od [OLED_DISK], --oled-disk [OLED_DISK]
                          Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme
    -oi [OLED_NETWORK_INTERFACE], --oled-network-interface [OLED_NETWORK_INTERFACE]
                          Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or      
                          wlan0
    -or [{0,180}], --oled-rotation [{0,180}]
                          Set to rotate OLED display, 0, 180
    -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds




.. note::

  Chaque fois que vous modifiez l'état du ``pironman5.service``, vous devez utiliser la commande suivante pour que les changements de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Vérifiez l'état du programme ``pironman5`` à l'aide de l'outil ``systemctl``.

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Vous pouvez également consulter les fichiers journaux générés par le programme.

  .. code-block:: shell

    cat /opt/pironman5/log


Contrôler les LEDs RGB
------------------------------
La carte dispose de 4 LEDs RGB WS2812, offrant un contrôle personnalisable. Vous pouvez les allumer ou les éteindre, changer leur couleur, ajuster leur luminosité, modifier le mode d'affichage des LEDs RGB et régler la vitesse des changements.

.. note::

  Chaque fois que vous modifiez l'état du ``pironman5.service``, vous devez utiliser la commande suivante pour que les changements de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Pour modifier l'état d'activation ou de désactivation des LEDs RGB, utilisez ``true`` pour les allumer et ``false`` pour les éteindre.

.. code-block:: shell

  sudo pironman5 -re true

* Pour changer leur couleur, entrez les valeurs hexadécimales souhaitées, par exemple ``fe1a1a``.

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Pour changer la luminosité des LEDs RGB (plage: 0 ~ 100%) :

.. code-block:: shell

  sudo pironman5 -rb 100

* Pour changer le mode d'affichage des LEDs RGB, choisissez parmi les options: ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` :

.. note::

  Si vous réglez le mode d'affichage des LEDs RGB sur ``rainbow``, ``rainbow_reverse`` ou ``hue_cycle``, vous ne pourrez pas définir la couleur avec ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Pour modifier la vitesse de changement (plage: 0 ~ 100%) :

.. code-block:: shell

  sudo pironman5 -rp 80

* La configuration par défaut inclut 4 LEDs RGB. Connectez des LEDs supplémentaires et mettez à jour le nombre avec :

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan:

Contrôler les Ventilateurs RGB
---------------------------------------
La carte d'extension IO prend en charge jusqu'à deux ventilateurs non-PWM 5V. Les deux ventilateurs sont contrôlés ensemble. 

.. note::

  Chaque fois que vous modifiez l'état du ``pironman5.service``, vous devez utiliser la commande suivante pour que les changements de configuration prennent effet.

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Vous pouvez utiliser des commandes pour configurer le mode de fonctionnement des deux ventilateurs RGB. Ces modes déterminent les conditions dans lesquelles les ventilateurs RGB s'activent. 

Par exemple, si vous réglez le mode sur **1: Performance**, les ventilateurs RGB s'activeront à 50°C.

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Silencieux**: Les ventilateurs RGB s'activent à 70°C.
* **3: Équilibré**: Les ventilateurs RGB s'activent à 67,5°C.
* **2: Cool**: Les ventilateurs RGB s'activent à 60°C.
* **1: Performance**: Les ventilateurs RGB s'activent à 50°C.
* **0: Toujours activé**: Les ventilateurs RGB seront toujours activés.

* Si vous connectez la broche de contrôle du ventilateur RGB à d'autres broches du Raspberry Pi, vous pouvez utiliser la commande suivante pour changer le numéro de broche.

.. code-block:: shell

  sudo pironman5 -gp 18

**À propos du ventilateur principal**

Le ventilateur principal se connecte à un port dédié pour ventilateur PWM à 4 broches sur le Raspberry Pi 5. Sa stratégie de contrôle par défaut est un système de régulation intelligent à plusieurs niveaux, géré par le firmware, qui ajuste la vitesse en fonction de la température du CPU. Cela signifie que lorsque vous utilisez un ventilateur PWM officiel ou compatible et que vous le connectez correctement, le système ajustera automatiquement la vitesse du ventilateur en fonction des changements de température du CPU (il commence à fonctionner au-dessus de 50°C), sans aucune intervention manuelle de votre part.


Vérifier l'Écran OLED
-----------------------------------

Lorsque vous avez installé la bibliothèque ``pironman5``, l'écran OLED affiche l'utilisation du CPU, de la RAM, de l'espace disque, la température du CPU et l'adresse IP du Raspberry Pi, et cela s'affiche à chaque redémarrage.

Si votre écran OLED n'affiche aucun contenu, vous devez d'abord vérifier si le câble FPC de l'écran OLED est correctement connecté.

Ensuite, vous pouvez consulter le journal du programme pour identifier le problème avec la commande suivante.

.. code-block:: shell

  cat /var/log/pironman5/

Ou vérifiez si l'adresse i2c de l'OLED, 0x3C, est reconnue :

.. code-block:: shell

  i2cdetect -y 1

Vérifier le Récepteur Infrarouge
---------------------------------------


* Installez le module ``lirc`` :

  .. code-block:: shell

    sudo apt-get install lirc -y

* Testez maintenant le récepteur IR en exécutant la commande suivante. 

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Après avoir exécuté la commande, appuyez sur un bouton de la télécommande, et le code de ce bouton s'affichera.
