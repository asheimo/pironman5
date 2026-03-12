.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikfans tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _set_up_batocera_mini:

Einrichtung unter Batocera.linux
=========================================================

Wenn du das Betriebssystem Batocera.linux installiert hast, kannst du dich per SSH mit dem System verbinden und anschließend die folgenden Schritte zur Konfiguration durchführen.

#. Sobald das System gestartet ist, verbindest du dich per SSH mit dem Pironman5. Unter Windows öffnest du **Powershell**, unter Mac OS X oder Linux direkt das **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Der Standard-Hostname für das Batocera-System ist ``batocera``, der Standard-Benutzername ``root`` und das Passwort ``linux``. Du kannst dich also mit dem Befehl ``ssh root@batocera.local`` anmelden und das Passwort ``linux`` eingeben.

   .. image:: img/batocera_login.png
      :width: 90%

#. Führe den Befehl ``/etc/init.d/S92switch setup`` aus, um in das Einstellungsmenü zu gelangen.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Navigiere mit der Pfeil-nach-unten-Taste bis zum Ende und aktiviere dort die **Pironman5**-Dienste.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Nachdem du den Pironman5-Dienst aktiviert hast, wähle **OK** aus.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Führe den Befehl ``reboot`` aus, um den Pironman5 neu zu starten.

   .. code-block:: shell

      reboot

#. Nach dem Neustart wird der ``pironman5.service`` automatisch gestartet. Hier die wichtigsten Konfigurationen des Pironman 5:

   * Vier WS2812-RGB-LEDs leuchten blau im Atmungsmodus.
   * Die RGB-Lüfter sind standardmäßig auf den Modus **ausgewogen** eingestellt. Weitere Informationen zu unterschiedlichen Temperaturgrenzen findest du unter :ref:`cc_control_fan_mini`.

Jetzt kannst du den Pironman 5 mit einem Bildschirm, Controllern, Kopfhörern und weiteren Geräten verbinden und in dein Gaming-Erlebnis eintauchen.

.. note::

   An diesem Punkt haben Sie den Pironman 5 Mini erfolgreich eingerichtet, und er ist einsatzbereit.
   
   Für die erweiterte Steuerung seiner Komponenten verweisen wir auf :ref:`view_control_commands_mini`.
