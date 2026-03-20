.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

NextCloudPi einrichten
=======================================

NextCloud ist eine Open-Source-Lösung für private Cloud-Speicher, ähnlich wie Google Drive oder Dropbox. Es kann verwendet werden, um Dateien zu speichern, Dokumente zu teilen, Fotos zu synchronisieren und Kalender sowie Kontakte zu verwalten.
Im Gegensatz zu öffentlichen Cloud-Diensten gibt NextCloud den Benutzern die vollständige Kontrolle über ihre Daten, was es ideal für Einzelpersonen und kleine Teams macht, die Wert auf Privatsphäre und Datensicherheit legen.

Die Pironman5-Serie, angetrieben von einem Raspberry Pi, bietet geringen Stromverbrauch, kompakte Größe und zuverlässige Leistung, was sie zu einer ausgezeichneten Wahl für einen privaten Heim-Cloud-Server macht. In Kombination mit NextCloud kann es als kostengünstiges NAS-System dienen.


**Vorbereitung**

* MicroSD-Karte (16GB+, Klasse 10 empfohlen)
* Offizielles Raspberry Pi System Raspberry Pi OS (oder Raspberry Pi OS Lite)
* Stabile Netzwerkverbindung (kabelgebundenes Ethernet empfohlen)
* Externe Festplatte oder USB-Stick (für erweiterten Speicher)


**Portainer installieren**

Öffnen Sie das Terminal und geben Sie die folgenden Befehle ein:

1. Docker installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainer installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash



3. Starten Sie Ihren Raspberry Pi neu. (Führen Sie dann die folgenden Schritte **SOFORT** aus.)



4. Nachdem Ihr Raspberry Pi hochgefahren ist, öffnen Sie einen Webbrowser und besuchen Sie Ihre Portainer-Adresse: ``https://<Ihre-RPi-IP-Adresse>:9443``.

5. Standardmäßig sehen Sie eine Warnung, dass die Website ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer bekannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Webbrowser zeigen eine Warnung über solche Zertifikate an. In diesem Fall können Sie die Warnung getrost ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png


#. Bei der ersten Anmeldung müssen Sie ein Admin-Passwort festlegen.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Nach der Registrierung des Admin-Kontos gelangen Sie in die Portainer-Oberfläche. Klicken Sie in der linken Navigationsleiste auf **Setting -> General**, suchen Sie **App Templates** und geben Sie die folgende URL in das Feld ein: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Klicken Sie auf **Save Application Settings**. Die Einrichtung dauert etwa 10 Sekunden.


**NextCloud installieren**


1. Klicken Sie in der linken Navigationsleiste auf **Home -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Gehen Sie zu **Templates -> Application**. Geben Sie in der Suchleiste oben rechts *nextcloud* ein und klicken Sie darauf.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Klicken Sie auf **Deploy the stack** und warten Sie, bis die Bereitstellung abgeschlossen ist. Dies dauert in der Regel etwa zwei Minuten.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Nach Abschluss ist NextCloud installiert.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png


**NextCloud verwenden**

1. Öffnen Sie Ihren Browser und besuchen Sie Ihre NextCloud-Adresse: ``https://<Ihre-RPi-IP-Adresse>:32768``.

.. note::

   Auch hier sehen Sie eine Warnung, dass die Website ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer bekannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Webbrowser zeigen eine Warnung über solche Zertifikate an.
   In diesem Fall können Sie die Warnung getrost ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png

2. Bei der ersten Anmeldung müssen Sie ein Admin-Passwort festlegen.

   .. image:: img/home_server_app/nc_admin_install.png

3. Nach der Registrierung können Sie NextCloud verwenden.

   .. image:: img/home_server_app/nc_dashboard.png