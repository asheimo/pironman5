.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Dual NVMe PIP
=====================

Le **Dual NVMe PIP** (PCIe Peripheral Board), tel que défini par la Raspberry Pi Foundation, est un adaptateur PCIe conçu spécifiquement pour les disques SSD NVMe.

L'interface PCIe du Raspberry Pi 5 offre nativement une seule voie **Gen2 x1** (500 Mo/s). En intégrant la puce commutateur PCIe **ASM1182e**, le Dual NVMe PIP étend cela en **deux voies Gen2 x1 indépendantes**, vous permettant de connecter :

* **Deux SSD NVMe M.2**, ou
* **Un SSD NVMe M.2 + un accélérateur AI Hailo-8/8L M.2**

**Remarques importantes** :

* Gen3 n'est pas supporté
* Supporte les tailles de SSD NVMe : **2230**, **2242**, **2260**, **2280** (tous dans les fentes M.2 M-key)

.. image:: img/nvme_pip.png

* La carte se connecte via un câble FFC (Flexible Flat Cable) inversé 16P 0,5 mm ou un câble FPC (Flexible Printed Circuit) à impédance adaptée personnalisé.
* **STA** : Un indicateur LED d'état.
* **PWR** : Un indicateur LED d'alimentation.
* L'alimentation 3,3V intégrée peut supporter jusqu'à 3A de sortie. Cependant, comme l'interface PCIe du Raspberry Pi est limitée à fournir une sortie 5V/1A (équivalente à 5W), une alimentation supplémentaire pour une utilisation 3,3V/3A peut être fournie via le connecteur J3 à partir d'une source 5V.
* **FORCE ENABLE** : L'alimentation intégrée est activée par le signal de commutation de l'interface PCIe. Après la mise sous tension du Raspberry Pi, il envoie un signal pour activer l'alimentation 3,3V. Si certains systèmes ne supportent pas le signal de commutation ou pour d'autres raisons, vous pouvez court-circuiter J4 FORCE ENABLE en soudant un fil entre les deux plots flottants pour forcer l'alimentation 3,3V intégrée à alimenter le NVMe.

À propos du modèle
---------------------------

Les SSD M.2, connus pour leur taille compacte, existent en différents types principalement différenciés par leur encoche (conception d'encoche sur le connecteur) et l'interface qu'ils utilisent. Voici les principaux types :

* **SSD M.2 SATA** : Ceux-ci utilisent l'interface SATA, similaire aux SSD SATA 2,5 pouces mais dans le facteur de forme M.2 plus petit. Ils sont limités par les vitesses maximales SATA III d'environ 600 Mo/s. Ces SSD sont compatibles avec les fentes M.2 à encoches B et M.
* **SSD M.2 NVMe** : Ces SSD utilisent le protocole NVMe sur les voies PCIe et sont nettement plus rapides que les SSD M.2 SATA. Ils conviennent aux applications nécessitant des vitesses de lecture/écriture élevées comme les jeux, le montage vidéo et les tâches intensives en données. Ces SSD nécessitent généralement des fentes à encoche M. Ces disques utilisent l'interface PCIe (Peripheral Component Interconnect Express), avec différentes versions comme 3.0, 4.0 et 5.0. Chaque nouvelle version de PCIe double effectivement la vitesse de transfert de données de son prédécesseur. Cependant, le Raspberry Pi 5 utilise une interface PCIe 3.0, capable de fournir des vitesses de transfert allant jusqu'à 3500 Mo/s.

Les SSD M.2 existent en trois types d'encoches : B key, M key et B+M key. Cependant, plus tard, la B+M key a été introduite, combinant les fonctionnalités de la B key et de la M key. En conséquence, elle a remplacé la B key autonome. Veuillez vous référer à l'image ci-dessous.

.. image:: img/ssd_key.png

En général, les SSD M.2 SATA sont B+M-key (peuvent s'adapter dans les fentes pour modules B-key et M-key), tandis que les SSD M.2 NVMe pour voie PCIe 3.0 x4 sont M-key.

.. image:: img/ssd_model2.png

À propos de la longueur
-----------------------

Les modules M.2 existent en différentes tailles et peuvent également être utilisés pour le Wi-Fi, WWAN, Bluetooth, GPS et NFC.

Le Pironman 5 MAX supporte quatre tailles de SSD NVMe M.2 (PCIe Gen 2.0) basées sur leurs noms : 2230, 2242, 2260 et 2280. Le « 22 » est la largeur en millimètres (mm), et les deux chiffres suivants sont la longueur. Plus le disque est long, plus il peut monter de puces mémoire NAND ; donc, plus la capacité est grande.

.. image:: img/m2_ssd_size.png
  :width: 600

Alimentation
-----------------------

L'alimentation double 3,3V intégrée supporte un courant de sortie maximum de 3A (10W). Les deux rails d'alimentation fonctionnent indépendamment sans interférence.

**FORCE ENABLE**
L'alimentation intégrée est activée par le signal de commutation de l'interface PCIe. Après le démarrage du Raspberry Pi, le signal active l'alimentation 3,3V. Si le système ne supporte pas le signal de commutation ou pour d'autres raisons, court-circuitez le cavalier J4 FORCE EN pour forcer l'alimentation 3,3V intégrée pour le NVMe.

**LED**
Chaque interface a des indicateurs d'état d'alimentation (PWR) et des indicateurs d'état (STA) indépendants.

Convertisseur d'interrupteur d'alimentation
-----------------------------------------------

**Ajout du bouton d'alimentation**

* Le Raspberry Pi 5 dispose d'un cavalier **J2**, situé entre le connecteur de la batterie RTC et le bord de la carte. Cette extension permet d'ajouter un bouton d'alimentation personnalisé au Raspberry Pi 5 en connectant un interrupteur momentané normalement ouvert (NO) à travers les deux plots. L'actionnement bref de cet interrupteur imite la fonctionnalité du bouton d'alimentation intégré.

   .. image:: img/pi5_j2.jpg

* Sur le Pironman 5, il y a un **convertisseur d'interrupteur d'alimentation** qui étend le cavalier **J2** à un bouton d'alimentation externe en utilisant deux broches Pogo.

   .. image:: img/psc.png

* Maintenant, le Raspberry Pi 5 peut être allumé et éteint à l'aide du bouton d'alimentation.

**Cycle d'alimentation**

Lors de la première mise sous tension de votre Raspberry Pi 5, il s'allumera automatiquement et démarrera dans le système d'exploitation sans avoir besoin d'appuyer sur le bouton.

Si vous utilisez le bureau Raspberry Pi, une brève pression sur le bouton d'alimentation initie un processus d'arrêt propre. Un menu apparaîtra, offrant des options pour éteindre, redémarrer ou se déconnecter. La sélection d'une option ou une nouvelle pression sur le bouton d'alimentation lancera un arrêt propre.

.. image:: img/button_shutdown.png

**Arrêt**

    * Si vous exécutez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d'alimentation pour éteindre.
    * Si vous exécutez le système **Raspberry Pi OS Lite** sans bureau, appuyez une seule fois sur le bouton d'alimentation pour initier un arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d'alimentation enfoncé.

**Mise sous tension**

    * Si la carte Raspberry Pi est éteinte, mais toujours alimentée, une seule pression permet de l'allumer à partir de l'état éteint.

.. note::

    Si vous exécutez un système qui ne prend pas en charge un bouton d'arrêt, vous pouvez le maintenir enfoncé pendant 5 secondes pour forcer un arrêt brutal, et une seule pression pour l'allumer à partir de l'état éteint.