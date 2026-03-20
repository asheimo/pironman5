.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _intro_pironman5_promax:

Pironman 5 Pro MAX
================================================================================


Vielen Dank, dass Sie sich für unseren |link_pironman5_promax| entschieden haben.

.. image:: img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Werten Sie Ihr Raspberry Pi 5-Erlebnis mit dem |link_pironman5_promax| auf, unserem neuen Flaggschiff-Hochleistungsgehäuse aus Aluminium. Entwickelt für ultimative Kühlung, Erweiterung und ein vollständiges Desktop-ähnliches Erlebnis, ist es perfekt für anspruchsvolle Anwendungen wie NAS, KI-Entwicklung, Medienzentren und fortgeschrittene Projekte.

**Hauptmerkmale**:

* **Dual-NVMe- & KI-Erweiterungs-Hub**: Integrierter PCIe-Gen-2-Switch mit zwei M.2-M-Key-Steckplätzen (2230/2242/2260/2280) für SSDs oder KI-Beschleuniger (voll kompatibel mit Hailo-8/8L). Konfigurierbar für RAID-0/1-NAS, SSD+KI oder duale KI-Setups.
* **Umfassendes Kühlsystem**: Massiver Tower-Kühler mit einem PWM-Lüfter, plus **drei** adressierbare RGB-PWM-Lüfter, die auch unter Volllast eine ausgezeichnete thermische Leistung gewährleisten.
* **Dual-Display & Multimedia**:

    * **4,3-Zoll-DSI-Touchscreen** (800x480): Nutzbar als sekundäres Info-Display, Status-Dashboard oder sogar als primärer Desktop-Monitor.
    * **0,96-Zoll-Smart-OLED-Display**: Zeigt in Echtzeit CPU, Arbeitsspeicher, Temperatur, Speicherbelegung und IP an. Verfügt über eine Aufweckfunktion per Tippen durch einen integrierten Vibrationssensor.
    * **Stereo-3W-Lautsprecher & 5MP-Kamera**: Bereit für Multimedia, Videokonferenzen oder Computer-Vision-Projekte.

* **Verbesserte Benutzeroberfläche & Steuerung**:

    * **Anpassbares RGB-Ökosystem**: Sechs WS2812B adressierbare LEDs und drei synchronisierte RGB-Lüfter für dynamische Lichteffekte.
    * **IR-Empfänger** für die Fernbedienung von Medienzentren (z.B. Kodi, Volumio).
    * **Sicherer Retro-Metall-Netzschalter** für ordnungsgemäßes Herunterfahren und Einschalten.
    * **RTC-Batteriefach** (für CR1220) zur Zeiterhaltung.

* **Professionelle Konnektivität & Layout**:

    * **Neuorganisation der Rückseite**: Stromeingang und zwei Standard-HDMI-Anschlüsse wurden versetzt, um mit den USB-Anschlüssen für ein sauberes, einheitliches Kabelmanagement-Layout zu fluchten.
    * **Voller Zugriff auf Anschlüsse**: Dual-HDMI, Gigabit-LAN, 2x USB 3.0, 2x USB 2.0.
    * **Beschrifteter externer GPIO-Erweiterer** für einfachen Anschluss von Zubehör.

* **Hochwertiges Industriedesign**: Robustes Gehäuse aus dunkel eloxierter Aluminiumlegierung mit dunklen Acryl-Seitenteilen, federbelastetem microSD-Kartensteckplatz und einer modernen, von Desktop-PCs inspirierten Ästhetik.

.. note::

  Es wird dringend empfohlen, das offizielle 27W-Netzteil für Raspberry Pi oder eine kompatible hochwertige Alternative wie das |link_sf_27w_supply| für den Pironman 5 Pro Max zu verwenden. Eine unzureichende Stromversorgung kann zu Instabilität oder Neustarts des Raspberry Pi 5 führen, insbesondere unter hoher Last mit NVMe-Laufwerken und Zubehör.

-------------------------------------------------------------------------------------


**Inhalt**

.. raw:: html

   <br/>

.. toctree::
    :maxdepth: 1

    About this Kit <self>
    what_do_we_need
    assembly_instructions
    install/install_the_os
    set_up/set_up_pironman5
    control/control_pironman5
    hardware/hardware
    optional_modules/optional_modules
    home_server/home_server
    ai_interaction/ai_interaction
    compitable_nvme_ssd
    faq

-------------------------------------------------------------------------------------

**Technische Daten**

* **Abmessungen**: 140,9 x 77,0 x 138,7 mm
* **Material**:

    * Hauptgehäuse: Dunkel eloxierte Aluminiumlegierung
    * Seitenwände: Dunkles Acryl

* **Unterstützte Plattform**: Nur Raspberry Pi 5
* **Stromversorgung**: USB Typ-C, 5V/5A (Mindestens 27W empfohlen)
* **Schnittstellen & Anschlüsse**:

    * **Raspberry Pi 40-polige GPIO** (extern herausgeführt mit klaren Beschriftungen)
    * **MicroSD-Kartensteckplatz** (mit federbelastetem Auswurfmechanismus)
    * **Rückseite**:

        * USB Typ-C Stromeingang
        * 2 x USB 2.0
        * 2 x USB 3.0
        * Gigabit Ethernet (RJ45)
        * 2 x Standard-HDMI-Anschlüsse (Typ A) (4Kp60 Unterstützung)

* **Kühlsystem**:

    * 1 x Großer Tower-Kühler mit PWM-gesteuertem Lüfter
    * 3 x adressierbare RGB-PWM-Lüfter (GPIO-gesteuert, synchronisierbar)

* **Display & Multimedia**:

    * 4,3-Zoll-DSI-Kapazitiv-Touchscreen (800 x 480 Pixel)
    * 0,96-Zoll-OLED-Display (128x64) für Systemstatistiken
    * Vibrationssensor zum Aufwecken des OLEDs per Tippen
    * Stereo-3W-Lautsprecher
    * Unterstützung für 5-Megapixel-Kameramodul

* **Speicher & Erweiterung**:

    * Integrierter PCIe Gen 2 Switch
    * 2 x PCIe 2.0 x1 M.2 M-Key Steckplätze
    * Unterstützte SSD/AI-Kartengrößen: 2230, 2242, 2260, 2280

* **Bedienelemente, Beleuchtung & Besonderheiten**:

    * 6 x WS2812B adressierbare RGB-LEDs
    * IR-Empfänger (38kHz)
    * Metallischer Netzschalter (sichere Abschaltfunktion)
    * Echtzeituhr (RTC)-Batteriehalter (für CR1220-Zelle)

* **Verarbeitungsqualität**: Präzisionsgefrästes CNC-Aluminiumgehäuse mit getönten Acrylfenstern, ausgelegt für Langlebigkeit und anspruchsvolle Ästhetik.