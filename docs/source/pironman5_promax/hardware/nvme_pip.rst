
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Dual NVMe PIP
=====================

Il **Dual NVMe PIP** (PCIe Peripheral Board), come definito dalla Raspberry Pi Foundation, è un adattatore PCIe progettato specificamente per unità a stato solido NVMe.

L'interfaccia PCIe del Raspberry Pi 5 offre nativamente una singola corsia **Gen2 x1** (500 MB/s). Integrando il chip switch PCIe **ASM1182e**, il Dual NVMe PIP espande questa in **due corsie Gen2 x1 indipendenti**, permettendoti di collegare:

* **Due SSD NVMe M.2**, oppure
* **Un SSD NVMe M.2 + un acceleratore AI M.2 Hailo-8/8L**

**Note Chiave**:

* Gen3 non è supportato
* Supporta dimensioni SSD NVMe: **2230**, **2242**, **2260**, **2280** (tutti negli slot M.2 M-key)

.. image:: img/nvme_pip.png

* La scheda si collega tramite un cavo FFC (Flexible Flat Cable) reverse 16P 0.5mm o un cavo FPC (Flexible Printed Circuit) con impedenza personalizzata.
* **STA**: Un indicatore LED di Stato.
* **PWR**: Un indicatore LED di Alimentazione.
* L'alimentatore onboard da 3.3V può supportare fino a 3A di uscita. Tuttavia, poiché l'interfaccia PCIe del Raspberry Pi è limitata a fornire 5V/1A in uscita (equivalenti a 5W), l'alimentazione aggiuntiva per l'uso a 3.3V/3A può essere fornita attraverso il connettore J3 da una sorgente 5V.
* **FORCE ENABLE**: L'alimentatore onboard viene attivato dal segnale di switch dell'interfaccia PCIe. Dopo che il Raspberry Pi è acceso, invia un segnale per accendere l'alimentazione 3.3V. Se alcuni sistemi non supportano il segnale di switch o per altri motivi, puoi cortocircuitare J4 FORCE ENABLE saldando un filo tra i due pad volanti per forzare l'alimentatore 3.3V onboard ad alimentare l'NVMe.

Informazioni sul Modello
---------------------------

