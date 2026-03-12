.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez au cœur de l’univers Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l’aide de notre équipe et de la communauté.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Soyez parmi les premiers informés des nouveaux produits et aperçus.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et événements promotionnels pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_view_control_commands:

Contrôle via Commandes
========================================
En plus d’afficher les données du Pironman 5 MAX et de contrôler divers appareils via le tableau de bord, vous pouvez également utiliser des commandes pour les piloter.

.. note::

  * Pour le système **Home Assistant**, vous ne pouvez surveiller et contrôler le Pironman 5 MAX qu’à travers le tableau de bord, accessible à l’adresse ``http://<ip>:34001``.
  * Pour le système **Batocera.linux**, le contrôle du Pironman 5 MAX s’effectue uniquement via des commandes. Notez que toute modification de la configuration nécessite un redémarrage du service via la commande ``pironman5 restart`` pour être prise en compte.

Afficher les configurations de base
---------------------------------------

Le module ``pironman5`` propose des configurations de base pour le Pironman, que vous pouvez consulter à l’aide de la commande suivante :

.. code-block:: shell

  sudo pironman5 -c

Les configurations par défaut s’affichent ainsi :

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

Personnalisez ces paramètres selon vos besoins.

Utilisez ``pironman5`` ou ``pironman5 -h`` pour obtenir de l’aide.

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [--background [BACKGROUND]] [-rd]
                          [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]     
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]    
                          [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-od [OLED_DISK]]
                          [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]] [-vp [VIBRATION_SWITCH_PIN]]
                          [-vu [VIBRATION_SWITCH_PULL_UP]] [-os [OLED_SLEEP_TIMEOUT]]
                          [{start,restart,stop}]

  Pironman 5 MAX command line interface

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
    -vp [VIBRATION_SWITCH_PIN], --vibration-switch-pin [VIBRATION_SWITCH_PIN]
                          Vibration switch pin
    -vu [VIBRATION_SWITCH_PULL_UP], --vibration-switch-pull-up [VIBRATION_SWITCH_PULL_UP]
                          Vibration switch pull up True/False
    -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                          OLED sleep timeout in seconds





.. note::

  À chaque modification de l’état du service ``pironman5.service``, vous devez exécuter la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* Vérifiez l’état du programme ``pironman5`` à l’aide de l’outil ``systemctl`` :

  .. code-block:: shell

    sudo systemctl status pironman5.service

* Vous pouvez également consulter les fichiers journaux générés par le programme :

  .. code-block:: shell

    ls /var/log/pironman5/


Contrôle des LEDs RGB
----------------------
La carte dispose de 4 LEDs RGB WS2812 entièrement personnalisables. Vous pouvez les allumer ou les éteindre, changer leur couleur, ajuster leur luminosité, modifier le mode d'affichage, et régler la vitesse des effets.

.. note::

  Chaque modification de l’état de ``pironman5.service`` nécessite l'exécution de la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Pour allumer ou éteindre les LEDs RGB, utilisez ``true`` pour allumer et ``false`` pour éteindre :

.. code-block:: shell

  sudo pironman5 -re true

* Pour changer leur couleur, indiquez une valeur hexadécimale, par exemple ``fe1a1a`` :

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* Pour ajuster la luminosité (plage : 0 ~ 100%) :

.. code-block:: shell

  sudo pironman5 -rb 100

* Pour modifier le mode d’affichage RGB, choisissez parmi : ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` :

.. note::

  Si vous sélectionnez ``rainbow``, ``rainbow_reverse`` ou ``hue_cycle``, vous ne pourrez pas définir la couleur via ``pironman5 -rc``.

.. code-block:: shell

  sudo pironman5 -rs breathing

* Pour ajuster la vitesse des effets (plage : 0 ~ 100%) :

.. code-block:: shell

  sudo pironman5 -rp 80

* Par défaut, 4 LEDs RGB sont utilisées. Pour en connecter davantage, indiquez le nombre :

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

Contrôle des ventilateurs RGB
---------------------------------
La carte d’extension IO prend en charge jusqu’à deux ventilateurs 5V non-PWM, contrôlés simultanément.

.. note::

  Chaque modification de l’état de ``pironman5.service`` nécessite l'exécution de la commande suivante pour appliquer les changements :

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* Utilisez la commande suivante pour configurer le mode de fonctionnement des ventilateurs RGB, selon la température de déclenchement souhaitée.

Par exemple, le mode **1 : Performance** active les ventilateurs à partir de 50°C.


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet** : activation à 70°C  
* **3: Balanced** : activation à 67,5°C  
* **2: Cool** : activation à 60°C  
* **1: Performance** : activation à 50°C  
* **0: Always On** : les ventilateurs restent toujours allumés  

* Si la broche de contrôle des ventilateurs est connectée à une autre broche du Raspberry Pi, vous pouvez la modifier ainsi :

.. code-block:: shell

  sudo pironman5 -gp 18


**À propos du ventilateur principal**

Le ventilateur principal se connecte à un port dédié pour ventilateur PWM à 4 broches sur le Raspberry Pi 5. Sa stratégie de contrôle par défaut est un système de régulation intelligent à plusieurs niveaux, géré par le firmware, qui ajuste la vitesse en fonction de la température du CPU. Cela signifie que lorsque vous utilisez un ventilateur PWM officiel ou compatible et que vous le connectez correctement, le système ajustera automatiquement la vitesse du ventilateur en fonction des changements de température du CPU (il commence à fonctionner au-dessus de 50°C), sans aucune intervention manuelle de votre part.

Vérification de l’écran OLED
-----------------------------------

Une fois la bibliothèque ``pironman5`` installée, l’écran OLED affiche les informations CPU, RAM, utilisation du disque, température CPU et l’adresse IP du Raspberry Pi à chaque redémarrage.

Si l’écran OLED ne montre rien, vérifiez d’abord la connexion du câble FPC.

Vous pouvez ensuite consulter le journal du programme pour diagnostiquer le problème :

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

Ou vérifiez si l’adresse i2c 0x3C de l’écran OLED est détectée :

.. code-block:: shell

  i2cdetect -y 1

Vérification du récepteur infrarouge
---------------------------------------



* Installez le module ``lirc`` :

  .. code-block:: shell

    sudo apt-get install lirc -y

* Testez maintenant le récepteur IR en exécutant la commande suivante :

  .. code-block:: shell

    mode2 -d /dev/lirc0

* Une fois la commande lancée, appuyez sur un bouton de la télécommande, et son code s'affichera à l'écran.

