.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit Gleichgesinnten noch tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei Problemen nach dem Kauf und technischen Herausforderungen – durch unsere Community und unser Support-Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erfahre als Erste:r von neuen Produkten und genieße exklusive Einblicke.
    - **Besondere Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an saisonalen Events und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde heute noch Mitglied!

FAQ
============

1. Über kompatible Systeme
-------------------------------

Systeme, die den Test auf dem Raspberry Pi 5 bestanden haben:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. Über die Einschalttaste
--------------------------

Die Einschalttaste führt die Power-Taste des Raspberry Pi 5 heraus und funktioniert genauso wie die Power-Taste des Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Herunterfahren**

  * Wenn Sie das **Raspberry Pi OS Desktop**-System verwenden, können Sie die Einschalttaste zweimal schnell hintereinander drücken, um herunterzufahren.
  * Wenn Sie das **Raspberry Pi OS Lite**-System verwenden, drücken Sie die Einschalttaste einmal, um ein Herunterfahren einzuleiten.
  * Um ein erzwungenes Herunterfahren durchzuführen, halten Sie die Einschalttaste gedrückt.

* **Einschalten**

  * Wenn das Raspberry Pi-Board heruntergefahren, aber noch mit Strom versorgt ist, drücken Sie die Taste einmal, um es aus dem Herunterfahrzustand einzuschalten.

* Wenn Sie ein System verwenden, das die Ausschalt-Taste nicht unterstützt, können Sie sie 5 Sekunden lang gedrückt halten, um ein erzwungenes Herunterfahren durchzuführen, und einmal drücken, um wieder einzuschalten.

3. Über den Raspberry Pi AI HAT+
----------------------------------------------------------

Der Raspberry Pi AI HAT+ ist nicht mit dem Pironman 5 kompatibel.

   .. image::  img/output3.png
        :width: 400

Das Raspberry Pi AI Kit kombiniert den Raspberry Pi M.2 HAT+ und das Hailo AI-Beschleunigermodul.

   .. image::  img/output2.jpg
        :width: 400

Sie können das Hailo AI-Beschleunigermodul vom Raspberry Pi AI Kit abnehmen und direkt in das NVMe PIP-Modul des Pironman 5 MAX einsetzen.

   .. .. image::  img/output4.png
   ..      :width: 800

4. Über die Kupferrohrenden des Tower-Kühlers
----------------------------------------------------------

Die U-förmigen Heatpipes an der Oberseite des Tower-Kühlers sind zusammengedrückt, damit die Kupferrohre durch die Aluminiumlamellen geführt werden können. Dies ist Teil des normalen Produktionsprozesses für Kupferrohre.

   .. image::  img/tower_cooler1.png

5. PI5 startet nicht (rote LED)?
-------------------------------------------

Dieses Problem kann durch ein Systemupdate, Änderungen der Bootreihenfolge oder einen beschädigten Bootloader verursacht werden. Sie können die folgenden Schritte ausprobieren, um das Problem zu beheben:

#. Überprüfen Sie die USB-HDMI-Adapter-Verbindung

   * Bitte überprüfen Sie sorgfältig, ob der USB-HDMI-Adapter korrekt mit dem PI5 verbunden ist.
   * Versuchen Sie, den USB-HDMI-Adapter abzuziehen und wieder anzuschließen.
   * Schließen Sie dann die Stromversorgung wieder an und prüfen Sie, ob der PI5 erfolgreich startet.

#. Testen Sie den PI5 außerhalb des Gehäuses

   * Wenn das erneute Anschließen des Adapters das Problem nicht löst:
   * Entfernen Sie den PI5 aus dem Pironman 5 Gehäuse.
   * Versorgen Sie den PI5 direkt mit dem Netzteil (ohne das Gehäuse).
   * Überprüfen Sie, ob er normal startet.

#. Bootloader wiederherstellen

   * Wenn der PI5 immer noch nicht startet, ist möglicherweise der Bootloader beschädigt. Sie können dieser Anleitung folgen: :ref:`update_bootloader_max` und wählen, ob von SD-Karte oder NVMe/USB gebootet werden soll.
   * Legen Sie die vorbereitete SD-Karte in den PI5 ein, schalten Sie ihn ein und warten Sie mindestens 10 Sekunden. Sobald die Wiederherstellung abgeschlossen ist, entfernen und formatieren Sie die SD-Karte erneut.
   * Verwenden Sie dann Raspberry Pi Imager, um das neueste Raspberry Pi OS auf die SD-Karte zu flashen, setzen Sie die Karte wieder ein und versuchen Sie erneut zu starten.