Gli SSD M.2, noti per le loro dimensioni compatte, esistono in vari tipi principalmente differenziati dal loro keying (design dell'intaglio sul connettore) e dall'interfaccia che utilizzano. Ecco i tipi principali:

* **SSD M.2 SATA**: Questi utilizzano l'interfaccia SATA, simile agli SSD SATA da 2.5 pollici ma nel fattore di forma M.2 più piccolo. Sono limitati dalle velocità massime SATA III di circa 600 MB/s. Questi SSD sono compatibili con slot M.2 keyati per chiavi B e M.
* **SSD M.2 NVMe**: Questi SSD utilizzano il protocollo NVMe sulle corsie PCIe e sono significativamente più veloci degli SSD M.2 SATA. Sono adatti per applicazioni che richiedono elevate velocità di lettura/scrittura come gaming, editing video e attività intensive di dati. Questi SSD richiedono tipicamente slot M-key. Queste unità utilizzano l'interfaccia PCIe (Peripheral Component Interconnect Express), con diverse versioni come 3.0, 4.0 e 5.0. Ogni nuova versione di PCIe raddoppia effettivamente la velocità di trasferimento dati del suo predecessore. Tuttavia, il Raspberry Pi 5 utilizza un'interfaccia PCIe 3.0, capace di fornire velocità di trasferimento fino a 3500 MB/s.

Gli SSD M.2 esistono in tre tipi di key: B key, M key e B+M key. Tuttavia, successivamente è stata introdotta la chiave B+M, che combina le funzionalità della chiave B e della chiave M. Di conseguenza, ha sostituito la chiave B standalone. Fare riferimento all'immagine qui sotto.

.. image:: img/ssd_key.png

In generale, gli SSD M.2 SATA sono B+M-key (possono adattarsi a socket per moduli B-key e M-key), mentre gli SSD M.2 NVMe per corsia PCIe 3.0 x4 sono M-key.

.. image:: img/ssd_model2.png

Informazioni sulla Lunghezza
----------------------------------------------

I moduli M.2 esistono in diverse dimensioni e possono anche essere utilizzati per Wi-Fi, WWAN, Bluetooth, GPS e NFC.

Il Pironman 5 MAX supporta quattro dimensioni di SSD NVMe M.2 (PCIe Gen 2.0) in base ai loro nomi: 2230, 2242, 2260 e 2280. Il "22" è la larghezza in millimetri (mm), e i due numeri successivi sono la lunghezza. Più lungo è il drive, più chip di memoria NAND flash possono essere montati; quindi, maggiore è la capacità.

.. image:: img/m2_ssd_size.png
  :width: 600

Alimentazione
-----------------------

L'alimentatore duale onboard da 3.3V supporta un'uscita massima di 3A (10W). Entrambi i rail di alimentazione operano indipendentemente senza interferenze.

**FORCE ENABLE**  
L'alimentatore onboard viene attivato dal segnale di switch dell'interfaccia PCIe. Dopo l'avvio del Raspberry Pi, il segnale accende l'alimentazione 3.3V. Se il sistema non supporta il segnale di switch o per altri motivi, cortocircuita il ponticello J4 FORCE EN per forzare l'alimentazione 3.3V onboard per l'NVMe.

**LED**  
Ogni interfaccia ha indicatori di stato dell'alimentazione (PWR) e indicatori di stato (STA) indipendenti.

Convertitore Interruttore di Alimentazione
------------------------------------------------------------

**Aggiunta del Pulsante di Alimentazione**

* Il Raspberry Pi 5 presenta un ponticello **J2**, situato tra il connettore della batteria RTC e il bordo della scheda. Questa breakout consente l'aggiunta di un pulsante di alimentazione personalizzato al Raspberry Pi 5 collegando un interruttore momentaneo Normally Open (NO) attraverso i due pad. Azionare brevemente questo interruttore imita la funzionalità del pulsante di alimentazione onboard.

   .. image:: img/pi5_j2.jpg

* Sul Pironman 5, c'è un **Power Switch Converter** che estende il ponticello **J2** a un pulsante di alimentazione esterno utilizzando due pin Pogo.

   .. image:: img/psc.png

* Ora, il Raspberry Pi 5 può essere acceso e spento utilizzando il Pulsante di Alimentazione.

**Ciclo di Alimentazione**

All'accensione iniziale del tuo Raspberry Pi 5, si accenderà automaticamente e si avvierà nel sistema operativo senza bisogno di premere il pulsante.

Se si esegue il desktop di Raspberry Pi, una breve pressione del pulsante di alimentazione avvia un processo di spegnimento pulito. Apparirà un menu che offre opzioni per spegnere, riavviare o uscire. Selezionare un'opzione o premere di nuovo il pulsante di alimentazione avvierà uno spegnimento pulito.

.. image:: img/button_shutdown.png

**Spegnimento**

    * Se esegui il sistema **Raspberry Pi OS Desktop**, puoi premere il pulsante di alimentazione due volte rapidamente per spegnere.
    * Se esegui il sistema **Raspberry Pi OS Lite** senza desktop, premi il pulsante di alimentazione una volta per avviare lo spegnimento.
    * Per forzare uno spegnimento brusco, tieni premuto il pulsante di alimentazione.

**Accensione**

    * Se la scheda Raspberry Pi è spenta, ma ancora alimentata, premi una volta per accendere da uno stato di spegnimento.

.. note::

    Se stai eseguendo un sistema che non supporta un pulsante di spegnimento, puoi tenerlo premuto per 5 secondi per forzare uno spegnimento brusco, e premerlo una volta per accendere da uno stato di spegnimento.
