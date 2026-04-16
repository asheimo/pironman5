.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Installazione del Sistema Operativo Batocera
=============================================

Segui il tutorial qui sotto per installare il sistema sulla tua scheda Micro SD.

**Componenti Richiesti**

* Un Personal Computer
* Una scheda Micro SD e un Lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il Sistema Operativo sulla scheda microSD
------------------------------------------------------------------------------------------

.. |shared_link_batocera_linux| raw:: html

    <a href="https://updates.batocera.org/bcm2712/stable/last/batocera-bcm2712-42-20251007.img.gz" target="_blank">Batocera.Linux</a>

1. Scarica l'ultima versione del sistema operativo dal sito web |shared_link_batocera_linux|.

2. Inserisci la tua scheda microSD nel tuo computer usando un lettore di schede.
   Prima di procedere, esegui il backup di tutti i dati importanti sulla scheda, poiché verranno cancellati.

   .. image:: img/insert_sd.png
      :width: 90%

3. Quando **Raspberry Pi Imager** si apre, vedrai la pagina **Device**.
   Seleziona il tuo modello **Raspberry Pi 5** dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

4. Vai alla sezione **OS**, scorri verso il basso fino alla fine della pagina e seleziona **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

5. Scegli il file **batocera-bcmxxxxxxx.img.gz** che hai appena scaricato e clicca su **Open**.

   .. image:: img/imager_choose_batocera.png
      :width: 90%

6. Nella sezione **Storage**, seleziona la tua scheda microSD.
   Per sicurezza, si consiglia di scollegare altri dispositivi di archiviazione USB in modo che solo la scheda microSD appaia nell'elenco.

   .. image:: img/imager_storage.png
      :width: 90%

#. Clicca su **NEXT** e vai direttamente a **Writing**, dove il sistema operativo viene scritto sulla scheda microSD.

   .. image:: img/imager_betocera_write.png
      :width: 90%

#. Quando appare il messaggio **"Write Successful"**, l'immagine è stata completamente scritta e verificata. Ora puoi rimuovere in sicurezza la scheda microSD e usarla per avviare il tuo Raspberry Pi.

   .. image:: img/imager_betocera_finish.png
      :width: 90%