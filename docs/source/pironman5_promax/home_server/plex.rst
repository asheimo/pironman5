
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configurazione di Plex
=======================================

Plex è una potente piattaforma media server che ti consente di organizzare, riprodurre in streaming e accedere ai tuoi film, programmi TV, musica e foto su più dispositivi. Configurando Plex sulla serie Pironman5 alimentata da Raspberry Pi, puoi creare un home media center economico ed efficiente dal punto di vista energetico che funziona 24/7. Le dimensioni compatte del Raspberry Pi, il basso consumo energetico e la flessibilità lo rendono una scelta eccellente per ospitare Plex, trasformando il tuo Pi in un hub di intrattenimento personale accessibile dalla tua rete domestica o anche da remoto.

**Preparazione**

* Scheda MicroSD (16GB+, consigliata Classe 10)
* Sistema ufficiale Raspberry Pi OS (o Raspberry Pi OS Lite)
* Connessione di rete stabile (consigliato Ethernet cablato)
* Disco rigido esterno o chiavetta USB (per archiviazione espansa)

**Installa Portainer**

Apri il terminale e inserisci i seguenti comandi:

1. Installa Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installa Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Riavvia il tuo Raspberry Pi. (Poi completa i seguenti passaggi **IMMEDIATAMENTE**.)

4. Dopo l'avvio del tuo Raspberry Pi, apri un browser web e visita il tuo indirizzo Portainer: ``https://<ip-del-tuo-rpi>:9443`` .

5. Per impostazione predefinita, potresti vedere un avviso che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un'Autorità di Certificazione (CA) nota. La maggior parte dei browser web mostrerà un tale avviso. In questo caso, puoi tranquillamente ignorarlo, accettare il rischio e procedere.

   .. image:: img/home_server_app/private_save.png

#. Al primo accesso, ti verrà chiesto di impostare una password di amministratore.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Dopo aver creato l'account amministratore, entrerai nell'interfaccia di Portainer. Dalla barra di navigazione a sinistra, vai su **Setting -> General**, trova **App Templates** e inserisci il seguente URL nel campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Clicca su **Save Application Settings**. L'installazione richiederà circa 10 secondi per completarsi.

**Installa Plex**

1. Dalla barra di navigazione a sinistra, clicca su **Home -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Vai su **Templates -> Application**. Nella barra di ricerca in alto a destra, digita *plex* e cliccaci sopra.

   .. image:: img/home_server_app/ptn_temp_plex.png

#. Imposta la modalità di rete su **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. Espandi **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. Nella sezione **volume mapping**, configura i percorsi di archiviazione per i tuoi file multimediali e concedi a Plex i permessi di lettura/scrittura. I percorsi predefiniti sono ``/portainer/TV`` e ``/portainer/Movies``, entrambi con accesso in lettura/scrittura abilitato.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. Clicca su **Deploy** e attendi che Plex completi l'installazione.

**Configura il Server Plex**

1. Apri il tuo browser e inserisci: ``http://<tuo_ip>:32400/web`` . Dovresti ora vedere l'interfaccia di Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Salta l'offerta di abbonamento premium.

3. Successivamente, vedrai la schermata **Server Setup**. Puoi spuntare *Allow me to access my media outside my home*. Per ora, si consiglia di lasciare deselezionata questa opzione e configurarla in seguito se necessario.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Ti verrà quindi chiesto di organizzare i tuoi media. Puoi scegliere *Skip* e aggiungere i media in seguito tramite le impostazioni. Tuttavia, si consiglia di aggiungere direttamente i percorsi di archiviazione che hai configurato nel volume mapping di Portainer, in modo che Plex possa scansionare e importare automaticamente i tuoi media.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Seleziona il tipo della tua libreria multimediale, dai un nome alla tua libreria e scegli la lingua.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Aggiungi le cartelle. Individua i percorsi di archiviazione dei media che hai impostato in precedenza e clicca su **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Clicca su **Finish**. Il tuo server Plex su Raspberry Pi è ora completamente configurato.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Ora dovresti vedere i tuoi file multimediali visualizzati sulla homepage del server Plex.

   .. image:: img/home_server_app/plex_index.png
