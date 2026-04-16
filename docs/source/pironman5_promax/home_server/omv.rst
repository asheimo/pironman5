.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_omv_5_promax:

Configurazione di OpenMediaVault
=====================================

.. warning::

   OpenMediaVault **non** supporta l'installazione sul desktop di Raspberry Pi OS.

   ⚠️ **Sono supportate solo le versioni Raspberry Pi OS Lite 11 (Bullseye) e 12 (Bookworm).**

   Assicurati di aver installato il sistema operativo corretto e configurato la rete.
   La procedura qui è coerente con :ref:`install_os_sd_rpi_promax`, ma quando selezioni un'immagine, scegli Raspberry Pi OS Lite da Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (abbreviato come OMV) è un sistema operativo open-source per Network Attached Storage (NAS) basato su Debian Linux, progettato per utenti domestici e piccoli uffici, con l'obiettivo di semplificare la gestione dello storage e fornire ricche funzionalità di servizio di rete.

Segui questi passaggi per installare OpenMediaVault sul tuo Raspberry Pi:

1. Connettiti al Tuo Raspberry Pi Usando SSH
-----------------------------------------------------------

   Inserisci il seguente comando nel terminale:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Se stai usando Windows, utilizza PuTTY o un altro client SSH per connetterti al tuo Raspberry Pi.

2. Installa OpenMediaVault
----------------------------

   Inserisci il seguente comando nel terminale:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   Questo scaricherà ed eseguirà lo script di installazione per OpenMediaVault. Non riavviare il tuo Raspberry Pi dopo l'installazione.

3. Accedi a OpenMediaVault
-----------------------------

   Inserisci il seguente URL nel tuo browser per accedere a OpenMediaVault:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Se non riesci ad accedere all'URL sopra, prova a usare l'indirizzo IP, ad esempio, http://192.168.1.100.

   Vedrai una pagina di accesso, accedi usando il nome utente e la password predefiniti. Il nome utente predefinito è ``admin`` e la password è ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Dopo aver effettuato l'accesso, vedrai l'interfaccia principale di OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Ora hai installato e accesso con successo a OpenMediaVault, puoi iniziare a configurare e gestire il tuo storage.

4. Configura RAID (Opzionale)
---------------------------------------

   NVMe RAID è una soluzione di storage che combina più unità a stato solido (SSD) NVMe utilizzando la tecnologia RAID, mirata a massimizzare le prestazioni ad alta velocità del protocollo NVMe e le funzionalità di ridondanza/miglioramento delle prestazioni del RAID. I modi comuni includono RAID 0, 1, 5, 10, ecc. Per due SSD NVMe, RAID 0 e RAID 1 sono i modi più comunemente usati.

   * RAID 0 è una tecnologia di striping che divide i dati in più strisce e distribuisce queste strisce su più hard disk, raggiungendo così velocità di lettura/scrittura più elevate. RAID 0 non fornisce protezione di ridondanza, quindi se uno qualsiasi degli hard disk si guasta, tutti i dati andranno persi.

   * RAID 1 è una tecnologia di mirroring che copia i dati su più hard disk, fornendo così protezione di ridondanza. Le velocità di lettura/scrittura di RAID 1 dipendono dalla velocità di un singolo hard disk, poiché i dati devono essere letti da più hard disk. Se uno qualsiasi degli hard disk si guasta, gli altri possono continuare a fornire dati.

   .. note:: Montare almeno 2 dischi per RAID 0 o RAID 1. In RAID 0, la capacità del volume RAID sarà la somma delle capacità di tutti i dischi. In RAID 1, la capacità del volume RAID sarà la stessa della capacità del disco più piccolo.

   1. Nel menu ``System`` clicca sull'opzione ``Plugins``, cerca il plugin ``openmediavault-md`` e installalo.

   .. image:: img/omv/omv-raid-1.png

   2. Nel menu ``Storage`` clicca sull'opzione ``Disks``, cancella due SSD.

   .. image:: img/omv/omv-raid-2.png

   3. Tieni presente che questa azione cancellerà tutti i dati sugli hard disk, assicurati di aver eseguito il backup di tutti i dati importanti.

   .. image:: img/omv/omv-raid-3.png

   4. La modalità di cancellazione seleziona ``QUICK`` è sufficiente.

   .. image:: img/omv/omv-raid-4.png

   5. Entra nella scheda ``Multiple Device``, clicca su ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. Nell'opzione Level, puoi scegliere Stripe (RAID 0) o Mirror (RAID 1). Nell'opzione Devices, seleziona gli hard disk che hai appena cancellato. Clicca su ``Save`` e attendi il completamento della configurazione RAID.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Se appare un rapporto di errore (500 - Internal Server Error), prova a riavviare il sistema OMV.

   7. Applica la configurazione cliccando sul pulsante ``Apply``.

   .. image:: img/omv/omv-raid-7.png

   8. Dopo il completamento della configurazione RAID, devi attendere che lo stato del RAID sia al ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. Dopo il completamento della configurazione RAID, i tuoi hard disk sono ora in una configurazione RAID 0 o RAID 1 e puoi usarli come un singolo dispositivo di storage.

