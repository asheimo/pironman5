
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============

1. À propos des systèmes compatibles
-----------------------------------------------------------------------------------------------------------------------------------------------

Systèmes ayant passé les tests sur le Raspberry Pi 5 :

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. À propos du bouton d'alimentation
----------------------------------------------------------------------

Le bouton d'alimentation prolonge le bouton d'alimentation du Raspberry Pi 5 et fonctionne exactement comme le bouton d'alimentation du Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Arrêt**

  * Si vous exécutez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d'alimentation pour éteindre.
  * Si vous exécutez le système **Raspberry Pi OS Lite**, appuyez une seule fois sur le bouton d'alimentation pour initier un arrêt.
  * Pour forcer un arrêt brutal, maintenez le bouton d'alimentation enfoncé.

* **Mise sous tension**

  * Si la carte Raspberry Pi est éteinte, mais toujours alimentée, une seule pression permet de l'allumer à partir de l'état éteint.

* Si vous exécutez un système qui ne prend pas en charge un bouton d'arrêt, vous pouvez le maintenir enfoncé pendant 5 secondes pour forcer un arrêt brutal, et une seule pression pour l'allumer à partir de l'état éteint.

3. À propos du Raspberry Pi AI HAT+
--------------------------------------------------------------------------------------------------------------------------------------------------

Le Raspberry Pi AI HAT+ n'est pas compatible avec le Pironman 5.

   .. image::  img/output3.png
        :width: 400

Le Raspberry Pi AI Kit combine le Raspberry Pi M.2 HAT+ et le module accélérateur AI Hailo.

   .. image::  img/output2.jpg
        :width: 400

Vous pouvez détacher le module accélérateur AI Hailo du Raspberry Pi AI Kit et l'insérer directement dans le module NVMe PIP du Pironman 5 MAX.

   .. .. image::  img/output4.png
   ..      :width: 800

4. À propos des extrémités des tubes en cuivre du refroidisseur tour
--------------------------------------------------------------------------------------------------------------------------------------------------

Les tubes thermiques en forme de U en haut du refroidisseur tour sont comprimés pour faciliter le passage des tubes en cuivre à travers les ailettes en aluminium, ce qui fait partie du processus de production normal des tubes en cuivre.

   .. image::  img/tower_cooler1.png

5. Le PI5 ne démarre pas (LED rouge) ?
---------------------------------------------------------------------------------------

Ce problème peut être causé par une mise à jour du système, une modification de l'ordre de démarrage ou un chargeur d'amorçage corrompu. Vous pouvez essayer les étapes suivantes pour résoudre le problème :

#. Vérifiez la connexion de l'adaptateur USB-HDMI

   * Veuillez vérifier soigneusement si l'adaptateur USB-HDMI est solidement connecté au PI5.
   * Essayez de débrancher et de rebrancher l'adaptateur USB-HDMI.
   * Rebranchez ensuite l'alimentation et vérifiez si le PI5 démarre correctement.

#. Testez le PI5 à l'extérieur du boîtier

   * Si le rebranchement de l'adaptateur ne résout pas le problème :
   * Retirez le PI5 du boîtier Pironman 5.
   * Alimentez le PI5 directement avec l'adaptateur secteur (sans le boîtier).
   * Vérifiez s'il peut démarrer normalement.

#. Restaurez le chargeur d'amorçage

   * Si le PI5 ne démarre toujours pas, le chargeur d'amorçage peut être corrompu. Vous pouvez suivre ce guide : :ref:`update_bootloader_promax` et choisir de démarrer depuis la carte SD ou NVMe/USB.
   * Insérez la carte SD préparée dans le PI5, allumez-le et attendez au moins 10 secondes. Une fois la restauration terminée, retirez et reformatez la carte SD.
   * Ensuite, utilisez Raspberry Pi Imager pour flasher la dernière version de Raspberry Pi OS, réinsérez la carte et réessayez de démarrer.

6. L'écran OLED ne fonctionne pas ?
--------------------------------------------------------------------------

