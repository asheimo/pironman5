.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_omv_5_promax:


OpenMediaVault einrichten
=====================================

.. warning::

   OpenMediaVault **unterstützt keine** Installation auf dem Raspberry Pi OS Desktop.

   ⚠️ **Es werden nur Raspberry Pi OS Lite Versionen 11 (Bullseye) und 12 (Bookworm) unterstützt.**

   Bitte stellen Sie sicher, dass Sie das korrekte Betriebssystem installiert und das Netzwerk konfiguriert haben.
   Die Vorgehensweise hier entspricht der unter :ref:`install_os_sd_rpi_promax`, aber wählen Sie bei der Image-Auswahl Raspberry Pi OS Lite aus Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (abgekürzt OMV) ist ein Open-Source-Betriebssystem für Netzwerkspeicher (NAS) basierend auf Debian Linux, das für Heimanwender und kleine Büroumgebungen entwickelt wurde. Es zielt darauf ab, die Speicherverwaltung zu vereinfachen und umfangreiche Netzwerkdienste bereitzustellen.

Bitte folgen Sie diesen Schritten, um OpenMediaVault auf Ihrem Raspberry Pi zu installieren:

1. Stellen Sie eine SSH-Verbindung zu Ihrem Raspberry Pi her
-------------------------------------------------------------------

   Geben Sie den folgenden Befehl im Terminal ein:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Wenn Sie Windows verwenden, nutzen Sie PuTTY oder einen anderen SSH-Client, um eine Verbindung zu Ihrem Raspberry Pi herzustellen.

2. OpenMediaVault installieren
----------------------------------------------------------------

   Geben Sie den folgenden Befehl im Terminal ein:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install
      chmod +x install
      sudo ./install -n

   Dies lädt das Installationsskript für OpenMediaVault herunter und führt es aus. Starten Sie Ihren Raspberry Pi nach der Installation nicht neu.

3. Auf OpenMediaVault zugreifen
---------------------------------------------------

   Geben Sie die folgende URL in Ihren Browser ein, um auf OpenMediaVault zuzugreifen:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Wenn Sie nicht über die obige URL zugreifen können, versuchen Sie es stattdessen mit der IP-Adresse, z.B. http://192.168.1.100.

   Sie sehen eine Anmeldeseite. Melden Sie sich mit dem Standard-Benutzernamen und -Passwort an. Der Standard-Benutzername ist ``admin``, und das Passwort ist ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Nach der Anmeldung sehen Sie die Hauptoberfläche von OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Sie haben OpenMediaVault nun erfolgreich installiert und darauf zugegriffen. Sie können nun mit der Konfiguration und Verwaltung Ihres Speichers beginnen.


4. RAID einrichten (Optional)
---------------------------------------

   NVMe-RAID ist eine Speicherlösung, die mehrere NVMe-Solid-State-Laufwerke (SSDs) mittels RAID-Technologie kombiniert, um die hohe Geschwindigkeit des NVMe-Protokolls und die Redundanz-/Leistungssteigerungsfunktionen von RAID zu maximieren. Übliche Modi sind RAID 0, 1, 5, 10 usw. Für zwei NVMe-SSDs sind RAID 0 und RAID 1 die am häufigsten verwendeten Modi.

   * RAID 0 ist eine Striping-Technologie, die Daten in mehrere Streifen aufteilt und diese Streifen auf mehrere Festplatten verteilt, um so höhere Lese-/Schreibgeschwindigkeiten zu erreichen. RAID 0 bietet keine Redundanz. Fällt eine der Festplatten aus, gehen alle Daten verloren.

   * RAID 1 ist eine Spiegelungstechnologie, die Daten auf mehrere Festplatten kopiert und so Redundanz bietet. Die Lese-/Schreibgeschwindigkeiten von RAID 1 hängen von der Geschwindigkeit einer einzelnen Festplatte ab, da Daten von mehreren Festplatten gelesen werden müssen. Fällt eine Festplatte aus, können die anderen weiterhin Daten bereitstellen.

   .. note:: Für RAID 0 oder RAID 1 müssen mindestens 2 Datenträger eingebunden sein. Bei RAID 0 entspricht die Kapazität des RAID-Volumes der Summe der Kapazitäten aller Festplatten. Bei RAID 1 entspricht die Kapazität des RAID-Volumes der Kapazität der kleinsten Festplatte.

   1. Klicken Sie im Menü ``System`` auf die Option ``Plugins``, suchen Sie das Plugin ``openmediavault-md`` und installieren Sie es.

   .. image:: img/omv/omv-raid-1.png

   2. Klicken Sie im Menü ``Storage`` auf die Option ``Disks`` und löschen Sie zwei SSDs.

   .. image:: img/omv/omv-raid-2.png

   3. Bitte beachten Sie, dass dieser Vorgang alle Daten auf den Festplatten löscht. Stellen Sie sicher, dass Sie alle wichtigen Daten gesichert haben.

   .. image:: img/omv/omv-raid-3.png

   4. Wählen Sie als Löschmodus ``QUICK``, das ist ausreichend.

   .. image:: img/omv/omv-raid-4.png

   5. Gehen Sie zum Tab ``Multiple Device`` und klicken Sie auf ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. In der Option Level können Sie Stripe (RAID 0) oder Mirror (RAID 1) wählen. Wählen Sie in der Option Devices die soeben gelöschten Festplatten aus. Klicken Sie auf ``Save`` und warten Sie, bis die RAID-Konfiguration abgeschlossen ist.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Wenn ein Fehlerbericht (500 - Internal Server Error) erscheint, versuchen Sie, das OMV-System neu zu starten.

   7. Wenden Sie die Konfiguration an, indem Sie auf die Schaltfläche ``Apply`` klicken.

   .. image:: img/omv/omv-raid-7.png

   8. Nachdem die RAID-Konfiguration abgeschlossen ist, müssen Sie warten, bis der Status des RAIDs ``100%`` beträgt.

   .. image:: img/omv/omv-raid-8.png

   9. Nach Abschluss der RAID-Konfiguration befinden sich Ihre Festplatten nun in einer RAID 0- oder RAID 1-Konfiguration und Sie können sie als ein einziges Speichergerät verwenden.

