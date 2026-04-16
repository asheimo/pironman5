.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_set_up_batocera:

Configurazione su Batocera.linux
=========================================================

Se hai installato il sistema operativo Batocera.linux, puoi accedere da remoto a questo sistema tramite SSH e quindi seguire i passaggi seguenti per completare la configurazione.

#. Una volta che il sistema si è avviato, usa ssh per connetterti da remoto a Pironman5. Per Windows, puoi aprire **Powershell**, e per Mac OS X e Linux, puoi aprire direttamente **Terminale**.

   .. image:: img/batocera_powershell.png
      :width: 90%

#. Il nome host predefinito per il sistema batocera è ``batocera``, con nome utente predefinito ``root`` e password ``linux``. Pertanto, puoi accedere digitando ``ssh root@batocera.local`` e inserendo la password ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Esegui il comando: ``/etc/init.d/S92switch setup`` per entrare nella pagina delle impostazioni del menu.

   .. image:: img/batocera_configure.png
      :width: 90%

#. Usa il tasto freccia giù per navigare fino alla fine, seleziona e attiva i servizi **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Dopo aver attivato il servizio pironman5, seleziona **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Esegui il comando ``reboot`` per riavviare Pironman5.

   .. code-block:: shell

      reboot

#. Al riavvio, il ``pironman5.service`` si avvierà automaticamente. Ecco le configurazioni principali per Pironman 5 Pro MAX:

   * Lo schermo OLED visualizza CPU, RAM, utilizzo del disco, temperatura della CPU e l'indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si accenderanno in blu con modalità respiro.

Ora puoi collegare Pironman 5 Pro MAX a uno schermo, controller di gioco, cuffie e altro ancora per immergerti nel tuo mondo di gioco.

.. note::

   A questo punto, hai configurato con successo Pironman 5 Pro MAX ed è pronto per l'uso.

   Per il controllo avanzato dei suoi componenti, fare riferimento a :ref:`control_commands_dashboard_promax`.