Si l'écran OLED n'affiche rien ou affiche incorrectement, suivez ces étapes de dépannage :

1. **Vérifiez la connexion de l'écran OLED**

   Assurez-vous que le câble FPC de l'écran OLED est correctement connecté.

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Oled-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

   .. todo 更新MP4

2. **Vérifiez la compatibilité du système d'exploitation**

   Assurez-vous d'exécuter un système d'exploitation compatible sur votre Raspberry Pi.

3. **Vérifiez l'adresse I2C**

   Exécutez la commande suivante pour vérifier si l'adresse I2C de l'OLED (0x3C) est reconnue :

   .. code-block:: shell

      sudo i2cdetect -y 1

   Si l'adresse n'est pas détectée, activez I2C en utilisant la commande suivante :

   .. code-block:: shell

      sudo raspi-config

4. **Redémarrez le service pironman5**

   Redémarrez le service `pironman5` pour voir si cela résout le problème :

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Vérifiez le fichier journal**

   Si le problème persiste, vérifiez le fichier journal pour les messages d'erreur et fournissez les informations au support client pour une analyse plus approfondie :

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

7. Le module NVMe PIP ne fonctionne pas ?
-----------------------------------------------------------------------------------

1. Assurez-vous que le câble FPC connectant le module NVMe PIP au Raspberry Pi 5 est solidement fixé.

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

   .. .. raw:: html

   ..     <div style="text-align: center;">
   ..         <video center loop autoplay muted style="max-width:90%">
   ..             <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
   ..             Your browser does not support the video tag.
   ..         </video>
   ..     </div>

.. todo 更新MP4

2. Confirmez que votre SSD est correctement fixé au module NVMe PIP.

3. Vérifiez l'état des LEDs du module NVMe PIP :

   Après avoir confirmé toutes les connexions, allumez le Pironman 5 MAX et observez les deux indicateurs sur le module NVMe PIP :

   * **LED PWR** : Doit être allumée.
   * **LED STA** : Doit clignoter pour indiquer un fonctionnement normal.

   .. image:: img/dual_nvme_pip_leds.png

   * Si la **LED PWR** est allumée mais que la **LED STA** ne clignote pas, cela indique que le SSD NVMe n'est pas reconnu par le Raspberry Pi.
   * Si la **LED PWR** est éteinte, court-circuitez les broches « Force Enable » sur le module. Si la **LED PWR** s'allume, cela pourrait indiquer un câble FPC desserré ou une configuration système non prise en charge pour NVMe.

   .. image:: img/dual_nvme_pip_j4.png

4. Confirmez que votre SSD NVMe a un système d'exploitation correctement installé. Référez-vous à : :ref:`install_the_os_promax`.

5. Si le câblage est correct et que le système d'exploitation est installé, mais que le SSD NVMe ne démarre toujours pas, essayez de démarrer à partir d'une carte Micro SD pour vérifier la fonctionnalité des autres composants. Une fois confirmé, passez à : :ref:`configure_boot_ssd_promax`.

Si le problème persiste après avoir effectué les étapes ci-dessus, veuillez envoyer un courriel à service@sunfounder.com. Nous répondrons dès que possible.

8. Les LEDs RGB ne fonctionnent pas ?
----------------------------------------------------------------------

#. Les deux broches sur l'Expanseur d'E/S au-dessus de J9 sont utilisées pour connecter les LEDs RGB à GPIO10. Assurez-vous que les cavaliers sur ces deux broches sont correctement en place.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vérifiez que le Raspberry Pi exécute un système d'exploitation compatible. Le Pironman 5 ne prend en charge que les versions suivantes :

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si vous avez installé un système d'exploitation non pris en charge, suivez le guide pour installer un système d'exploitation compatible : :ref:`install_the_os_promax`.

#. Exécutez la commande ``sudo raspi-config`` pour ouvrir le menu de configuration. Naviguez vers **3 Interface Options** -> **I3 SPI** -> **YES**, puis cliquez sur **OK** et **Finish** pour activer le SPI. Après avoir activé le SPI, redémarrez le Pironman 5.