5. Speicher konfigurieren
-------------------------------------------------------

   Klicken Sie in der Hauptoberfläche von OpenMediaVault im linken Menü auf die Option ``Storage``. Klicken Sie auf der Seite ``Storage`` auf den Tab ``Disks``. Auf der Seite ``Disks`` sehen Sie alle Festplatten Ihres Raspberry Pi. Stellen Sie sicher, dass Ihr NVMe PIP eine angeschlossene Festplatte hat.

   .. image:: img/omv/omv-disk.png

   1. Klicken Sie in der Seitenleiste auf die Option ``File System``. Erstellen Sie dann ein Dateisystem und hängen Sie es ein. Wählen Sie als Dateisystemtyp ``ext4``.

   .. image:: img/omv/omv-mount.png

   2. Wählen Sie das Gerät (Device) aus und speichern Sie.

   .. note:: Wenn Sie RAID eingerichtet haben, sehen Sie das RAID-Gerät in der Liste. Wählen Sie es einfach aus und speichern Sie.

   .. image:: img/omv/omv-mount-2.png

   3. Es erscheint ein Fenster, das Sie darüber informiert, dass das Dateisystem erstellt wird. Bitte warten Sie einen Moment.

   .. image:: img/omv/omv-mount-3.png

   4. Nach Abschluss gelangen Sie in die Oberfläche ``Mount``. Wählen Sie das soeben erstellte Dateisystem aus und hängen Sie es in Ihren Raspberry Pi ein.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Wenn Sie zwei Festplatten verwenden (und kein RAID), wiederholen Sie die obigen Schritte, um auch die zweite Festplatte in Ihren Raspberry Pi einzuhängen.

   5. Nach dem Einhängen klicken Sie bitte auf Apply. Anschließend können Sie die Daten auf Ihren Festplatten im Dateisystem sehen.

   .. image:: img/omv/omv-mount-5.png

   An diesem Punkt haben Sie OpenMediaVault erfolgreich konfiguriert und Ihre Festplatten eingehängt. Sie können nun OpenMediaVault zur Verwaltung Ihres Speichers verwenden.


6. Einen freigegebenen Ordner erstellen
---------------------------------------

   1. Gehen Sie auf der Seite ``Storage`` zum Tab ``Shared Folders`` und klicken Sie auf die Schaltfläche ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. Geben Sie auf der Seite ``Create Shared Folder`` den Namen des freigegebenen Ordners ein, wählen Sie die Festplatte aus, die Sie freigeben möchten, den Pfad des freigegebenen Ordners und legen Sie die Berechtigungen des freigegebenen Ordners fest. Klicken Sie dann auf die Schaltfläche ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Jetzt können Sie den soeben erstellten freigegebenen Ordner sehen. Bestätigen Sie, dass er korrekt ist, und wenden Sie die Änderungen an (Apply).

   .. image:: img/omv/omv-share-3.png

   Sie haben nun erfolgreich einen freigegebenen Ordner erstellt.


