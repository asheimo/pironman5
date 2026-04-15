.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances et vos projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes techniques et après-vente grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des conseils et tutoriels pour renforcer vos compétences.
    - **Avant-premières exclusives** : Profitez d’un accès anticipé aux annonces et démonstrations de nouveaux produits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et offres promotionnelles pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !


FAQ
============

1. À propos des systèmes compatibles
-----------------------------------------------

Systèmes ayant passé le test sur le Raspberry Pi 5 :

.. image:: img/compitable_os.png
   :width: 600
   :align: center


2. À propos du bouton d’alimentation
-------------------------------------------

Le bouton d’alimentation étend le bouton Power du Raspberry Pi 5 et fonctionne exactement comme celui du Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Arrêt**

  * Si vous utilisez le système **Raspberry Pi Bookworm Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d’alimentation pour éteindre le système.  
  * Si vous utilisez le système **Raspberry Pi Bookworm Lite**, appuyez une fois sur le bouton d’alimentation pour initier l’arrêt.  
  * Pour un arrêt forcé, maintenez le bouton d’alimentation enfoncé.

* **Allumage**

  * Si la carte Raspberry Pi est arrêtée mais toujours alimentée, appuyez une fois sur le bouton pour la rallumer.

* Si vous utilisez un système qui ne prend pas en charge le bouton d’alimentation, maintenez-le enfoncé pendant 5 secondes pour forcer l’arrêt, puis appuyez une fois pour redémarrer.


3. À propos du Raspberry Pi AI HAT+
----------------------------------------------------------

Le Raspberry Pi AI HAT+ n’est pas compatible avec le Pironman 5.

   .. image::  img/output3.png
        :width: 400

Le kit Raspberry Pi AI combine le Raspberry Pi M.2 HAT+ et le module accélérateur AI Hailo.

   .. image::  img/output2.jpg
        :width: 400

Vous pouvez retirer le module accélérateur AI Hailo du kit Raspberry Pi AI et l’insérer directement dans le module NVMe PIP du Pironman 5 MAX.


4. À propos des extrémités des tubes en cuivre du refroidisseur tour
---------------------------------------------------------------------------

Les caloducs en forme de U situés en haut du refroidisseur tour sont sertis afin de permettre aux tubes en cuivre de passer à travers les ailettes en aluminium. Il s’agit d’une étape normale du processus de fabrication des tubes en cuivre.

   .. image::  img/tower_cooler1.png



5. Puis-je utiliser la fonction d'interrupteur à vibration du Pironman5 Max ?
----------------------------------------------------------------------------------------------------------------------------

À partir de la version v1.3.6, le réveil de l'écran OLED utilise le bouton d'alimentation. Vous devez retirer le cavalier de l'interrupteur à vibration pour éviter d'occuper les broches GPIO du Raspberry Pi et prévenir d'éventuels conflits. Veuillez vérifier si ce cavalier est présent ; si ce n'est pas le cas, veuillez ignorer cet avis.

.. image:: /pironman5_max/img/remove_vib_jumper.jpg


6. L’écran OLED ne fonctionne pas ?
------------------------------------------

.. note:: L’écran OLED peut s’éteindre automatiquement après une période d’inactivité afin d’économiser de l’énergie. Vous pouvez tapoter légèrement sur le boîtier pour activer le capteur de vibration et rallumer l’écran.

Si l’écran OLED n’affiche rien ou affiche des informations incorrectes, suivez les étapes de dépannage ci-dessous :

1. **Vérifiez la connexion de l’écran OLED**

   Assurez-vous que le câble FPC de l’écran OLED est correctement connecté.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

2. **Vérifiez la compatibilité du système d’exploitation**

   Assurez-vous que vous utilisez un système d’exploitation compatible sur votre Raspberry Pi.

3. **Vérifiez l’adresse I2C**

   Exécutez la commande suivante pour vérifier si l’adresse I2C (0x3C) de l’OLED est détectée :

   .. code-block:: shell

      sudo i2cdetect -y 1

   Si l’adresse n’est pas détectée, activez I2C avec la commande suivante :

   .. code-block:: shell

      sudo raspi-config

4. **Redémarrez le service pironman5**

   Redémarrez le service `pironman5` pour voir si le problème est résolu :

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Vérifiez le fichier journal**

   Si le problème persiste, consultez le fichier journal pour trouver les messages d’erreur et envoyez ces informations au support client pour une analyse plus approfondie :

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log


7. Le module NVMe PIP ne fonctionne pas ?
--------------------------------------------------

1. Assurez-vous que le câble FPC reliant le module NVMe PIP au Raspberry Pi 5 est correctement connecté.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

2. Vérifiez que votre SSD est correctement fixé dans le module NVMe PIP.

