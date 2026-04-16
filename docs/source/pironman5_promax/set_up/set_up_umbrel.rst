
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _set_up_umbrel_promax:

Configurazione su Umbrel OS
======================================================================

Se hai installato Umbrel OS sul tuo Raspberry Pi 5, dovrai configurare Pironman 5 Pro MAX utilizzando la riga di comando. Le istruzioni dettagliate sono fornite di seguito:

#. Collega il tuo Raspberry Pi 5 alla tua rete utilizzando un cavo Ethernet. Questo passaggio è essenziale per garantire che il tuo Raspberry Pi abbia accesso a Internet.

#. Nel tuo browser, visita: ``http://umbrel.local``. Se la pagina non si apre, controlla il tuo router per l'indirizzo IP del dispositivo Umbrel, ad esempio: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Crea il tuo account Umbrel impostando un nome utente e una password. Questa password verrà utilizzata per l'accesso remoto futuro a Umbrel, quindi assicurati di ricordarla.

   .. image:: img/umbrel_account.png

#. Clicca su **Next** per completare la configurazione di Umbrel e accedere all'ambiente desktop.

   .. image:: img/umbrel_desktop.png

#. Apri il Terminale. Dal desktop, clicca sull'icona **Settings**, quindi seleziona **Advanced Settings** e clicca su **Open**.

   .. image:: img/umbrel_setting.png

#. Clicca su **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Puoi scegliere di aprire il Terminale in Umbrel OS o all'interno di un'app specifica. Entrambe le opzioni ti porteranno all'interfaccia del Terminale.

   .. image:: img/umbrel_terminal.png

#. Procedi a scaricare il codice da GitHub e installare il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b pro-max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Dopo il completamento dell'installazione, inserisci il seguente comando per riavviare il tuo Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Al riavvio, il ``pironman5.service`` si avvierà automaticamente. Ecco le configurazioni principali per Pironman 5 Pro MAX:

   * Lo schermo OLED visualizza CPU, RAM, utilizzo del disco, temperatura della CPU e l'indirizzo IP del Raspberry Pi.
   * Quattro LED RGB WS2812 si accenderanno in blu con modalità respiro.

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` di ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``: Usa questo comando per applicare eventuali modifiche apportate alle impostazioni di Pironman 5 Pro MAX.
   * ``start/stop``: Abilita o disabilita il ``pironman5.service``.
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` usando lo strumento ``systemctl``.

.. note::

   A questo punto, hai configurato con successo Pironman 5 Pro MAX ed è pronto per l'uso.

   Per il controllo avanzato dei suoi componenti, fare riferimento a :ref:`control_commands_dashboard_promax`.