Si le problème persiste après avoir effectué les étapes ci-dessus, veuillez envoyer un courriel à service@sunfounder.com. Nous répondrons dès que possible.

.. _promax_fan_faq:

9. Le ventilateur ne fonctionne pas / ne peut pas être contrôlé ?
--------------------------------------------------------------------------------------------------------------------------------------

Le Pro / MAX adopte la solution officielle de contrôle du ventilateur PWM du Raspberry Pi. Les trois ventilateurs de refroidissement sont directement contrôlés par le système Raspberry Pi et ne dépendent pas du service pironman5 (par conséquent, vous ne verrez pas d'options de contrôle du ventilateur dans l'outil de ligne de commande ou le tableau de bord).

**Tester si le ventilateur fonctionne correctement**

Vous pouvez contrôler manuellement le ventilateur en utilisant les commandes suivantes :

.. code-block:: bash

   pinctrl FAN_PWM op dl   # activer le ventilateur (actif bas)
   pinctrl FAN_PWM op dh   # désactiver le ventilateur (actif haut)
   pinctrl FAN_PWM a0      # mode automatique (contrôle par température système)

**Contrôle de la vitesse du ventilateur basé sur la température**

Le ventilateur PWM fonctionne dynamiquement, ajustant sa vitesse en fonction de la température du Raspberry Pi 5 :

* **En dessous de 50°C** : Ventilateur éteint (vitesse 0%).
* **À 50°C** : Ventilateur fonctionne à basse vitesse (vitesse 30%).
* **À 60°C** : Ventilateur augmente à vitesse moyenne (vitesse 50%).
* **À 67,5°C** : Ventilateur monte à haute vitesse (vitesse 70%).
* **À 75°C et plus** : Ventilateur fonctionne à pleine vitesse (vitesse 100%).

10. Comment réveiller l'écran OLED ?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pour économiser l'énergie et prolonger la durée de vie de l'écran, l'écran OLED s'éteint automatiquement après une période d'inactivité. Cela fait partie de la conception normale et n'affecte pas la fonctionnalité du produit.

.. note::

   Pour la configuration de l'écran OLED (comme l'activation/désactivation, le délai de mise en veille, la rotation, etc.), veuillez vous référer à : :ref:`promax_view_control_dashboard` ou :ref:`promax_view_control_commands`.

11. Comment désactiver le tableau de bord web ?
----------------------------------------------------------------------------------------------------------------------------------------------

Une fois que vous avez terminé l'installation du module ``pironman5``, vous pourrez accéder au :ref:`promax_view_control_dashboard`.

Si vous n'avez pas besoin de cette fonctionnalité et souhaitez réduire l'utilisation du CPU et de la RAM, vous pouvez désactiver le tableau de bord lors de l'installation de ``pironman5`` en ajoutant le drapeau ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si vous avez déjà installé ``pironman5``, vous pouvez supprimer le module ``dashboard`` et ``influxdb``, puis redémarrer pironman5 pour appliquer les modifications :

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. Le Pironman 5 MAX prend-il en charge les systèmes de jeu rétro ?
.. ----------------------------------------------------------------------------------------------------------------------------------------------
.. Oui, il est compatible. Cependant, la plupart des systèmes de jeu rétro sont des versions allégées qui ne peuvent pas installer et exécuter de logiciels supplémentaires. Cette limitation peut empêcher certains composants du Pironman 5 MAX, tels que l'écran OLED, les deux ventilateurs RGB et les 4 LEDs RGB, de fonctionner correctement car ces composants nécessitent l'installation des paquets logiciels du Pironman 5 MAX.

.. .. note::

..     Le système Batocera.linux est maintenant entièrement compatible avec le Pironman 5 MAX. Batocera.linux est une distribution de jeu rétro open-source et entièrement gratuite.

..     * :ref:`promax_install_batocera`
..     * :ref:`promax_set_up_batocera`

