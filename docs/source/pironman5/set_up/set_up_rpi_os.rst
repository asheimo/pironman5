.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit der Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Konfiguration unter Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
==================================================================


.. image:: img/pironman5_pic.jpg
    :width: 400
    :align: center


Wenn du Raspberry Pi OS, Ubuntu, Kali Linux oder Homebridge auf deinem Raspberry Pi installiert hast, musst du den Pironman 5 über die Befehlszeile konfigurieren. Nachfolgend findest du detaillierte Anleitungen.

.. note::

  Bevor du mit der Konfiguration fortfährst, musst du deinen Raspberry Pi starten und dich anmelden.  
  Wenn du dir nicht sicher bist, wie du dich anmeldest, kannst du die offizielle Website von Raspberry Pi besuchen: |link_rpi_get_start|.


Konfiguration des Herunterfahrens zur Deaktivierung der GPIO-Stromversorgung
--------------------------------------------------------------------------------------

Um zu verhindern, dass das vom GPIO des Raspberry Pi gespeiste OLED-Display und die RGB-Lüfter nach dem Herunterfahren eingeschaltet bleiben, ist es wichtig, den Raspberry Pi so zu konfigurieren, dass die GPIO-Stromversorgung deaktiviert wird.

#. Öffne das EEPROM-Konfigurationstool:

   .. code-block::

      sudo raspi-config

#. Gehe zu **Advanced Options → A12 Shutdown Behaviour**.

   .. image:: img/shutdown_behaviour.png

#. Wähle **B1 Full Power Off**.

   .. image:: img/run_power_off.png

#. Speichere die Änderungen. Du wirst aufgefordert, einen Neustart durchzuführen, damit die neuen Einstellungen wirksam werden.

Download und Installation des Moduls ``pironman5``
-----------------------------------------------------------

.. note::

   Für „Lite“-Systeme installiere zunächst Werkzeuge wie ``git``, ``python3``, ``pip3``, ``setuptools`` usw.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Lade den Code von GitHub herunter und installiere das Modul ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b base https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Nach einer erfolgreichen Installation muss das System neu gestartet werden, um die Installation zu aktivieren. Folge der Aufforderung auf dem Bildschirm, um den Neustart durchzuführen.

   Nach dem Neustart wird der Dienst ``pironman5.service`` automatisch gestartet.  
   Hier sind die Hauptfunktionen der Pironman-5-Konfiguration:
   
   * Das OLED-Display zeigt CPU-, RAM- und Festplattennutzung, CPU-Temperatur und die IP-Adresse des Raspberry Pi an.  
   * Vier WS2812-RGB-LEDs leuchten blau mit einem Atemeffekt.  
   * Die RGB-Lüfter sind standardmäßig auf **Always On** eingestellt. Informationen zur Einstellung der Einschalttemperaturen findest du unter :ref:`cc_control_fan`.

#. Du kannst das Tool ``systemctl`` verwenden, um den Dienst ``pironman5.service`` zu ``starten``, ``stoppen``, ``neustarten`` oder seinen ``Status`` zu überprüfen.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Verwende diesen Befehl, um Änderungen an den Pironman-5-Einstellungen zu übernehmen.  
   * ``start/stop``: Aktiviert oder deaktiviert den Dienst ``pironman5.service``.  
   * ``status``: Überprüft den Betriebsstatus des Programms ``pironman5`` mithilfe des Tools ``systemctl``.

.. note::

   An diesem Punkt hast du den Pironman 5 erfolgreich konfiguriert, und er ist einsatzbereit.  
   Für die erweiterte Steuerung seiner Komponenten siehe :ref:`control_commands_dashboard_5`.
