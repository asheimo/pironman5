
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuration de l'écran
===================================================================

Ce chapitre vous guide à travers la configuration des paramètres d'affichage pour le Pironman 5 Pro MAX, y compris l'activation de la mise en veille de l'écran pour économiser l'énergie et la configuration du retournement de l'écran pour s'adapter à des orientations d'installation spéciales.

-------------------------------------------------------------------

**Configuration de la mise en veille de l'écran**


Pour économiser de l'énergie lorsque vous n'utilisez pas activement le Pironman 5 Pro MAX, vous pouvez activer la fonction de mise en veille automatique de l'écran. Lorsque l'appareil est inactif pendant une période définie, l'écran principal s'éteindra automatiquement, passant dans un état de faible consommation.

Suivez ces étapes pour le configurer :

1. Cliquez sur **Menu -> Préférences** dans le coin inférieur gauche de l'écran, puis trouvez et ouvrez le **Centre de contrôle**.

   .. image:: img/sleep_screen1.png

2. Dans l'interface du Centre de contrôle, cliquez pour accéder aux paramètres **Affichage**.

3. Localisez l'option **Mise en veille de l'écran** et activez-la.

   .. image:: img/sleep_screen2.png

----------------------------------------------------------------------

**Retourner le Pironman 5 Pro MAX**

Le Pironman 5 Pro MAX peut être retourné pour une utilisation. Dans cette configuration, l'écran tactile sera positionné sur le dessus et les ports GPIO en bas, offrant une plus grande flexibilité pour divers projets. Cette configuration est idéale pour des applications telles qu'une visualisation plus pratique de l'écran ou un accès plus facile aux broches GPIO lors de la connexion de capteurs.

Lorsque vous retournez l'appareil, les deux écrans nécessitent des réglages séparés :

   * Écran tactile principal – Nécessite des paramètres de rotation au niveau du système d'exploitation
   * Écran de statut OLED – Nécessite une configuration en ligne de commande

Pour retourner le Pironman 5 Pro MAX, suivez ces étapes :

1. Préparation physique

   Retirez la caméra du Pironman 5 Pro MAX, retournez l'ensemble de l'unité, et réinstallez la caméra. L'installation doit être symétrique par rapport à son orientation d'origine.

   .. image:: img/inverted_screen0.png

2. Configuration de l'orientation de l'écran tactile

   Allumez l'appareil. Sur l'écran tactile, effectuez un appui long sur le bureau pour faire apparaître le menu et sélectionnez **Préférences du bureau**.

   .. image:: img/inverted_screen1.png

   Faites défiler vers le bas pour trouver l'option **Écrans**, puis effectuez un appui long sur l'indicateur d'écran dans l'affichage. Sélectionnez **Orientation → Inversée**.

   .. image:: img/inverted_screen2.png

   Appliquez, la fenêtre de mise à jour affichera l'écran, vous devez cliquer sur OK pour confirmer.

   .. image:: img/inverted_screen3.png

3. Configuration de l'écran OLED

   Dans le terminal, exécutez la commande suivante pour faire pivoter l'OLED de 180 degrés :

   .. code-block:: bash

      sudo pironman5 -or 180

----------------------------------------------------

**Remarque**

- Après le retournement, assurez-vous que l'unité est placée sur une surface stable pour éviter qu'elle ne bascule.
- Si vous rencontrez un décalage des entrées tactiles, recalibrez l'écran tactile via les paramètres système.
- Pour des réglages d'affichage avancés, consultez la section :ref:`promax_view_control_commands` pour les commandes supplémentaires relatives à l'OLED et à la rotation de l'écran.
