.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configurazione di NextCloudPi
=======================================

NextCloud è una soluzione open-source per cloud storage privato, simile a Google Drive o Dropbox. Può essere utilizzato per archiviare file, condividere documenti, sincronizzare foto e gestire calendari e contatti.
A differenza dei servizi cloud pubblici, NextCloud offre agli utenti il controllo completo sui propri dati, rendendolo ideale per individui e piccoli team che danno valore alla privacy e alla sicurezza dei dati.

La serie Pironman5 alimentata da Raspberry Pi offre basso consumo energetico, dimensioni compatte e prestazioni affidabili, che lo rendono una scelta eccellente per un server cloud privato domestico. Combinato con NextCloud, può funzionare come un sistema NAS economicamente vantaggioso.

**Preparazione**

* Scheda MicroSD (16GB+, consigliata Classe 10)
* Sistema ufficiale Raspberry Pi OS (o Raspberry Pi OS Lite)
* Connessione di rete stabile (consigliato Ethernet cablato)
* Disco rigido esterno o chiavetta USB (per archiviazione espansa)

**Installare Portainer**

Apri il terminale e inserisci i seguenti comandi:

1. Installa Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installa Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Riavvia il tuo Raspberry Pi. (Poi completa i seguenti passaggi **IMMEDIATAMENTE**.)

4. Dopo l'avvio del tuo Raspberry Pi, apri un browser web e visita il tuo indirizzo Portainer: ``https://<ip-del-tuo-rpi>:9443`` .

5. Per impostazione predefinita, vedrai un avviso che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un'Autorità di Certificazione (CA) nota. La maggior parte dei browser web mostrerà un avviso su tali certificati. In questo caso, puoi tranquillamente ignorare l'avviso, accettare il rischio e continuare.

   .. image:: img/home_server_app/private_save.png

#. Al primo accesso, dovrai impostare una password di amministrazione.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Dopo aver registrato l'account amministratore, entrerai nell'interfaccia di Portainer. Dalla barra di navigazione a sinistra, clicca su **Setting -> General**, trova **App Templates** e inserisci il seguente URL nel campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Clicca su **Save Application Settings**. L'installazione richiederà circa 10 secondi per completarsi.

**Installare NextCloud**

1. Dalla barra di navigazione a sinistra, clicca su **Home -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. Vai su **Templates -> Application**. Nella barra di ricerca in alto a destra, digita *nextcloud* e cliccaci sopra.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Clicca su **Deploy the stack** e attendi il completamento del deployment. Di solito richiede circa due minuti.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Una volta completato, NextCloud sarà installato.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**Utilizzare NextCloud**

1. Apri il tuo browser e visita il tuo indirizzo NextCloud: ``https://<ip-del-tuo-rpi>:32768`` .

.. note::

   Analogamente, vedrai un avviso che il sito utilizza un certificato SSL/TLS autofirmato non emesso da un'Autorità di Certificazione (CA) nota. La maggior parte dei browser web mostrerà un avviso su tali certificati.
   In questo caso, puoi tranquillamente ignorare l'avviso, accettare il rischio e continuare.

   .. image:: img/home_server_app/private_save.png

2. Al primo accesso, dovrai impostare una password di amministrazione.

   .. image:: img/home_server_app/nc_admin_install.png

3. Dopo la registrazione, puoi iniziare a utilizzare NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png