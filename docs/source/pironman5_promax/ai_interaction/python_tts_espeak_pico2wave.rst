
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

1. TTS con Espeak e Pico2Wave
=================================================

In questa lezione, useremo due motori di sintesi vocale (TTS) integrati su Raspberry Pi — **Espeak** e **Pico2Wave** — per far parlare il Pironman 5 Pro MAX.

Questi due motori sono entrambi semplici e funzionano offline, ma hanno un suono molto diverso:

* **Espeak**: molto leggero e veloce, ma la voce è robotica. Puoi regolare velocità, tono e volume.
* **Pico2Wave**: produce una voce più fluida e naturale rispetto a Espeak, ma ha meno opzioni configurabili.

Sentirai la differenza nella **qualità della voce** e nelle **funzionalità**.

----

1. Testare Espeak
--------------------

Espeak è un motore TTS leggero incluso in Raspberry Pi OS.
La sua voce suona robotica, ma è altamente configurabile: puoi regolare volume, tono, velocità e altro.

**Eseguire il programma**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_espeak.py

  * Dovresti sentire il Pironman 5 Pro MAX dire: "Hello! I'm Espeak TTS."
  * Prova a modificare i parametri di tuning nel codice per sperimentare come ``amp``, ``speed``, ``gap`` e ``pitch`` influenzano il suono.

**Codice**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Espeak

  # Crea un'istanza TTS Espeak
  tts = Espeak()
  # Imposta l'ampiezza 0-200, default 100
  tts.set_amp(200)
  # Imposta la velocità 80-260, default 150
  tts.set_speed(150)
  # Imposta il gap 0-200, default 1
  tts.set_gap(1)
  # Imposta il tono 0-99, default 80
  tts.set_pitch(80)

  tts.say("Hello! I'm Espeak TTS.")

**Spiegazione del codice:**

* ``tts.set_amp()`` — Controlla il volume (0–200).
* ``tts.set_speed()`` — Regola la velocità di pronuncia (80–260).
* ``tts.set_gap()`` — Imposta il gap tra le parole (0–200).
* ``tts.set_pitch()`` — Imposta il tono (0–99).
* ``tts.say()`` — Converte il testo in parlato e lo riproduce.

💡 **Suggerimento:** Prova ad aumentare il tono e la velocità per rendere il robot allegro, o diminuirli per renderlo serioso.

----

2. Testare Pico2Wave
---------------------

Pico2Wave produce una voce **più naturale e simile a quella umana** rispetto a Espeak.
È molto facile da usare, ma meno flessibile — puoi solo **cambiare la lingua**, non il tono, la velocità o il volume.
Questo rende Pico2Wave un'ottima scelta quando desideri un parlato chiaro e fluido senza troppa configurazione.

**Eseguire il programma**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_pico2wave.py

* Dovresti sentire il Pironman 5 Pro MAX dire: "Hello! I'm Pico2Wave TTS."
* Prova a cambiare la lingua (ad esempio, ``es-ES`` per lo spagnolo) e ascolta come cambia la voce.

**Codice**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Pico2Wave

  # Crea un'istanza TTS Pico2Wave
  tts = Pico2Wave()

  # Imposta la lingua
  tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  # Saluto rapido (verifica di base)
  tts.say("Hello! I'm Pico2Wave TTS.")

**Spiegazione del codice:**

* ``tts.set_lang()`` — Imposta la lingua di output per la sintesi vocale.

  - ``en-US`` (predefinito)
  - ``en-GB``
  - ``de-DE``
  - ``es-ES``
  - ``fr-FR``
  - ``it-IT``

* ``tts.say()`` — Converte il testo in parlato e lo riproduce immediatamente.

----

Risoluzione dei Problemi
------------------------

* **Nessun suono durante l'esecuzione di Espeak o Pico2Wave**

  * Controlla che i tuoi altoparlanti/cuffie siano collegati e che il volume non sia disattivato.
  * Esegui un rapido test nel terminale:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

    Se non senti nulla, il problema è nell'uscita audio, non nel tuo codice Python.

* **La voce di Espeak suona troppo veloce o troppo robotica**

  * Prova a regolare i parametri nel tuo codice:

    .. code-block:: python

       tts.set_speed(120)   # più lento
       tts.set_pitch(60)    # tono diverso

* **Permesso negato durante l'esecuzione del codice**

  * Prova a eseguire con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

Confronto: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Caratteristica
     - Espeak
     - Pico2Wave
   * - Qualità della voce
     - Robotica, sintetica
     - Più naturale, simile a quella umana
   * - Lingue
     - Inglese predefinito
     - Meno, ma quelle comuni
   * - Regolabile
     - Sì (velocità, tono, ecc.)
     - No (solo lingua)
   * - Prestazioni
     - Molto veloce, leggero
     - Leggermente più lento, più pesante
