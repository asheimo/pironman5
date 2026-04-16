
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




Module Caméra Panoramique et d'Inclinaison
===========================================

.. image:: img/pan_tilt.jpg
    :width: 600
    :align: center

.. note::

    La série Pironman 5 n'inclut pas de module caméra.
    Vous devez en préparer un vous-même ou l'acheter sur notre site officiel :

    * `Kit AI Funsion Lab <https://www.sunfounder.com/products/sunfounder-ai-fusion-lab-kit>`_

Dans cette section, vous apprendrez comment configurer et contrôler un module caméra panoramique et d'inclinaison en utilisant deux servomoteurs SG90 connectés directement aux broches GPIO. À la fin de cette section, vous aurez un module entièrement installé et fonctionnel prêt pour vos projets.

Connexion matérielle
-------------------------------------------

Avant de commencer, assurez-vous que votre Raspberry Pi est éteint.

**Schéma de connexion :**

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Périphérique
     - Broche GPIO
     - Broche physique
   * - Servo Pan (Orange)
     - GPIO17
     - Broche 11
   * - Servo Tilt (Orange)
     - GPIO18
     - Broche 12
   * - VCC (Rouge)
     - 5V
     - Broche 2 ou 4
   * - GND (Marron)
     - GND
     - Broche 6, 9, 14, 20, 25, 30, 34, 39
   * - Module Caméra
     - Interface CSI
     - Connectez-vous au port caméra

.. attention::

    Bien que les servomoteurs SG90 puissent être alimentés directement par la broche 5V du Raspberry Pi pendant les tests, une utilisation prolongée ou le mouvement simultané des deux servomoteurs peut provoquer des chutes de tension et une instabilité du système. Pour les projets à long terme, envisagez d'utiliser une alimentation externe 5V (assurez une masse commune avec le Raspberry Pi).

**Connexion étape par étape :**

1. **Connectez les servomoteurs** :

   - Connectez le fil orange de signal du servo Pan à GPIO17 (broche physique 11)
   - Connectez le fil orange de signal du servo Tilt à GPIO18 (broche physique 12)
   - Connectez les fils rouges VCC des deux servomoteurs à une broche 5V (broche physique 2 ou 4)
   - Connectez les fils marrons GND des deux servomoteurs à n'importe quelle broche GND (par exemple, broche physique 6)

2. **Connectez la caméra** :

   - Soulevez doucement la pince en plastique sur le connecteur caméra CSI
   - Insérez le câble nappe de la caméra avec les contacts métalliques orientés vers l'opposé du port Ethernet
   - Appuyez sur la pince en plastique pour sécuriser le câble

Tester le servomoteur
-------------------------------------------

Avant d'exécuter l'exemple complet de Pan-Tilt, testons chaque servomoteur individuellement pour nous assurer qu'ils fonctionnent correctement.

**1. Activer GPIO et I2C (si nécessaire) :**

.. code-block:: bash

    sudo raspi-config
    # Naviguez vers : Interface Options -> I2C -> Enable
    # Redémarrez après l'activation

**2. Script simple de test du servomoteur :**

Créez un fichier de test ``servo_test.py`` :

.. code-block:: python

    #!/usr/bin/env python3
    # servo_test.py - Test simple de servomoteur

    from gpiozero import Servo
    import time

    # Test du servo Pan sur GPIO17
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    print("Test du servo Pan (GPIO17)...")
    print("Déplacement vers la position 0°...")
    pan.value = -1  # 0°
    time.sleep(2)

    print("Déplacement vers la position 90°...")
    pan.value = 0   # 90°
    time.sleep(2)

    print("Déplacement vers la position 180°...")
    pan.value = 1   # 180°
    time.sleep(2)

    pan.close()
    print("Test du servo Pan terminé")

**3. Exécutez le test :**

.. code-block:: bash

    python3 servo_test.py

Si le servomoteur se déplace correctement à travers toutes les positions, répétez le test pour le servo Tilt en changeant le numéro de broche pour 18.

Tester la caméra
-------------------------------------------

**1. Activez l'interface caméra :**

.. code-block:: bash

    sudo raspi-config
    # Naviguez vers : Interface Options -> Camera -> Enable
    # Ou pour les systèmes plus récents : Interface Options -> Legacy Camera -> Enable
    sudo reboot

**2. Testez la capture de la caméra :**

Pour Raspberry Pi OS Bullseye et plus récent (utilisant libcamera) :

.. code-block:: bash

    # Prendre une photo de test
    libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480

    # Aperçu du flux caméra
    libcamera-hello -t 0

Pour les systèmes plus anciens (utilisant raspistill) :

