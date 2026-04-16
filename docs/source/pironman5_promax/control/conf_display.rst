
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configurazione del Display
===================================================================

Questo capitolo ti guida attraverso la configurazione delle impostazioni del display per il Pironman 5 Pro MAX, includendo l'abilitazione dello spegnimento automatico dello schermo per il risparmio energetico e la configurazione del capovolgimento dello schermo per adattarsi a orientamenti di installazione speciali.

-------------------------------------------------------------------

**Impostazione della Sospensione dello Schermo in Idle**


Per risparmiare energia quando non stai utilizzando attivamente il Pironman 5 Pro MAX, puoi abilitare la funzione di sospensione automatica dello schermo. Quando il dispositivo è rimasto inattivo per un periodo impostato, il display principale si spegnerà automaticamente, entrando in uno stato a basso consumo.

Segui questi passaggi per configurarlo:

1. Clicca su **Menu -> Preferenze** nell'angolo in basso a sinistra dello schermo, quindi trova e apri il **Pannello di Controllo**.

   .. image:: img/sleep_screen1.png

2. Nell'interfaccia del Pannello di Controllo, clicca per accedere alle impostazioni **Display**.

3. Trova l'opzione **Screen Blanking** e attivala.

   .. image:: img/sleep_screen2.png

----------------------------------------------------------------------

**Capovolgere il Pironman 5 Pro MAX**

Il Pironman 5 Pro MAX può essere capovolto per l'uso. In questa configurazione, lo schermo touchscreen sarà posizionato nella parte superiore e le porte GPIO nella parte inferiore, offrendo maggiore flessibilità per vari progetti. Questa configurazione è ideale per applicazioni come una visualizzazione dello schermo più comoda o un accesso più facile ai pin GPIO durante il collegamento di sensori.

Quando si capovolge il dispositivo, entrambi i display necessitano di regolazioni separate:

   * Touchscreen principale – Richiede impostazioni di rotazione a livello di sistema operativo
   * Schermo OLED di stato – Richiede configurazione tramite riga di comando

Per capovolgere il Pironman 5 Pro MAX, segui questi passaggi:

1. Preparazione Fisica

   Rimuovi la fotocamera dal Pironman 5 Pro MAX, capovolgi l'intera unità e reinstalla la fotocamera. L'installazione dovrebbe essere simmetrica rispetto al suo orientamento originale.

   .. image:: img/inverted_screen0.png

2. Configurazione dell'Orientamento del Touchscreen

   Accendi il dispositivo. Sul touchscreen, premi a lungo sul desktop per aprire il menu e seleziona **Preferenze del Desktop**.

   .. image:: img/inverted_screen1.png

   Scorri verso il basso per trovare l'opzione **Schermi**, quindi premi a lungo l'indicatore dello schermo nel display. Seleziona **Orientamento → Invertito**.

   .. image:: img/inverted_screen2.png

   Applica, la finestra di aggiornamento mostrerà lo schermo, è necessario cliccare su OK per confermare.

   .. image:: img/inverted_screen3.png

3. Configurazione dello Schermo OLED

   Nel Terminale, esegui il seguente comando per ruotare l'OLED di 180 gradi:

   .. code-block:: bash

      sudo pironman5 -or 180

----------------------------------------------------

**Nota**

- Dopo il capovolgimento, assicurati che l'unità sia posizionata su una superficie stabile per evitare ribaltamenti.
- Se incontri un disallineamento dell'input tattile, ricalibra il touchscreen attraverso le impostazioni di sistema.
- Per regolazioni avanzate del display, fai riferimento alla sezione :ref:`promax_view_control_commands` per comandi aggiuntivi relativi a OLED e rotazione dello schermo.
