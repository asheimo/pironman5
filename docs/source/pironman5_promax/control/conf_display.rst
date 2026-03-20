.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Display konfigurieren
===================================================================

Dieses Kapitel führt Sie durch die Konfiguration der Display-Einstellungen für den Pironman 5 Pro MAX, einschließlich der Aktivierung des energiesparenden Bildschirm-Ausschaltens und der Einrichtung der Bildschirmumkehrung für spezielle Einbaulagen.


-------------------------------------------------------------------

**Bildschirm-Leerlauf-Sleep einrichten**


Um Strom zu sparen, wenn Sie den Pironman 5 Pro MAX nicht aktiv nutzen, können Sie die automatische Schlaffunktion des Bildschirms aktivieren. Wenn das Gerät für eine festgelegte Zeit im Leerlauf ist, schaltet sich das Hauptdisplay automatisch aus und wechselt in einen stromsparenden Zustand.

Folgen Sie diesen Schritten, um es zu konfigurieren:

1. Klicken Sie unten links auf dem Bildschirm auf **Menü -> Einstellungen**, suchen Sie dann das **Kontrollzentrum** und öffnen Sie es.

   .. image:: img/sleep_screen1.png

2.  Klicken Sie im Kontrollzentrum, um die **Anzeige**-Einstellungen zu öffnen.

3.  Suchen Sie die Option **Bildschirm-Ausschalten** und schalten Sie sie ein.

   .. image:: img/sleep_screen2.png



----------------------------------------------------------------------

**Pironman 5 Pro MAX umdrehen**

Der Pironman 5 Pro MAX kann umgedreht verwendet werden. In dieser Konfiguration befindet sich der Touchscreen oben und die GPIO-Anschlüsse sind unten, was eine größere Flexibilität für verschiedene Projekte bietet. Dieses Setup ist ideal für Anwendungen wie eine bequemere Bildschirmansicht oder einen einfacheren Zugriff auf GPIO-Pins beim Anschließen von Sensoren.

Beim Umdrehen des Geräts müssen beide Displays separat angepasst werden:

   * Haupt-Touchscreen – Erfordert rotations-Einstellungen auf Betriebssystemebene
   * OLED-Statusbildschirm – Erfordert Konfiguration über die Befehlszeile

Um den Pironman 5 Pro MAX umzudrehen, folgen Sie diesen Schritten:


1. Physische Vorbereitung

   Entfernen Sie die Kamera vom Pironman 5 Pro MAX, drehen Sie das gesamte Gerät um und installieren Sie die Kamera wieder. Die Installation sollte symmetrisch zu ihrer ursprünglichen Ausrichtung sein.

   .. image:: img/inverted_screen0.png

2. Touchscreen-Ausrichtung einrichten

   Schalten Sie das Gerät ein. Halten Sie auf dem Touchscreen den Desktop gedrückt, um das Menü aufzurufen, und wählen Sie **Desktop-Einstellungen**.

   .. image:: img/inverted_screen1.png

   Scrollen Sie nach unten, um die Option **Bildschirme** zu finden, und halten Sie dann die Bildschirmanzeige im Display gedrückt. Wählen Sie **Ausrichtung → Umgekehrt**.

   .. image:: img/inverted_screen2.png

   Übernehmen Sie die Einstellungen. Das Aktualisierungsfenster zeigt den Bildschirm an, Sie müssen auf OK klicken, um zu bestätigen.

   .. image:: img/inverted_screen3.png

3. OLED-Bildschirm-Konfiguration

   Führen Sie im Terminal den folgenden Befehl aus, um das OLED um 180 Grad zu drehen:

   .. code-block:: bash

      sudo pironman5 -or 180

----------------------------------------------------

**Hinweis**

- Stellen Sie nach dem Umdrehen sicher, dass das Gerät auf einer stabilen Oberfläche steht, um ein Umkippen zu verhindern.
- Wenn die Touch-Eingabe nicht mehr korrekt ist, kalibrieren Sie den Touchscreen über die Systemeinstellungen neu.
- Für erweiterte Display-Anpassungen finden Sie im Abschnitt :ref:`promax_view_control_commands` weitere Befehle zu OLED und Bildschirmrotation.