6. OLED-Bildschirm funktioniert nicht?
------------------------------------------------

Wenn der OLED-Bildschirm nichts anzeigt oder falsch anzeigt, folgen Sie diesen Schritten zur Fehlerbehebung:

1. **Überprüfen Sie die Verbindung des OLED-Bildschirms**

   Stellen Sie sicher, dass das FPC-Kabel des OLED-Bildschirms richtig angeschlossen ist.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

2. **Überprüfen Sie die OS-Kompatibilität**

   Stellen Sie sicher, dass Sie ein kompatibles Betriebssystem auf Ihrem Raspberry Pi verwenden.

3. **Überprüfen Sie die I2C-Adresse**

   Führen Sie den folgenden Befehl aus, um zu prüfen, ob die I2C-Adresse (0x3C) des OLED erkannt wird:

   .. code-block:: shell

      sudo i2cdetect -y 1

   Wenn die Adresse nicht erkannt wird, aktivieren Sie I2C mit folgendem Befehl:

   .. code-block:: shell

      sudo raspi-config

4. **Starten Sie den pironman5-Dienst neu**

   Starten Sie den `pironman5`-Dienst neu, um zu sehen, ob das Problem behoben ist:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Überprüfen Sie die Protokolldatei**

   Wenn das Problem weiterhin besteht, überprüfen Sie die Protokolldatei auf Fehlermeldungen und geben Sie die Informationen an den Kundensupport weiter, um eine weitere Analyse zu ermöglichen:

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log

7. NVMe PIP-Modul funktioniert nicht?
---------------------------------------

1. Stellen Sie sicher, dass das FPC-Kabel, das das NVMe PIP-Modul mit dem Raspberry Pi 5 verbindet, korrekt angeschlossen ist.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

2. Bestätigen Sie, dass Ihre SSD korrekt im NVMe PIP-Modul befestigt ist.  

3. Überprüfen Sie den Status der LEDs des NVMe PIP-Moduls:

   Nachdem alle Verbindungen bestätigt wurden, schalten Sie den Pironman 5 MAX ein und beobachten Sie die beiden Anzeigen am NVMe PIP-Modul:  

   * **PWR-LED**: Sollte leuchten.  
   * **STA-LED**: Sollte blinken, um den normalen Betrieb anzuzeigen.  

   .. image:: img/dual_nvme_pip_leds.png  

   * Wenn die **PWR-LED** leuchtet, die **STA-LED** jedoch nicht blinkt, bedeutet dies, dass die NVMe-SSD vom Raspberry Pi nicht erkannt wird.  
   * Wenn die **PWR-LED** aus ist, überbrücken Sie die "Force Enable"-Pins am Modul. Wenn die **PWR-LED** leuchtet, könnte dies auf ein loses FPC-Kabel oder eine nicht unterstützte Systemkonfiguration für NVMe hinweisen.

   .. image:: img/dual_nvme_pip_j4.png  

4. Stellen Sie sicher, dass auf Ihrer NVMe SSD ein korrekt installiertes Betriebssystem vorhanden ist. Siehe: :ref:`install_the_os_max`.

5. Wenn die Verkabelung korrekt ist und das OS installiert wurde, die NVMe SSD aber immer noch nicht bootet, versuchen Sie, von einer Micro-SD-Karte zu booten, um die Funktionalität anderer Komponenten zu überprüfen. Sobald bestätigt, fahren Sie fort mit: :ref:`configure_boot_ssd_max`.

Wenn das Problem nach den obigen Schritten weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

8. RGB-LEDs funktionieren nicht?
--------------------------------------------

#. Die beiden Pins am IO-Expander oberhalb von J9 werden verwendet, um die RGB-LEDs mit GPIO10 zu verbinden. Stellen Sie sicher, dass die Jumperkappe korrekt auf diesen beiden Pins sitzt.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Überprüfen Sie, ob der Raspberry Pi ein kompatibles Betriebssystem ausführt. Der Pironman 5 unterstützt nur die folgenden OS-Versionen:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Wenn Sie ein nicht unterstütztes OS installiert haben, folgen Sie der Anleitung zur Installation eines kompatiblen Betriebssystems: :ref:`install_the_os_max`.