5. Configura lo Storage
-----------------------

   Nell'interfaccia principale di OpenMediaVault, clicca sull'opzione ``Storage`` nel menu a sinistra. Nella pagina ``Storage``, clicca sulla scheda ``Disks``. Nella pagina ``Disks``, vedrai tutti i dischi sul tuo Raspberry Pi. Assicurati che il tuo NVMe PIP abbia un hard disk collegato.

   .. image:: img/omv/omv-disk.png

   1. Nella barra laterale, clicca sull'opzione ``File System``. Quindi crea e monta un file system. Scegli ``ext4`` come tipo di file system.

   .. image:: img/omv/omv-mount.png

   2. Seleziona Device e salva.

   .. note:: Se hai configurato il RAID, vedrai il dispositivo RAID nell'elenco. Selezionalo e salva.

   .. image:: img/omv/omv-mount-2.png

   3. Apparirà una finestra che ti informa che il file system è in fase di creazione, attendi un momento.

   .. image:: img/omv/omv-mount-3.png

   4. Una volta terminato, entrerai nell'interfaccia ``Mount``, seleziona il file system che hai appena creato e montalo sul tuo Raspberry Pi.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Se stai usando due hard disk (e non RAID), dovresti ripetere i passaggi sopra per montare anche il secondo hard disk sul tuo Raspberry Pi.

   5. Dopo il montaggio, applica le modifiche, e poi puoi vedere i dati sui tuoi hard disk nel file system.

   .. image:: img/omv/omv-mount-5.png

   A questo punto, hai configurato con successo OpenMediaVault e montato i tuoi hard disk. Ora puoi usare OpenMediaVault per gestire il tuo storage.

6. Crea una Cartella Condivisa
---------------------------------------

   1. Nella pagina ``Storage``, vai alla scheda ``Shared Folders``. E clicca sul pulsante ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. Nella pagina ``Create Shared Folder``, inserisci il nome della cartella condivisa, seleziona l'hard disk che vuoi condividere, il percorso della cartella condivisa e imposta i permessi della cartella condivisa. Quindi clicca sul pulsante ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Ora puoi vedere la cartella condivisa che hai appena creato. Conferma che sia corretta, quindi applica.

   .. image:: img/omv/omv-share-3.png

   Ora hai creato con successo una cartella condivisa.

7. Crea un Nuovo Utente
---------------------------------------

   Per accedere alla cartella, dobbiamo creare un nuovo utente, segui questi passaggi:

   1. Nella pagina ``User``, clicca sul pulsante ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. Nella pagina ``Create User``, inserisci il nome utente e la password del nuovo utente, quindi clicca sul pulsante ``Save``.

   .. image:: img/omv/omv-user-2.png

   Ora hai creato con successo un nuovo utente.

8. Imposta i Permessi per il Nuovo Utente
----------------------------------------------------------------------

   1. Nella pagina ``Shared Folders``, clicca sulla cartella condivisa che hai appena creato. Quindi clicca sul pulsante ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. Nella pagina ``Permissions``, imposta i permessi. Quindi clicca sul pulsante ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Dopo aver completato, clicca sul pulsante ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Ora puoi usare questo nuovo utente per accedere alla tua cartella condivisa.

9. Configura il Servizio SMB
---------------------------------------

   1. Nella pagina ``Services``, trova la scheda ``SMB/CIFS`` > ``Setting``. E spunta l'opzione ``Enable``. Quindi clicca sul pulsante ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Applica le modifiche cliccando sul pulsante ``Apply``.

   .. image:: img/omv/omv-smb-2.png

   3. Entra nella pagina ``Shares``, clicca sul pulsante ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. Nella pagina ``Create Share``, seleziona il percorso della cartella condivisa. Quindi clicca sul pulsante ``Save``. Tra l'altro, ci sono molte opzioni in questa pagina che puoi configurare come necessario.

   .. image:: img/omv/omv-smb-4.png

   5. Clicca su ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Ora hai configurato con successo il servizio SMB. Ora puoi usare il protocollo SMB per accedere alla tua cartella condivisa.

10. Accedi alla Cartella Condivisa su Windows
-----------------------------------------------------------------

   1. Apri ``Questo PC``, quindi clicca su ``Connetti unità di rete``.

   .. image:: img/omv/omv-network-location-1.png

   2. Nella finestra di dialogo che appare, inserisci l'IP del Raspberry Pi nel campo ``Cartella``, ad esempio, ``\\192.168.1.100\``, o il nome host del Raspberry Pi, ad esempio, ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Clicca sul pulsante Sfoglia, quindi seleziona la cartella condivisa a cui vuoi accedere. Durante questo processo, dovrai inserire il nome utente e la password che hai creato in precedenza.

   .. image:: img/omv/omv-network-location-3.png

   4. Spunta "Riconnetti all'accesso" e clicca sul pulsante ``Fine``.

   .. image:: img/omv/omv-network-location-4.png

   5. Ora puoi accedere alla cartella condivisa NAS.

   .. image:: img/omv/omv-network-location-5.png

11. Accedi alla Cartella Condivisa su Mac
------------------------------------------------------------------

   1. Nel menu ``Vai``, clicca su ``Connetti al server``.

   .. image:: img/omv/omv-mac-1.png

   2. Nella finestra di dialogo che appare, inserisci l'IP del Raspberry Pi, come ``smb://192.168.1.100``, o il nome host del Raspberry Pi, come ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Clicca sul pulsante ``Connetti``.

   .. image:: img/omv/omv-mac-3.png

   4. Nella finestra di dialogo che appare, inserisci il nome utente e la password che hai creato in precedenza. Clicca sul pulsante ``Connetti``.

   .. image:: img/omv/omv-mac-4.png

   5. Ora puoi accedere alla cartella condivisa NAS.

   .. image:: img/omv/omv-mac-5.png