7. Einen neuen Benutzer erstellen
---------------------------------------

   Um auf den Ordner zuzugreifen, müssen wir einen neuen Benutzer erstellen. Bitte folgen Sie diesen Schritten:

   1. Klicken Sie auf der Seite ``User`` auf die Schaltfläche ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. Geben Sie auf der Seite ``Create User`` den Benutzernamen und das Passwort für den neuen Benutzer ein und klicken Sie dann auf die Schaltfläche ``Save``.

   .. image:: img/omv/omv-user-2.png

   Sie haben nun erfolgreich einen neuen Benutzer erstellt.


8. Berechtigungen für den neuen Benutzer festlegen
----------------------------------------------------------------------------

   1. Klicken Sie auf der Seite ``Shared Folders`` auf den soeben erstellten freigegebenen Ordner. Klicken Sie dann auf die Schaltfläche ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. Legen Sie auf der Seite ``Permissions`` die Berechtigungen fest. Klicken Sie dann auf die Schaltfläche ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Klicken Sie nach Abschluss auf die Schaltfläche ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Sie können nun diesen neuen Benutzer verwenden, um auf Ihren freigegebenen Ordner zuzugreifen.


9. Den SMB-Dienst konfigurieren
---------------------------------------

   1. Suchen Sie auf der Seite ``Services`` den Punkt ``SMB/CIFS`` > Tab ``Setting``. Aktivieren Sie die Option ``Enable``. Klicken Sie dann auf die Schaltfläche ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Wenden Sie die Änderungen durch Klicken auf die Schaltfläche ``Apply`` an.

   .. image:: img/omv/omv-smb-2.png

   3. Gehen Sie zur Seite ``Shares`` und klicken Sie auf die Schaltfläche ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. Wählen Sie auf der Seite ``Create Share`` den Pfad des freigegebenen Ordners aus. Klicken Sie dann auf die Schaltfläche ``Save``. Übrigens gibt es auf dieser Seite viele Optionen, die Sie nach Bedarf konfigurieren können.

   .. image:: img/omv/omv-smb-4.png

   5. Klicken Sie auf ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Sie haben nun den SMB-Dienst erfolgreich konfiguriert. Sie können jetzt das SMB-Protokoll verwenden, um auf Ihren freigegebenen Ordner zuzugreifen.


10. Auf den freigegebenen Ordner unter Windows zugreifen
----------------------------------------------------------------------------------

   1. Öffnen Sie ``Dieser PC`` und klicken Sie dann auf ``Netzlaufwerk verbinden``.

   .. image:: img/omv/omv-network-location-1.png

   2. Geben Sie im daraufhin angezeigten Dialogfeld im Feld ``Ordner`` die IP des Raspberry Pi ein, z.B. ``\\192.168.1.100\``, oder den Hostnamen des Raspberry Pi, z.B. ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Klicken Sie auf die Durchsuchen-Schaltfläche und wählen Sie dann den freigegebenen Ordner aus, auf den Sie zugreifen möchten. Während dieses Vorgangs müssen Sie den zuvor erstellten Benutzernamen und das Passwort eingeben.

   .. image:: img/omv/omv-network-location-3.png

   4. Aktivieren Sie "Verbindung bei Anmeldung wiederherstellen" und klicken Sie auf die Schaltfläche ``Fertig stellen``.

   .. image:: img/omv/omv-network-location-4.png

   5. Sie können jetzt auf den NAS-freigegebenen Ordner zugreifen.

   .. image:: img/omv/omv-network-location-5.png

10. Auf den freigegebenen Ordner unter Mac zugreifen
------------------------------------------------------------------------

   1. Klicken Sie im Menü ``Gehe zu`` auf ``Mit Server verbinden``.

   .. image:: img/omv/omv-mac-1.png

   2. Geben Sie im daraufhin angezeigten Dialogfeld die IP des Raspberry Pi ein, z.B. ``smb://192.168.1.100``, oder den Hostnamen des Raspberry Pi, z.B. ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Klicken Sie auf die Schaltfläche ``Verbinden``.

   .. image:: img/omv/omv-mac-3.png

   4. Geben Sie im daraufhin angezeigten Dialogfeld den zuvor erstellten Benutzernamen und das Passwort ein. Klicken Sie auf die Schaltfläche ``Verbinden``.

   .. image:: img/omv/omv-mac-4.png

   5. Sie können jetzt auf den NAS-freigegebenen Ordner zugreifen.

   .. image:: img/omv/omv-mac-5.png