#. Führen Sie den Befehl ``sudo raspi-config`` aus, um das Konfigurationsmenü zu öffnen. Navigieren Sie zu **3 Interfacing Options** -> **I3 SPI** -> **YES**, klicken Sie dann auf **OK** und **Finish**, um SPI zu aktivieren. Starten Sie nach dem Aktivieren von SPI den Pironman 5 neu.

Wenn das Problem nach den obigen Schritten weiterhin besteht, senden Sie bitte eine E-Mail an service@sunfounder.com. Wir werden so schnell wie möglich antworten.

9. CPU-Lüfter funktioniert nicht?
----------------------------------------------

Wenn die CPU-Temperatur die eingestellte Schwelle nicht erreicht hat, funktioniert der CPU-Lüfter nicht.

**Lüfterdrehzahlsteuerung basierend auf Temperatur**  

Der PWM-Lüfter arbeitet dynamisch und passt seine Drehzahl entsprechend der Temperatur des Raspberry Pi 5 an:  

* **Unter 50°C**: Lüfter bleibt aus (0 % Drehzahl).  
* **Bei 50°C**: Lüfter läuft mit niedriger Geschwindigkeit (30 %).  
* **Bei 60°C**: Lüfter erhöht auf mittlere Geschwindigkeit (50 %).  
* **Bei 67,5°C**: Lüfter erhöht auf hohe Geschwindigkeit (70 %).  
* **Bei 75°C und höher**: Lüfter läuft mit voller Geschwindigkeit (100 %).  

Weitere Details finden Sie unter : :ref:`fan_max`

10. Wie weckt man den OLED-Bildschirm auf?
---------------------------------------------------------------------------------

Um Strom zu sparen und die Lebensdauer des Bildschirms zu verlängern, schaltet sich der OLED-Bildschirm nach einer gewissen Inaktivität automatisch ab. Dies ist Teil des normalen Designs und beeinträchtigt die Funktionalität des Produkts nicht.

Sie können die Taste drücken und den Bildschirm aktivieren.

.. note::

   Für die Konfiguration des OLED-Bildschirms (z. B. Ein/Aus, Schlafzeit, Drehung usw.) siehe bitte: :ref:`max_view_control_dashboard` oder :ref:`max_view_control_commands`.

11. Wie deaktiviere ich das Web-Dashboard?
------------------------------------------------------

Nach Abschluss der Installation des ``pironman5``-Moduls können Sie auf das :ref:`max_view_control_dashboard` zugreifen.
      
Wenn Sie diese Funktion nicht benötigen und die CPU- und RAM-Auslastung reduzieren möchten, können Sie das Dashboard während der Installation von ``pironman5`` mit dem Flag ``--disable-dashboard`` deaktivieren.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Wenn Sie ``pironman5`` bereits installiert haben, können Sie das ``dashboard``-Modul und ``influxdb`` entfernen und dann pironman5 neu starten, um die Änderungen zu übernehmen:
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5


12. Wie steuert man Komponenten mit dem ``pironman5``-Befehl?
----------------------------------------------------------------------

Sie können das folgende Tutorial verwenden, um die Komponenten des Pironman 5 MAX mit dem ``pironman5``-Befehl zu steuern.

* :ref:`max_view_control_commands`


13. Wie ändere ich die Boot-Reihenfolge des Raspberry Pi mit Befehlen?
-----------------------------------------------------------------------------------

Wenn Sie bereits in Ihrem Raspberry Pi eingeloggt sind, können Sie die Boot-Reihenfolge mit Befehlen ändern. Detaillierte Anweisungen finden Sie hier:

* :ref:`configure_boot_ssd_max`


14. Wie ändere ich die Boot-Reihenfolge mit Raspberry Pi Imager?
---------------------------------------------------------------------------

Zusätzlich zur Änderung des ``BOOT_ORDER`` in der EEPROM-Konfiguration können Sie auch den **Raspberry Pi Imager** verwenden, um die Boot-Reihenfolge Ihres Raspberry Pi zu ändern.

Es wird empfohlen, für diesen Schritt eine Ersatzkarte zu verwenden.

* :ref:`update_bootloader_max`


15. Wie kopiere ich das System von der SD-Karte auf eine NVMe-SSD?
--------------------------------------------------------------------------

