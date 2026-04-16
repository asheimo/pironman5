
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_batocera:

Configuration sur Batocera.linux
=========================================================

Si vous avez installé le système d'exploitation Batocera.linux, vous pouvez vous connecter à distance à ce système via SSH, puis suivre les étapes ci-dessous pour terminer la configuration.

#. Une fois le système démarré, utilisez ssh pour vous connecter à distance au Pironman5. Pour Windows, vous pouvez ouvrir **Powershell**, et pour Mac OS X et Linux, vous pouvez ouvrir directement **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%

#. Le nom d'hôte par défaut du système batocera est ``batocera``, avec le nom d'utilisateur par défaut ``root`` et le mot de passe ``linux``. Par conséquent, vous pouvez vous connecter en tapant ``ssh root@batocera.local`` et en entrant le mot de passe ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Exécutez la commande : ``/etc/init.d/S92switch setup`` pour accéder à la page des paramètres du menu.

   .. image:: img/batocera_configure.png
      :width: 90%

#. Utilisez la touche flèche vers le bas pour naviguer jusqu'à la fin, sélectionnez et activez les services **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Après avoir activé le service pironman5, sélectionnez **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Exécutez la commande ``reboot`` pour redémarrer le Pironman5.

   .. code-block:: shell

      reboot

#. Au redémarrage, le ``pironman5.service`` démarrera automatiquement. Voici les principales configurations du Pironman 5 Pro MAX :

   * L'écran OLED affiche le CPU, la RAM, l'utilisation du disque, la température du CPU et l'adresse IP du Raspberry Pi.
   * Quatre LEDs RGB WS2812 s'allumeront en bleu avec un mode de respiration.

Maintenant, vous pouvez connecter le Pironman 5 Pro MAX à un écran, des manettes de jeu, un casque, etc., pour vous immerger dans votre monde de jeu.

.. note::

   À ce stade, vous avez configuré avec succès le Pironman 5 Pro MAX, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_promax`.
