.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Plex einrichten
=======================================

Plex ist eine leistungsstarke Media-Server-Plattform, mit der Sie Ihre Filme, Fernsehsendungen, Musik und Fotos organisieren, streamen und auf mehreren Geräten darauf zugreifen können. Durch die Einrichtung von Plex auf der Pironman5-Serie, die von einem Raspberry Pi angetrieben wird, können Sie ein erschwingliches und energieeffizientes Heim-Medienzentrum schaffen, das rund um die Uhr läuft. Die kompakte Größe, der geringe Stromverbrauch und die Flexibilität des Raspberry Pi machen ihn zu einer ausgezeichneten Wahl für das Hosten von Plex und verwandeln Ihren Pi in einen persönlichen Unterhaltungs-Hub, auf den Sie von Ihrem Heimnetzwerk oder sogar aus der Ferne zugreifen können.


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



4. Nachdem Ihr Raspberry Pi hochgefahren ist, öffnen Sie einen Webbrowser und besuchen Sie Ihre Portainer-Adresse: ``http://<Ihre-RPi-IP-Adresse>:9443`` .



5. Standardmäßig sehen Sie möglicherweise eine Warnung, dass die Website ein selbstsigniertes SSL/TLS-Zertifikat verwendet, das nicht von einer bekannten Zertifizierungsstelle (CA) ausgestellt wurde. Die meisten Webbrowser zeigen eine solche Warnung an. In diesem Fall können Sie sie getrost ignorieren, das Risiko akzeptieren und fortfahren.

   .. image:: img/home_server_app/private_save.png


#. Bei Ihrer ersten Anmeldung werden Sie aufgefordert, ein Administrator-Passwort festzulegen.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Nach der Erstellung des Admin-Kontos gelangen Sie in die Portainer-Oberfläche. Gehen Sie in der linken Navigationsleiste zu **Setting -> General**, suchen Sie **App Templates** und geben Sie die folgende URL in das Feld ein: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Klicken Sie auf **Save Application Settings**. Die Einrichtung dauert etwa 10 Sekunden.


**Plex installieren**


1. Klicken Sie in der linken Navigationsleiste auf **Home -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Gehen Sie zu **Templates -> Application**. Geben Sie in der Suchleiste oben rechts *plex* ein und klicken Sie darauf.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png


#. Setzen Sie den Netzwerkmodus auf **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. Erweitern Sie **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. Konfigurieren Sie im Abschnitt **volume mapping** die Speicherpfade für Ihre Mediendateien und gewähren Sie Plex Lese-/Schreibberechtigungen. Die Standardpfade sind ``/portainer/TV`` und ``/portainer/Movies``, beide mit aktiviertem Lese-/Schreibzugriff.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. Klicken Sie auf **Deploy** und warten Sie, bis die Installation von Plex abgeschlossen ist.


**Plex-Server konfigurieren**

1. Öffnen Sie Ihren Browser und geben Sie ein: ``http://<Ihre_IP>:32400/web`` . Sie sollten nun die Plex-Oberfläche sehen.

   .. image:: img/home_server_app/plex_visit.png

2. Überspringen Sie das Angebot für ein Premium-Abonnement.

3. Als nächstes sehen Sie den Bildschirm **Server Setup**. Sie können *Allow me to access my media outside my home* aktivieren. Für den Moment wird empfohlen, dies nicht zu aktivieren und es später bei Bedarf zu konfigurieren.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Sie werden dann aufgefordert, Ihre Medien zu organisieren. Sie können *Skip* wählen und später über die Einstellungen Medien hinzufügen. Es wird jedoch empfohlen, direkt die Speicherpfade hinzuzufügen, die Sie im Volume-Mapping von Portainer konfiguriert haben, damit Plex Ihre Medien automatisch scannen und importieren kann.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Wählen Sie den Typ Ihrer Medienbibliothek aus, geben Sie Ihrer Bibliothek einen Namen und wählen Sie die Sprache.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Fügen Sie Ordner hinzu. Suchen Sie die zuvor festgelegten Medienspeicherpfade und klicken Sie auf **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Klicken Sie auf **Finish**. Ihr Raspberry Pi Plex-Server ist nun vollständig konfiguriert.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Sie sollten nun Ihre Mediendateien auf der Startseite des Plex-Servers angezeigt sehen.

   .. image:: img/home_server_app/plex_index.png