Wenn Sie eine NVMe-SSD haben, aber keinen Adapter, um Ihre NVMe mit Ihrem Computer zu verbinden, können Sie das System zunächst auf Ihrer Micro-SD-Karte installieren. Sobald der Pironman 5 MAX erfolgreich gestartet ist, können Sie das System von Ihrer Micro-SD-Karte auf Ihre NVMe-SSD kopieren. Detaillierte Anweisungen finden Sie hier:

* :ref:`copy_sd_to_nvme_max`


16. Wie entfernt man die Schutzfolie von den Acrylplatten?
-----------------------------------------------------------------

Im Paket sind zwei Acrylplatten enthalten, die auf beiden Seiten mit einer gelben/transparenten Schutzfolie überzogen sind, um Kratzer zu vermeiden. Die Schutzfolie kann etwas schwer zu entfernen sein. Verwenden Sie einen Schraubendreher, um vorsichtig an den Ecken zu kratzen, und ziehen Sie dann die gesamte Folie ab.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center


.. _max_openssh_powershell:

17. Wie installiere ich OpenSSH über Powershell?
--------------------------------------------------

Wenn Sie ``ssh <Benutzername>@<Hostname>.local`` (oder ``ssh <Benutzername>@<IP-Adresse>``) verwenden, um sich mit Ihrem Raspberry Pi zu verbinden, aber die folgende Fehlermeldung erscheint:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Bedeutet dies, dass Ihr Computersystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen es manuell nach folgender Anleitung installieren:

#. Geben Sie ``powershell`` in das Suchfeld Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im erscheinenden Menü ``Als Administrator ausführen``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      
#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird die folgende Ausgabe zurückgegeben.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfen Sie die Installation mit folgendem Befehl.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Nun wird Ihnen angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

        Wenn die obige Meldung nicht erscheint, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist. In diesem Fall sollten Sie ein Drittanbieter-SSH-Tool wie |link_putty| installieren.

#. Starten Sie nun PowerShell neu und führen Sie es weiterhin als Administrator aus. An diesem Punkt können Sie sich mit dem ``ssh``-Befehl bei Ihrem Raspberry Pi anmelden. Sie werden dann nach dem Passwort gefragt, das Sie zuvor eingerichtet haben.

   .. image:: img/powershell_login.png


18. Wenn ich OMV einrichte, kann ich dann trotzdem die Funktionen des Pironman5 nutzen?
--------------------------------------------------------------------------------------------------------

Ja, OpenMediaVault wird auf dem Raspberry-Pi-System eingerichtet. Bitte folgen Sie den Schritten in :ref:`max_set_up_pi_os`, um die Konfiguration fortzusetzen.

19. Kann ich die Vibrationsschalterfunktion des Pironman5 Max verwenden?
----------------------------------------------------------------------------------------------------------------------------

Die Vibrationsschalterfunktion des Pironman5 Max ist ab Version 1.3.6 nicht mehr softwarekompatibel. Dies ist eine Änderung, die durch die Versionseinführung entstanden ist, und kein Hardwarefehler. Wenn Sie auf diese Funktion angewiesen sind, können Sie in Betracht ziehen, auf eine frühere Version zurückzusetzen, den Code manuell anzupassen oder eine Anfrage an den offiziellen Support zu senden. Die Anzeigedauer des OLED-Bildschirms kann weiterhin über die Befehlszeile angepasst werden. Der OLED-Bildschirm wird durch einmaliges Drücken der Taste aktiviert und bleibt einige Sekunden lang eingeschaltet.

20. Das Dashboard zeigt keine Daten an (Temperatur, Statistiken, Diagramme sind leer)
----------------------------------------------------------------------------------------------------------------------------

1. Bitte leeren Sie den Cache Ihres Browsers oder rufen Sie die Dashboard-Seite im Inkognito-/Privaten Modus Ihres Browsers auf.

2. Um den aktuellen Status weiter zu überprüfen, wird empfohlen, zunächst zu prüfen, ob die folgenden beiden Dienste ordnungsgemäß ausgeführt werden:

   .. code-block::

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   Beide Dienste sollten als ``active (running)`` angezeigt werden.

3. Wenn die Dienste nicht ordnungsgemäß ausgeführt werden, können Sie versuchen, Folgendes auszuführen:

   .. code-block::

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   Warten Sie dann etwa 30 Sekunden und aktualisieren Sie die Dashboard-Seite, um dies zu überprüfen.