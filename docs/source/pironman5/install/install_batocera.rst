Installation des Batocera-Betriebssystems
==========================================================

Befolgen Sie das folgende Tutorial, um das System auf Ihrer microSD-Karte zu installieren.

**Erforderliche Komponenten**

* Ein persönlicher Computer
* Eine Micro-SD-Karte und ein Kartenlesegerät

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Betriebssystem auf der microSD-Karte installieren
-------------------------------------------------------------------

1. Stecken Sie Ihre microSD-Karte mit einem Kartenlesegerät in Ihren Computer.  
   Sichern Sie vor dem Fortfahren alle wichtigen Daten auf der Karte, da diese gelöscht werden.

   .. image:: img/insert_sd.png
      :width: 90%

2. Wenn sich **Raspberry Pi Imager** öffnet, sehen Sie die Seite **Device (Gerät)**.  
   Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

3. Gehen Sie zum Abschnitt **OS (Betriebssystem)**, scrollen Sie nach unten auf der Seite und wählen Sie Ihr Betriebssystem aus.

   .. note::

      * Für **Ubuntu** klicken Sie auf **Other general-purpose OS (Andere allgemeine Betriebssysteme)** → **Ubuntu** und wählen dann  
        **Ubuntu Desktop 24.04 LTS (64-bit)** oder **Ubuntu Server 24.04 LTS (64-bit)**.
      * Für **Kali Linux**, **Home Assistant** und **Homebridge** klicken Sie auf  
        **Other specific-purpose OS (Andere spezielle Betriebssysteme)** und wählen dann das entsprechende System aus.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Wählen Sie im Abschnitt **Storage (Speicher)** Ihre microSD-Karte aus.  
   Für mehr Sicherheit wird empfohlen, andere USB-Speichergeräte zu trennen, sodass nur die microSD-Karte in der Liste erscheint.

   .. image:: img/imager_storage.png
      :width: 90%

#. Klicken Sie auf **NEXT (WEITER)**.

   .. note::

      * Für Systeme, die **nicht vorkonfiguriert werden können**, überspringt ein Klick auf **NEXT (WEITER)** den Schritt **Customisation (Anpassung)** und geht direkt zu **Writing (Schreiben)** über, wo das Betriebssystem auf die microSD-Karte geschrieben wird.
      * Für Systeme, die **Vorkonfiguration unterstützen**, befolgen Sie die Schritte unter **Customisation (Anpassung)**, um Optionen wie **Hostname**, **WiFi** und die **Aktivierung von SSH** zu konfigurieren.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Wenn das Popup-Fenster **« Write Successful (Schreiben erfolgreich) »** erscheint, wurde das Image vollständig geschrieben und verifiziert. Sie können nun die microSD-Karte sicher entfernen und zum Starten Ihres Raspberry Pi verwenden.