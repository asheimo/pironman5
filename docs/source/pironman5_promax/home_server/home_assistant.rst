.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configurazione di Home Assistant
======================================

Home Assistant è una piattaforma di automazione domestica che funziona su un hub centrale (Raspberry Pi, PC, ecc.). Può essere utilizzato per controllare e monitorare tutti i tipi di dispositivi, dalle luci e termostati alle telecamere di sicurezza e agli elettrodomestici intelligenti.

**Preparazione**

Prima di iniziare, assicurati di avere quanto segue:

* Un Raspberry Pi in grado di eseguire Home Assistant.
* Una connessione Internet stabile.
* Un account su Home Assistant Cloud (opzionale, ma consigliato per l'accesso remoto).

**Installazione**

Apri il terminale e inserisci i seguenti comandi:

1. Installa Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installa Home Assistant

.. code-block:: bash

   sudo docker pull homeassistant/home-assistant

**Esecuzione del Container Home Assistant**

Qui, utilizziamo Docker Compose per eseguire Home Assistant. Puoi pensare a Docker Compose come a uno "script di automazione". Scriverà tutte le configurazioni (come nome dell'immagine, porte, montaggi dei volumi, variabili d'ambiente, ecc.) in un file ``docker-compose.yml``. Successivamente, con un semplice comando ``docker compose up -d``, Docker creerà e avvierà automaticamente tutti i container configurati secondo questo "script".

1. **Entra nella directory del progetto**: Vai in quella cartella.

   .. code-block:: bash

      cd ~/homeassistant

2. **Crea il file di configurazione**: Nella directory ``~/homeassistant``, crea un file chiamato ``docker-compose.yml`` e copia la configurazione sopra riportata al suo interno.

   .. code-block:: bash

      sudo nano docker-compose.yml

3. Incolla il seguente contenuto nel file ``docker-compose.yml``:

   .. note:: Sostituisci ``- TZ=Asia/Shanghai`` con il tuo fuso orario.

   .. code-block:: bash

      version: '3'
      services:
      homeassistant:
         image: ghcr.io/home-assistant/raspberrypi5-64-homeassistant:stable
         container_name: homeassistant
         restart: unless-stopped
         privileged: true
         network_mode: host
         environment:
            - TZ=Asia/Shanghai
         volumes:
            - ./config:/config

4. ``Ctrl+X`` per uscire dall'editor, quindi premi ``Y`` per salvare le modifiche.

5. **Avvia Home Assistant**: Nella directory ``~/homeassistant``, esegui il seguente comando. Docker Compose scaricherà automaticamente l'immagine e avvierà il container.

   .. code-block:: bash

      sudo docker compose up -d

   * ``up``: Crea e avvia i servizi.
   * ``-d``: Esegue in background (modalità distaccata).

6. **Controlla lo stato di esecuzione**:

    .. code-block:: bash

      docker compose ps

   Dovresti vedere lo stato di ``homeassistant`` come ``Up``.

7. **Visualizza i log** (se ci sono problemi di avvio):

   .. code-block:: bash

      docker compose logs -f

8. Per ulteriori comandi, controlla:

   .. code-block:: bash

      docker compose --help

**Configurazione**

Ora puoi aprire il browser del tuo computer e inserire: ``http://<Indirizzo del tuo Raspberry Pi>:8123`` per accedere a Home Assistant.

.. image:: img/home_assistant/ha_welcome.png

Seleziona **CREATE MY SMART HOME**, quindi crea il tuo account.

.. image:: img/home_assistant/ha_onboarding.png

Segui le istruzioni per scegliere la tua posizione e altre configurazioni. Una volta completato, accederai alla dashboard di Home Assistant.

.. image:: img/home_assistant/ha_overview.png