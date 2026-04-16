.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Installazione di Umbrel OS
============================================

Umbrel è una piattaforma/sistema operativo open-source e self-hosted per home server che ti consente di eseguire il tuo nodo Bitcoin, installare una varietà di app self-hosted con un clic — e trasformare il tuo hardware nel tuo cloud personale. È un modo eccellente per iniziare con il self-custody e la privacy.

**Componenti Richiesti**

* Un Personal Computer
* Un SSD NVMe
* Un Adattatore NVMe-USB
* Scheda Micro SD e Lettore

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installare il Sistema Operativo sull'SSD NVMe
-----------------------------------------------------------------------------

Ora sei pronto per installare il sistema operativo sul tuo **SSD NVMe**.
Segui attentamente i passaggi qui sotto — questa guida è scritta per principianti ed è facile da seguire.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Versioni di Umbrel OS</a>

#. Scarica l'ultima immagine di **Umbrel OS** ed estrai il file. Se vuoi usare una versione specifica, puoi anche visitare la pagina |link_umbrel_release|.

   * :download:`Ultima Immagine di Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Inserisci l'**SSD NVMe** nel tuo computer usando un **adattatore NVMe-USB**.

#. Apri **Raspberry Pi Imager**. Nella schermata **Device**, seleziona il tuo modello **Raspberry Pi 5** dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

#. Vai alla sezione **OS**, scorri verso il basso e seleziona **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Seleziona il **file immagine di Umbrel OS** che hai scaricato ed estratto in precedenza, quindi clicca su **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Clicca su **Next** per continuare.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. Nella sezione **Storage**, seleziona il tuo **SSD NVMe**. Assicurati di scegliere l'SSD NVMe e non un'altra unità del tuo computer.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Rivedi attentamente tutte le impostazioni, quindi clicca su **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Se l'SSD NVMe contiene già dati, Raspberry Pi Imager ti avviserà che tutti i dati verranno cancellati. Ricontrolla che sia selezionata l'unità corretta, quindi clicca su **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Quando appare il messaggio **“Write Complete”**, l'immagine è stata scritta e verificata con successo.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%