3. Vérifiez l’état des voyants LED du module NVMe PIP :

   Une fois toutes les connexions vérifiées, allumez le Pironman 5 MAX et observez les deux voyants du module NVMe PIP :

   * **PWR-LED** : doit être allumée.  
   * **STA-LED** : doit clignoter pour indiquer un fonctionnement normal.

   .. image:: img/dual_nvme_pip_leds.png  

   * Si la **PWR-LED** est allumée mais que la **STA-LED** ne clignote pas, cela signifie que le SSD NVMe n’est pas reconnu par le Raspberry Pi.  
   * Si la **PWR-LED** est éteinte, reliez les broches "Force Enable" sur le module. Si la **PWR-LED** s’allume ensuite, cela peut indiquer un câble FPC desserré ou une configuration système non compatible avec NVMe.

   .. image:: img/dual_nvme_pip_j4.png  

4. Assurez-vous qu’un système d’exploitation correct est installé sur votre SSD NVMe. Voir : :ref:`install_the_os_max`.

5. Si le câblage est correct et que l’OS est installé mais que le SSD NVMe ne démarre toujours pas, essayez de démarrer à partir d’une carte Micro SD pour vérifier le bon fonctionnement des autres composants. Une fois confirmé, passez à :ref:`configure_boot_ssd_max`.

Si le problème persiste après ces étapes, veuillez envoyer un e-mail à service@sunfounder.com. Nous vous répondrons dans les plus brefs délais.


8. Les LED RVB ne fonctionnent pas ?
------------------------------------------

#. Les deux broches de l’IO-Expander situées au-dessus de J9 sont utilisées pour connecter les LED RVB au GPIO10. Assurez-vous que le cavalier est correctement placé sur ces deux broches.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vérifiez que le Raspberry Pi exécute un système d’exploitation compatible. Le Pironman 5 ne prend en charge que les versions d’OS suivantes :

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si vous avez installé un OS non compatible, suivez le guide pour installer un OS pris en charge : :ref:`install_the_os_max`.

#. Exécutez la commande ``sudo raspi-config`` pour ouvrir le menu de configuration. Accédez à **3 Interfacing Options** -> **I3 SPI** -> **YES**, puis cliquez sur **OK** et **Finish** pour activer SPI. Après l’activation, redémarrez le Pironman 5.

Si le problème persiste après ces étapes, veuillez envoyer un e-mail à service@sunfounder.com. Nous vous répondrons dans les plus brefs délais.


9. Le ventilateur CPU ne fonctionne pas ?
----------------------------------------------

Si la température du CPU n’a pas atteint le seuil défini, le ventilateur ne s’allumera pas.

**Contrôle de la vitesse du ventilateur en fonction de la température**  

Le ventilateur PWM fonctionne de manière dynamique et ajuste sa vitesse en fonction de la température du Raspberry Pi 5 :

* **Moins de 50°C** : ventilateur arrêté (0 % de vitesse)  
* **À 50°C** : vitesse faible (30 %)  
* **À 60°C** : vitesse moyenne (50 %)  
* **À 67,5°C** : vitesse élevée (70 %)  
* **À 75°C et plus** : vitesse maximale (100 %)

Pour plus de détails, voir : :ref:`fan_max`


10. Comment réactiver l’écran OLED ?
---------------------------------------------------------------------------------

Pour économiser de l’énergie et prolonger la durée de vie de l’écran, celui-ci s’éteint automatiquement après une période d’inactivité. C’est un comportement normal et cela n’affecte pas les fonctionnalités du produit.

Vous pouvez tapoter légèrement sur le boîtier pour activer le capteur de vibration et rallumer l’écran.

.. note::

   Pour configurer l’écran OLED (par exemple, marche/arrêt, durée de veille, rotation, etc.), veuillez consulter : :ref:`max_view_control_dashboard` ou :ref:`max_view_control_commands`.


11. Comment désactiver le tableau de bord Web ?  
------------------------------------------------------

Une fois l’installation du module ``pironman5`` terminée, vous pourrez accéder au :ref:`max_view_control_dashboard`.
      
Si vous n’avez pas besoin de cette fonctionnalité et que vous souhaitez réduire l’utilisation du processeur et de la mémoire, vous pouvez désactiver le tableau de bord pendant l’installation de ``pironman5`` en ajoutant l’option ``--disable-dashboard``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Si vous avez déjà installé ``pironman 5``, vous pouvez supprimer le module ``dashboard`` et ``influxdb``, puis redémarrer pironman5 pour appliquer les changements :
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5


12. Comment contrôler les composants avec la commande ``pironman5``  
----------------------------------------------------------------------

Vous pouvez consulter le tutoriel suivant pour contrôler les composants du Pironman 5 MAX à l’aide de la commande ``pironman5``.