12. Comment contrôler les composants en utilisant la commande ``pironman5``
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Vous pouvez vous référer au tutoriel suivant pour contrôler les composants du Pironman 5 MAX en utilisant la commande ``pironman5``.

* :ref:`promax_view_control_commands`

13. Comment modifier l'ordre de démarrage du Raspberry Pi en utilisant des commandes
-----------------------------------------------------------------------------------------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l'ordre de démarrage en utilisant des commandes. Les instructions détaillées sont les suivantes :

* :ref:`configure_boot_ssd_promax`

14. Comment modifier l'ordre de démarrage avec Raspberry Pi Imager ?
-------------------------------------------------------------------------------------------------------------------------------------------------------

En plus de modifier le ``BOOT_ORDER`` dans la configuration EEPROM, vous pouvez également utiliser **Raspberry Pi Imager** pour changer l'ordre de démarrage de votre Raspberry Pi.

Il est recommandé d'utiliser une carte de rechange pour cette étape.

* :ref:`update_bootloader_promax`

15. Comment copier le système de la carte SD vers un SSD NVMe ?
-----------------------------------------------------------------------------------------------------------------------------------------------------

Si vous avez un SSD NVMe mais que vous n'avez pas d'adaptateur pour connecter votre NVMe à votre ordinateur, vous pouvez d'abord installer le système sur votre carte Micro SD. Une fois que le Pironman 5 MAX démarre avec succès, vous pouvez copier le système de votre carte Micro SD vers votre SSD NVMe. Les instructions détaillées sont les suivantes :

* :ref:`copy_sd_to_nvme_promax`

16. Comment retirer le film protecteur des plaques acryliques
---------------------------------------------------------------------------------------------------------------------------------------------------------

Deux panneaux acryliques sont inclus dans l'emballage, tous deux recouverts d'un film protecteur jaune/transparent sur les deux côtés pour éviter les rayures. Le film protecteur peut être un peu difficile à retirer. Utilisez un tournevis pour gratter doucement les coins, puis décollez soigneusement tout le film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _promax_openssh_powershell:

17. Comment installer OpenSSH via Powershell ?
------------------------------------------------------------------------------------------------------------------------------------------

Lorsque vous utilisez ``ssh <nom_utilisateur>@<nom_hôte>.local`` (ou ``ssh <nom_utilisateur>@<adresse_IP>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Cela signifie que votre système informatique est trop ancien et n'a pas `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé, vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la zone de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell``, et sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, la sortie suivante sera retournée.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation en utilisant la commande suivante.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Il vous indique maintenant que ``OpenSSH.Client`` a été installé avec succès.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. attention::

        Si l'invite ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien, et il vous est conseillé d'installer un outil SSH tiers, comme |link_putty|.

#. Maintenant, redémarrez PowerShell et continuez à l'exécuter en tant qu'administrateur. À ce stade, vous pourrez vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, où il vous sera demandé d'entrer le mot de passe que vous avez défini précédemment.

   .. image:: img/powershell_login.png

18. Si j'installe OMV, puis-je toujours utiliser les fonctions du Pironman5 ?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Oui, OpenMediaVault est installé sur le système Raspberry Pi. Veuillez suivre les étapes de :ref:`promax_set_up_pi_os` pour continuer la configuration.

19. La caméra Raspberry Pi ne fonctionne pas ?
------------------------------------------------------------------------------------

Lorsque la caméra ne fonctionne pas, 90 % des problèmes sont liés à la connexion du câble nappe ou au matériel de la caméra lui-même.

Tout d'abord, utilisez ``rpicam-hello --list-cameras`` pour confirmer si la caméra est détectée. Si elle est détectée avec succès, vous devriez voir un message similaire à ce qui suit :

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Si la caméra n'est pas détectée, vérifiez si le câble nappe est inversé ou pas complètement inséré. Si le problème persiste, essayez de remplacer le câble nappe ou le module caméra pour un test croisé.
