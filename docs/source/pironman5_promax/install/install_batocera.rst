.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Batocera-Betriebssystem installieren
=============================================

Folgen Sie dem untenstehenden Tutorial, um das System auf Ihre Micro-SD-Karte zu installieren.


**Benötigte Komponenten**

* Ein Personal Computer
* Eine Micro-SD-Karte und ein Kartenleser

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Betriebssystem auf der microSD-Karte installieren
-----------------------------------------------------------------------


.. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>


1. Laden Sie die neueste Version des Betriebssystems von der Website |shared_link_batocera_linux| herunter.

2. Legen Sie Ihre microSD-Karte mit einem Kartenleser in Ihren Computer ein.
   Sichern Sie vor dem Fortfahren alle wichtigen Daten auf der Karte, da diese gelöscht werden.

   .. image:: img/insert_sd.png
      :width: 90%

3. Wenn **Raspberry Pi Imager** geöffnet wird, sehen Sie die Seite **Gerät**.
   Wählen Sie Ihr **Raspberry Pi 5**-Modell aus der Liste aus.

   .. image:: img/imager_device.png
      :width: 90%

4. Gehen Sie zum Bereich **Betriebssystem**, scrollen Sie nach unten zum Ende der Seite und wählen Sie **Benutzerdefiniertes Betriebssystem verwenden**.

   .. image:: img/imager_use_custom.png
      :width: 90%

5. Wählen Sie die soeben heruntergeladene Datei **batocera-bcmxxxxxxx.img.gz** aus und klicken Sie auf **Öffnen**.

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. Wählen Sie im Bereich **Speicher** Ihre microSD-Karte aus.
   Aus Sicherheitsgründen wird empfohlen, andere USB-Speichergeräte zu trennen, sodass nur die microSD-Karte in der Liste erscheint.

   .. image:: img/imager_storage.png
      :width: 90%

#. Klicken Sie auf **WEITER** und gehen Sie direkt zum **Schreiben**, wo das Betriebssystem auf die microSD-Karte geschrieben wird.

   .. image:: img/imager_betocera_write.png
      :width: 90%

#. Wenn das Popup **"Schreiben erfolgreich"** erscheint, wurde das Image vollständig geschrieben und verifiziert. Sie können die microSD-Karte jetzt sicher entfernen und verwenden, um Ihren Raspberry Pi zu starten.

   .. image:: img/imager_betocera_finish.png
      :width: 90%