* :ref:`max_view_control_commands`


13. Comment modifier l’ordre de démarrage du Raspberry Pi à l’aide de commandes  
---------------------------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l’ordre de démarrage en utilisant des commandes. Les instructions détaillées sont les suivantes :

* :ref:`configure_boot_ssd_max`


14. Comment modifier l’ordre de démarrage avec Raspberry Pi Imager ?  
------------------------------------------------------------------------------

En plus de modifier la variable ``BOOT_ORDER`` dans la configuration de l’EEPROM, vous pouvez également utiliser **Raspberry Pi Imager** pour changer l’ordre de démarrage de votre Raspberry Pi.

Il est recommandé d’utiliser une carte de secours pour cette étape.

* :ref:`update_bootloader_max`


15. Comment copier le système de la carte SD vers un SSD NVMe ?  
-------------------------------------------------------------------------

Si vous disposez d’un SSD NVMe mais que vous n’avez pas d’adaptateur pour le connecter à votre ordinateur, vous pouvez d’abord installer le système sur votre carte Micro SD. Une fois que le Pironman 5 MAX démarre correctement, vous pouvez copier le système de votre carte Micro SD vers votre SSD NVMe. Les instructions détaillées sont les suivantes :

* :ref:`copy_sd_to_nvme_max`


16. Comment retirer le film protecteur des plaques en acrylique  
-----------------------------------------------------------------

Deux panneaux en acrylique sont inclus dans le colis, chacun recouvert d’un film protecteur jaune ou transparent des deux côtés pour éviter les rayures. Ce film peut être un peu difficile à retirer. Utilisez un tournevis pour gratter doucement les coins, puis décollez soigneusement l’ensemble du film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center


.. _max_openssh_powershell:

17. Comment installer OpenSSH via PowerShell ?  
--------------------------------------------------

Lorsque vous utilisez ``ssh <nom_utilisateur>@<nom_hôte>.local`` (ou ``ssh <nom_utilisateur>@<adresse_IP>``) pour vous connecter à votre Raspberry Pi, mais que le message d’erreur suivant apparaît :

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Cela signifie que votre système est trop ancien et ne possède pas `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Vous devez suivre le tutoriel ci-dessous pour l’installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu’administrateur`` dans le menu qui apparaît.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l’installation, la sortie suivante s’affichera.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l’installation en utilisant la commande suivante.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Cela vous indique que ``OpenSSH.Client`` a été installé avec succès.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        Si le message ci-dessus n’apparaît pas, cela signifie que votre système Windows est encore trop ancien. Il est alors recommandé d’installer un outil SSH tiers comme |link_putty|.

#. Redémarrez maintenant PowerShell et exécutez-le à nouveau en tant qu’administrateur. À ce stade, vous pourrez vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``. Vous serez invité à entrer le mot de passe que vous avez configuré précédemment.

   .. image:: img/powershell_login.png


18. Si je configure OMV, puis-je toujours utiliser les fonctions de Pironman5 ?  
--------------------------------------------------------------------------------------------------------

Oui, OpenMediaVault est configuré sur le système Raspberry Pi. Veuillez suivre les étapes de :ref:`max_set_up_pi_os` pour continuer la configuration.



19. PI5 ne démarre pas (LED rouge) ?
-------------------------------------------

Ce problème peut être causé par une mise à jour du système, des modifications de l’ordre de démarrage ou un chargeur de démarrage corrompu. Vous pouvez essayer les étapes suivantes pour le résoudre :

#. Vérifiez la connexion de l’adaptateur USB-HDMI

   * Vérifiez soigneusement si l’adaptateur USB-HDMI est correctement connecté au PI5.  
   * Essayez de le débrancher et de le rebrancher.  
   * Reconnectez ensuite l’alimentation et vérifiez si le PI5 démarre correctement.

#. Testez le PI5 en dehors du boîtier

   * Si le fait de reconnecter l’adaptateur ne résout pas le problème :  
   * Retirez le PI5 du boîtier Pironman 5.  
   * Alimentez directement le PI5 avec l’adaptateur secteur (sans boîtier).  
   * Vérifiez s’il démarre normalement.

#. Restaurer le chargeur de démarrage

   * Si le PI5 ne démarre toujours pas, le chargeur de démarrage est peut-être corrompu. Vous pouvez suivre ce guide : :ref:`update_bootloader_max` et choisir de démarrer depuis la carte SD ou NVMe/USB.  
   * Insérez la carte SD préparée dans le PI5, allumez-le et attendez au moins 10 secondes. Une fois la restauration terminée, retirez et reformatez la carte SD.  
   * Ensuite, utilisez Raspberry Pi Imager pour flasher la dernière version de Raspberry Pi OS, insérez à nouveau la carte et essayez de démarrer.