.. code-block:: bash

    # Prendre une photo de test
    raspistill -o test.jpg -t 2000 -w 640 -h 480

    # Aperçu du flux vidéo
    raspivid -t 0

**3. Vérifiez la photo :**

.. code-block:: bash

    ls -l test.jpg
    # Ouvrir l'image (si vous avez une interface graphique)
    xdg-open test.jpg

Exemple de Pan-Tilt
-------------------------------------------

Maintenant, combinons le contrôle des servomoteurs et la fonctionnalité de la caméra dans un programme complet de contrôle Pan-Tilt. Cet exemple vous permet de contrôler la direction de la caméra à l'aide des touches WSAD et de prendre des photos avec la touche T.

**1. Créez le script de contrôle Pan-Tilt :**

.. code-block:: bash

    nano ptz_wsad_simple.py

Copiez le code suivant :

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # ptz_wsad_simple.py - Contrôle PTZ avec touches WSAD, version ultra simple

    from gpiozero import Servo
    import os
    from datetime import datetime

    # Initialiser les servomoteurs
    # Paramètres SG90 : largeur d'impulsion min 0,5ms (0°), largeur d'impulsion max 2,5ms (180°)
    pan = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
    tilt = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    # Position initiale (centre)
    pan.value = 0
    tilt.value = 0

    print("\n=== Contrôle PTZ SG90 ===")
    print("W : Haut")
    print("S : Bas")
    print("A : Gauche")
    print("D : Droite")
    print("T : Prendre une photo")
    print("C : Centrer")
    print("Q : Quitter")
    print("-" * 30)

    def take_photo():
        """Fonction pour prendre une photo"""
        # Créer le répertoire de photos s'il n'existe pas
        photo_dir = "/home/pi/Pictures/ptz"
        os.makedirs(photo_dir, exist_ok=True)

        # Générer un nom de fichier avec horodatage
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{photo_dir}/ptz_{timestamp}.jpg"

        # Prendre une photo avec libcamera (pour Raspberry Pi Bullseye et supérieur)
        # Alternative pour les systèmes plus anciens : utiliser raspistill
        os.system(f"libcamera-jpeg -o {filename} -t 1 --width 640 --height 480")

        # Commande alternative pour les systèmes plus anciens :
        # os.system(f"raspistill -o {filename} -t 1 -w 640 -h 480")

        print(f"Photo enregistrée : {filename}")

    try:
        while True:
            # Obtenir l'entrée utilisateur
            cmd = input("Entrez la commande : ").lower().strip()

            if cmd == 'w':
                # Monter (augmenter l'angle d'inclinaison)
                tilt.value = min(1.0, tilt.value + 0.2)
                print(f"↑ Haut ({tilt.value:.1f})")

            elif cmd == 's':
                # Descendre (diminuer l'angle d'inclinaison)
                tilt.value = max(-1.0, tilt.value - 0.2)
                print(f"↓ Bas ({tilt.value:.1f})")

            elif cmd == 'a':
                # Aller à gauche (diminuer l'angle panoramique)
                pan.value = max(-1.0, pan.value - 0.2)
                print(f"← Gauche ({pan.value:.1f})")

            elif cmd == 'd':
                # Aller à droite (augmenter l'angle panoramique)
                pan.value = min(1.0, pan.value + 0.2)
                print(f"→ Droite ({pan.value:.1f})")

            elif cmd == 't':
                # Prendre une photo
                take_photo()

            elif cmd == 'c':
                # Centrer le PTZ
                pan.value = 0
                tilt.value = 0
                print("PTZ centré")

            elif cmd == 'q':
                # Quitter le programme
                print("Fermeture du programme")
                break

            else:
                print("Commande invalide, veuillez utiliser W/S/A/D/T/C/Q")

    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur")

    finally:
        # Nettoyer les ressources GPIO
        pan.close()
        tilt.close()
        print("GPIO nettoyé")

**2. Rendez le script exécutable :**

.. code-block:: bash

    chmod +x ptz_wsad_simple.py

**3. Exécutez le contrôleur Pan-Tilt :**

.. code-block:: bash

    python3 ptz_wsad_simple.py

**4. Contrôlez la caméra :**

- Appuyez sur **W/S** pour incliner haut/bas
- Appuyez sur **A/D** pour panoramique gauche/droite
- Appuyez sur **T** pour prendre une photo (enregistrée dans `/home/pi/Pictures/ptz/`)
- Appuyez sur **C** pour centrer la caméra
- Appuyez sur **Q** pour quitter

**Capture de la caméra :**

Le script utilise ``libcamera-jpeg`` (pour les versions plus récentes de Raspberry Pi OS) pour capturer des photos. Les photos sont automatiquement enregistrées avec des horodatages pour éviter les écrasements.
