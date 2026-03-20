.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _set_up_umbrel_promax:

Einrichtung unter Umbrel OS
======================================================================

Wenn Sie Umbrel OS auf Ihrem Raspberry Pi 5 installiert haben, müssen Sie den Pironman 5 Pro MAX über die Befehlszeile konfigurieren. Detaillierte Anweisungen finden Sie unten:

#. Verbinden Sie Ihren Raspberry Pi 5 mit einem Ethernet-Kabel mit Ihrem Netzwerk. Dieser Schritt ist notwendig, um sicherzustellen, dass Ihr Raspberry Pi Internetzugang hat.

#. Besuchen Sie in Ihrem Browser: ``http://umbrel.local``. Wenn die Seite nicht geöffnet wird, suchen Sie in Ihrem Router nach der IP-Adresse des Umbrel-Geräts, z.B.: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Erstellen Sie Ihr Umbrel-Konto, indem Sie einen Benutzernamen und ein Passwort festlegen. Dieses Passwort wird für den zukünftigen Fernzugriff auf Umbrel verwendet, merken Sie es sich also.

   .. image:: img/umbrel_account.png

#. Klicken Sie auf **Weiter**, um die Umbrel-Einrichtung abzuschließen und die Desktop-Umgebung zu betreten.

   .. image:: img/umbrel_desktop.png

#. Öffnen Sie das Terminal. Klicken Sie auf dem Desktop auf das Symbol **Einstellungen**, wählen Sie dann **Erweiterte Einstellungen** und klicken Sie auf **Öffnen**.

   .. image:: img/umbrel_setting.png

#. Klicken Sie auf **Terminal öffnen**.

   .. image:: img/umbrel_open_terminal.png

#. Sie können wählen, ob Sie das Terminal in Umbrel OS oder innerhalb einer bestimmten App öffnen möchten. Beide Optionen führen Sie zur Terminal-Oberfläche.

   .. image:: img/umbrel_terminal.png

#. Fahren Sie fort, den Code von GitHub herunterzuladen und das Modul ``pironman5`` zu installieren.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Nachdem die Installation abgeschlossen ist, geben Sie den folgenden Befehl ein, um Ihren Raspberry Pi neu zu starten.

   .. code-block:: shell

      sudo reboot

#. Nach dem Neustart wird der ``pironman5.service`` automatisch gestartet. Hier sind die primären Konfigurationen für den Pironman 5 Pro MAX:

   * Der OLED-Bildschirm zeigt CPU, RAM, Festplattenauslastung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.
   * Vier WS2812-RGB-LEDs leuchten blau im Atmungsmodus.


#. Sie können das ``systemctl``-Werkzeug verwenden, um den ``pironman5.service`` zu ``starten``, zu ``stoppen``, ``neu zu starten`` oder den ``Status`` zu überprüfen.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Verwenden Sie diesen Befehl, um alle Änderungen an den Einstellungen des Pironman 5 Pro MAX zu übernehmen.
   * ``start/stop``: Aktivieren oder deaktivieren Sie den ``pironman5.service``.
   * ``status``: Überprüfen Sie den Betriebsstatus des ``pironman5``-Programms mit dem ``systemctl``-Werkzeug.

.. note::

   An diesem Punkt haben Sie den Pironman 5 Pro MAX erfolgreich eingerichtet und er ist einsatzbereit.

   Informationen zur erweiterten Steuerung seiner Komponenten finden Sie unter :ref:`control_commands_dashboard_promax`.