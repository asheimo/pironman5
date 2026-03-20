.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_batocera:

Einrichtung unter Batocera.linux
=========================================================

Wenn Sie das Batocera.linux-Betriebssystem installiert haben, können Sie sich per SSH remote in dieses System einloggen und dann die folgenden Schritte ausführen, um die Konfiguration abzuschließen.

#. Sobald das System hochgefahren ist, verwenden Sie SSH, um eine Remote-Verbindung zum Pironman5 herzustellen. Für Windows können Sie **Powershell** öffnen, für Mac OS X und Linux können Sie direkt das **Terminal** öffnen.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Der Standard-Hostname für das batocera-System ist ``batocera``, der Standard-Benutzername ist ``root`` und das Passwort ist ``linux``. Sie können sich also anmelden, indem Sie ``ssh root@batocera.local`` eingeben und das Passwort ``linux`` eingeben.

   .. image:: img/batocera_login.png
      :width: 90%

#. Führen Sie den Befehl aus: ``/etc/init.d/S92switch setup``, um die Menüeinstellungsseite aufzurufen.

   .. image:: img/batocera_configure.png
      :width: 90%

#. Navigieren Sie mit der Pfeiltaste nach unten zum Ende, wählen Sie die **Pironman5**-Dienste aus und aktivieren Sie sie.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Nach der Aktivierung des pironman5-Dienstes wählen Sie **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Führen Sie den Befehl ``reboot`` aus, um den Pironman5 neu zu starten.

   .. code-block:: shell

      reboot

#. Nach dem Neustart wird der ``pironman5.service`` automatisch gestartet. Hier sind die primären Konfigurationen für den Pironman 5 Pro MAX:

   * Der OLED-Bildschirm zeigt CPU, RAM, Festplattenauslastung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.
   * Vier WS2812-RGB-LEDs leuchten blau im Atmungsmodus.

Jetzt können Sie den Pironman 5 Pro MAX an einen Bildschirm, Gamecontroller, Kopfhörer usw. anschließen und in Ihre Spielwelt eintauchen.


.. note::

   An diesem Punkt haben Sie den Pironman 5 Pro MAX erfolgreich eingerichtet und er ist einsatzbereit.

   Informationen zur erweiterten Steuerung seiner Komponenten finden Sie unter :ref:`control_commands_dashboard_promax`.