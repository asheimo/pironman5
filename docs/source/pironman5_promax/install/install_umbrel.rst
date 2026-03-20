Umbrel OS installieren
============================================

Umbrel ist eine Open-Source, selbst-gehostete Heimserver-Plattform / ein Betriebssystem, mit dem Sie Ihren eigenen Bitcoin-Knoten betreiben, eine Vielzahl von Ein-Klick-Self-Hosted-Apps installieren und Ihre Hardware in Ihre persönliche Heim-Cloud verwandeln können. Es ist eine hervorragende Möglichkeit, mit Selbstverwahrung und Privatsphäre zu beginnen.

**Benötigte Komponenten**

* Ein Personal Computer
* Eine NVMe-SSD
* Ein NVMe-zu-USB-Adapter
* Micro-SD-Karte und Kartenleser

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Betriebssystem auf der NVMe-SSD installieren
-----------------------------------------------------------------------------

Jetzt sind Sie bereit, das Betriebssystem auf Ihrer **NVMe-SSD** zu installieren.
Befolgen Sie einfach die folgenden Schritte sorgfältig – dieser Leitfaden ist für Anfänger geschrieben und leicht verständlich.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. Laden Sie das neueste **Umbrel OS**-Image herunter und entpacken Sie die Datei. Wenn Sie eine bestimmte Version verwenden möchten, können Sie auch die Seite |link_umbrel_release| besuchen.

   * :download:`Neuestes Umbrel OS-Image <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Schließen Sie die **NVMe-SSD** mit einem **NVMe-zu-USB-Adapter** an Ihren Computer an.

#. Öffnen Sie **Raspberry Pi Imager**. Wählen Sie auf dem Bildschirm **Gerät** Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

#. Gehen Sie zum Bereich **Betriebssystem**, scrollen Sie nach unten und wählen Sie **Benutzerdefiniertes Betriebssystem verwenden**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Wählen Sie die zuvor heruntergeladene und entpackte **Umbrel OS-Imagedatei** aus und klicken Sie dann auf **Öffnen**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Klicken Sie auf **Weiter**, um fortzufahren.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. Wählen Sie im Bereich **Speicher** Ihre **NVMe-SSD** aus. Stellen Sie sicher, dass Sie die NVMe-SSD und nicht ein anderes Laufwerk Ihres Computers auswählen.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Überprüfen Sie alle Einstellungen sorgfältig und klicken Sie dann auf **SCHREIBEN**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Wenn die NVMe-SSD bereits Daten enthält, warnt Sie Raspberry Pi Imager, dass alle Daten gelöscht werden. Überprüfen Sie noch einmal, dass das richtige Laufwerk ausgewählt ist, und klicken Sie dann auf **ICH VERSTEHE, LÖSCHEN UND SCHREIBEN**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Wenn die Meldung **“Schreiben abgeschlossen”** erscheint, wurde das Image erfolgreich geschrieben und verifiziert.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%