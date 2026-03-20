.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _control_commands_dashboard_5:

5. Steuerung mit Befehlen oder Dashboard
=======================================================

Sobald das ``pironman5``-Modul erfolgreich installiert wurde, startet der ``pironman5.service`` automatisch nach jedem Neustart.

Sie können den Pironman 5 entweder über Befehle überwachen und steuern oder das Dashboard über die Webseite unter ``http://<ip>:34001`` aufrufen.

.. note::

    * Für das **Home Assistant**-System können Sie den Pironman 5 nur über das Dashboard überwachen und steuern, indem Sie die Webseite unter ``http://<ip>:34001`` öffnen.

.. * Für das **Batocera.linux**-System können Sie den Pironman 5 nur über Befehle überwachen und steuern. Es ist wichtig zu beachten, dass alle Änderungen an der Konfiguration einen Neustart des Dienstes mit ``pironman5 restart`` erfordern, damit sie wirksam werden.

.. toctree::
    :maxdepth: 1

    control_with_dashboard 
    control_with_commands