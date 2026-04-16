.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Adaptateur USB HDMI
==========================================

.. image:: img/hdmi_adapter.png

Cette carte adaptateur USB HDMI est spécialement conçue pour le Raspberry Pi 5. Sa fonction principale est de repositionner les connexions USB et HDMI pour les aligner avec le côté interface USB du Raspberry Pi, améliorant ainsi l'accessibilité et la gestion des câbles.

De plus, le port HDMI est converti en une interface HDMI Type A standard, offrant une compatibilité plus large.

**Alimentation supplémentaire pour NVMe**

La carte dispose d'un en-tête d'alimentation 5V spécifiquement pour l'alimentation du PIP NVMe. Couplé à un en-tête d'extension, il peut être connecté à l'interface d'alimentation supplémentaire du NVMe pour fournir une puissance supplémentaire.

**Support de batterie 1220RTC**

Un support de batterie 1220RTC est incorporé pour une installation pratique d'une batterie RTC. Il se connecte à l'interface RTC du Raspberry Pi via un câble inversé SH1.0 2P.

Le support de batterie est compatible avec les batteries CR1220 et ML1220. Si vous utilisez une batterie ML1220 (batterie au dioxyde de manganèse et lithium), la charge peut être configurée directement sur le Raspberry Pi. Notez que la CR1220 n'est pas rechargeable.

**Activation de la charge d'entretien**

.. attention::

  Si vous utilisez une batterie CR1220, n'activez pas la charge d'entretien car cela pourrait endommager irrémédiablement la batterie et risquer d'endommager la carte.

Par défaut, la fonction de charge d'entretien de la batterie est désactivée. Les fichiers ``sysfs`` indiquent la tension et les limites de charge d'entretien actuelles :

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Pour activer la charge d'entretien, ajoutez ``rtc_bbat_vchg`` dans ``/boot/firmware/config.txt`` :

  * Ouvrez le fichier ``/boot/firmware/config.txt``.

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt

  * Ajoutez ``rtc_bbat_vchg`` dans ``/boot/firmware/config.txt``.

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

Après le redémarrage, le système affichera :

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Cela confirme que la batterie est maintenant en charge d'entretien. Pour désactiver cette fonction, supprimez simplement la ligne ``dtparam`` du fichier ``config.txt``.

Interface audio
---------------------------------

Cette section couvre les fonctionnalités de sortie audio de la carte, y compris la sortie haut-parleur et la prise casque.

.. image:: img/hdmi_speaker_port.png

**Port haut-parleur**

La carte dispose d'une interface de sortie haut-parleur à deux canaux qui prend en charge deux haut-parleurs de 4Ω 3W.

**Interrupteur des haut-parleurs**

Le signal audio des haut-parleurs provient de la source HDMI0. Si HDMI0 est connecté à un écran avec haut-parleurs intégrés, les haut-parleurs du Pironman 5 Pro Max et les haut-parleurs de l'écran peuvent jouer l'audio simultanément. Le cavalier **SPEAKER** vous permet de contrôler ce comportement.

*   Connectez le cavalier aux deux broches de gauche (**ON**) pour garder les haut-parleurs **toujours activés**.
*   Connectez le cavalier aux deux broches de droite (**AUTO**) pour que les haut-parleurs soient **automatiquement désactivés** lorsqu'un casque est branché ou lorsque HDMI0 est connecté.

Par conséquent, si vous souhaitez utiliser les haut-parleurs intégrés alors qu'un écran HDMI est connecté, vous pouvez soit :

*   Connecter l'écran au port **HDMI1** à la place.
*   Régler le cavalier **SPEAKER** sur la position **ON**.

**Prise audio 3,5 mm**

La prise casque partage la même source audio que les haut-parleurs mais transporte un signal **non amplifié**. Elle utilise une prise commutée qui **désactive automatiquement l'amplificateur des haut-parleurs** lorsqu'un casque est branché, empêchant ainsi les deux de jouer du son simultanément.

La prise est un connecteur TRRS à 4 broches mais ne prend en charge que la **sortie audio stéréo standard** :

*   **Pointe (T)** : Canal gauche
*   **Anneau 1 (R1)** : Canal droit
*   **Anneau 2 (R2)** : Masse
*   **Manchon (S)** : Masse

Cette configuration maintient la compatibilité avec la plupart des standards de casques à 4 broches courants.