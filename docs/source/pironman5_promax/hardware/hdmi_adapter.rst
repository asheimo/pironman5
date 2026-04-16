
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Adattatore USB HDMI
==========================================

.. image:: img/hdmi_adapter.png

Questa scheda adattatore USB HDMI è progettata specificamente per il Raspberry Pi 5. La sua funzione principale è quella di riposizionare le connessioni USB e HDMI per allinearle con il lato dell'interfaccia USB del Raspberry Pi, migliorando l'accessibilità e la gestione dei cavi.

Inoltre, la porta HDMI viene convertita in un'interfaccia HDMI Type A standard, offrendo una compatibilità più ampia.

**Alimentazione Aggiuntiva per NVMe**

La scheda presenta un header di alimentazione 5V specificamente per l'alimentazione NVMe PIP. Insieme a un header di estensione, può essere collegato all'interfaccia di alimentazione aggiuntiva dell'NVMe per fornire potenza extra.

**Porta Batteria 1220RTC**

È incorporato un supporto per batteria 1220RTC per una comoda installazione di una batteria RTC. Si collega all'interfaccia RTC del Raspberry Pi tramite un cavo reverse SH1.0 2P.

Il supporto batteria è compatibile sia con batterie CR1220 che ML1220. Se si utilizza una ML1220 (batteria al biossido di manganese e litio), la ricarica può essere configurata direttamente sul Raspberry Pi. Nota che la CR1220 non è ricaricabile.

**Abilitazione della Ricarica a Goccia**

.. warning::

  Se stai utilizzando una batteria CR1220, non abilitare la ricarica a goccia poiché può causare danni irreparabili alla batteria e rischiare di danneggiare la scheda.

Per impostazione predefinita, la funzione di ricarica a goccia per la batteria è disabilitata. I file ``sysfs`` indicano la tensione e i limiti di ricarica a goccia correnti:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Per abilitare la ricarica a goccia, aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``:

  * Apri ``/boot/firmware/config.txt``.

    .. code-block:: shell

      sudo nano /boot/firmware/config.txt

  * Aggiungi ``rtc_bbat_vchg`` a ``/boot/firmware/config.txt``.

    .. code-block:: shell

      dtparam=rtc_bbat_vchg=3000000

Dopo il riavvio, il sistema visualizzerà:

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_promax
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Questo conferma che la batteria è ora in ricarica a goccia. Per disabilitare questa funzione, rimuovi semplicemente la riga ``dtparam`` da ``config.txt``.

**Interfaccia Audio**
---------------------------------

Questa sezione copre le funzionalità di uscita audio della scheda, inclusa l'uscita degli altoparlanti e il jack per cuffie.

.. image:: img/hdmi_speaker_port.png

**Porta Altoparlante**

La scheda presenta un'interfaccia di uscita altoparlanti a due canali che supporta due altoparlanti da 4Ω 3W.

**Interruttore Altoparlante**

Il segnale audio dell'altoparlante proviene dalla sorgente HDMI0. Se HDMI0 è collegato a un display con altoparlanti integrati, sia gli altoparlanti del Pironman 5 Pro Max che quelli del display potrebbero riprodurre l'audio simultaneamente. Il ponticello **SPEAKER** ti permette di controllare questo comportamento.

*   Collega il ponticello ai due pin di sinistra (**ON**) per mantenere gli altoparlanti **sempre abilitati**.
*   Collega il ponticello ai due pin di destra (**AUTO**) per far **disabilitare automaticamente** gli altoparlanti quando vengono inserite le cuffie o quando HDMI0 è collegato.

Pertanto, se desideri utilizzare gli altoparlanti integrati mentre un display HDMI è collegato, puoi:

*   Collegare il display alla porta **HDMI1** invece.
*   Impostare il ponticello **SPEAKER** sulla posizione **ON**.

**Jack Audio 3.5mm**

Il jack per cuffie condivide la stessa sorgente audio degli altoparlanti ma trasporta un segnale **non amplificato**. Utilizza un jack commutato che **disabilita automaticamente l'amplificatore degli altoparlanti** quando vengono inserite le cuffie, impedendo a entrambi di riprodurre il suono simultaneamente.

Il jack è un connettore TRRS a 4 pin ma supporta **solo uscita audio stereo standard**:

*   **Punta (T):** Canale Sinistro
*   **Anello 1 (R1):** Canale Destro
*   **Anello 2 (R2):** Terra
*   **Manicotto (S):** Terra

Questa configurazione mantiene la compatibilità con la maggior parte degli standard comuni per cuffie a 4 pin.
