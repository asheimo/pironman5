.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Home Assistant einrichten
======================================

Home Assistant ist eine Hausautomationsplattform, die auf einem zentralen Hub (Raspberry Pi, PC usw.) läuft. Sie kann verwendet werden, um alle Arten von Geräten zu steuern und zu überwachen, von Lampen und Thermostaten bis hin zu Überwachungskameras und intelligenten Haushaltsgeräten.

**Vorbereitung**

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

* Einen Raspberry Pi, der Home Assistant ausführen kann.
* Eine stabile Internetverbindung.
* Ein Konto bei Home Assistant Cloud (optional, aber für den Fernzugriff empfohlen).

**Installation**

Öffnen Sie das Terminal und geben Sie die folgenden Befehle ein:

1. Docker installieren

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash


2. Home Assistant installieren

.. code-block:: bash

   sudo docker pull homeassistant/home-assistant


**Home Assistant Container ausführen**

Hier verwenden wir Docker Compose, um Home Assistant auszuführen. Sie können sich Docker Compose als ein "Automatisierungsskript" vorstellen. Es schreibt alle Konfigurationen (wie Image-Name, Ports, Volume-Mounts, Umgebungsvariablen usw.) in eine ``docker-compose.yml``-Datei. Danach erstellt und startet Docker mit einem einfachen Befehl ``docker compose up -d`` automatisch alle konfigurierten Container gemäß diesem "Skript".


1.  **In das Projektverzeichnis wechseln**: Gehen Sie in diesen Ordner.

   .. code-block:: bash

      cd ~/homeassistant


2.  **Die Konfigurationsdatei erstellen**: Erstellen Sie im Verzeichnis ``~/homeassistant`` eine Datei namens ``docker-compose.yml`` und kopieren Sie die obige Konfiguration hinein.

   .. code-block:: bash

      sudo nano docker-compose.yml


3. Fügen Sie den folgenden Inhalt in die Datei ``docker-compose.yml`` ein:

   .. note:: Bitte ersetzen Sie ``- TZ=Asia/Shanghai`` durch Ihre Zeitzone.

   .. code-block:: bash

      version: '3'
      services:
      homeassistant:
         image: ghcr.io/home-assistant/raspberrypi5-64-homeassistant:stable
         container_name: homeassistant
         restart: unless-stopped
         privileged: true
         network_mode: host
         environment:
            - TZ=Europe/Berlin
         volumes:
            - ./config:/config

4. ``Strg+X`` zum Beenden des Editors, und dann drücken Sie ``Y``, um die Änderungen zu speichern.

5.  **Home Assistant starten**: Führen Sie im Verzeichnis ``~/homeassistant`` den folgenden Befehl aus. Docker Compose wird automatisch das Image pullen und den Container starten.

   .. code-block:: bash

      sudo docker compose up -d

   * ``up``: Dienste erstellen und starten.
   * ``-d``: Im Hintergrund ausführen (getrennter Modus).


6.  **Den Ausführungsstatus überprüfen**:

    .. code-block:: bash

      docker compose ps

   Sie sollten den Status von ``homeassistant`` als ``Up`` sehen.

7.  **Die Protokolle anzeigen** (falls es Startprobleme gibt):

   .. code-block:: bash

      docker compose logs -f

8. Für weitere Befehle überprüfen Sie:

   .. code-block:: bash

      docker compose --help

**Einrichtung**

Jetzt können Sie den Browser Ihres Computers öffnen und eingeben: ``http://<Ihre Raspberry Pi Adresse>:8123``, um auf Home Assistant zuzugreifen.

.. image:: img/home_assistant/ha_welcome.png


Wählen Sie **CREATE MY SMART HOME** und erstellen Sie dann Ihr Konto.

.. image:: img/home_assistant/ha_onboarding.png

Folgen Sie den Eingabeaufforderungen, um Ihren Standort und andere Konfigurationen auszuwählen. Nach Abschluss gelangen Sie in das Home Assistant-Dashboard.

.. image:: img/home_assistant/ha_overview.png