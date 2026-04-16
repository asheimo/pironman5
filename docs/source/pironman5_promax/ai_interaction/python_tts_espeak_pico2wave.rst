.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



1. TTS avec Espeak et Pico2Wave
=================================================

Dans cette leçon, nous allons utiliser deux moteurs de synthèse vocale (TTS) intégrés sur Raspberry Pi — **Espeak** et **Pico2Wave** — pour faire parler le Pironman 5 Pro MAX.

Ces deux moteurs sont simples et fonctionnent hors ligne, mais leur son est assez différent :

* **Espeak** : très léger et rapide, mais la voix est robotique. Vous pouvez ajuster la vitesse, la hauteur tonale et le volume.
* **Pico2Wave** : produit une voix plus douce et plus naturelle qu'Espeak, mais offre moins d'options de configuration.

Vous remarquerez la différence en termes de **qualité vocale** et de **fonctionnalités**.

----

1. Tester Espeak
--------------------

Espeak est un moteur TTS léger inclus dans Raspberry Pi OS.
Sa voix sonne de manière robotique, mais il est hautement configurable : vous pouvez ajuster le volume, la hauteur tonale, la vitesse, et plus encore.

**Exécuter le programme**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_espeak.py

  * Vous devriez entendre le Pironman 5 Pro MAX dire : « Hello! I'm Espeak TTS. »
  * Essayez de modifier les paramètres de réglage dans le code pour expérimenter comment ``amp``, ``speed``, ``gap`` et ``pitch`` affectent le son.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Espeak

  # Créer une instance TTS Espeak
  tts = Espeak()
  # Définir l'amplitude 0-200, valeur par défaut 100
  tts.set_amp(200)
  # Définir la vitesse 80-260, valeur par défaut 150
  tts.set_speed(150)
  # Définir l'écart entre les mots 0-200, valeur par défaut 1
  tts.set_gap(1)
  # Définir la hauteur tonale 0-99, valeur par défaut 80
  tts.set_pitch(80)

  tts.say("Hello! I'm Espeak TTS.")

**Explication du code :**

* ``tts.set_amp()`` — Contrôle le volume (0–200).
* ``tts.set_speed()`` — Ajuste la vitesse de parole (80–260).
* ``tts.set_gap()`` — Définit l'écart entre les mots (0–200).
* ``tts.set_pitch()`` — Définit la hauteur tonale (0–99).
* ``tts.say()`` — Convertit le texte en parole et le lit.

💡 **Astuce :** Essayez d'augmenter la hauteur tonale et la vitesse pour rendre la voix du robot plus joyeuse, ou de les baisser pour la rendre plus sérieuse.

----

2. Tester Pico2Wave
---------------------

Pico2Wave produit une **voix plus naturelle et humaine** par rapport à Espeak.
Il est très facile à utiliser, mais moins flexible — vous ne pouvez **changer que la langue**, pas la hauteur tonale, la vitesse ou le volume.
Cela rend Pico2Wave un excellent choix lorsque vous voulez une parole claire et fluide sans trop de configuration.

**Exécuter le programme**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_pico2wave.py

* Vous devriez entendre le Pironman 5 Pro MAX dire : « Hello! I'm Pico2Wave TTS. »
* Essayez de changer la langue (par exemple, ``es-ES`` pour l'espagnol) et écoutez comment la voix change.

**Code**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Pico2Wave

  # Créer une instance TTS Pico2Wave
  tts = Pico2Wave()

  # Définir la langue
  tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  # Bonjour rapide (vérification de base)
  tts.say("Hello! I'm Pico2Wave TTS.")

**Explication du code :**

* ``tts.set_lang()`` — Définit la langue de sortie pour la synthèse vocale.

  - ``en-US`` (par défaut)
  - ``en-GB``
  - ``de-DE``
  - ``es-ES``
  - ``fr-FR``
  - ``it-IT``

* ``tts.say()`` — Convertit le texte en parole et le lit immédiatement.

----

Dépannage
-------------------

* **Pas de son lors de l'exécution d'Espeak ou Pico2Wave**

  * Vérifiez que vos haut-parleurs/casque sont connectés et que le volume n'est pas en sourdine.
  * Effectuez un test rapide dans le terminal :

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Si vous n'entendez rien, le problème vient de la sortie audio, pas de votre code Python.

* **La voix d'Espeak sonne trop rapide ou trop robotique**

  * Essayez d'ajuster les paramètres dans votre code :

    .. code-block:: python

       tts.set_speed(120)   # plus lent
       tts.set_pitch(60)    # hauteur tonale différente

* **Permission refusée lors de l'exécution du code**

  * Essayez d'exécuter avec ``sudo`` :

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

Comparaison : Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Fonctionnalité
     - Espeak
     - Pico2Wave
   * - Qualité vocale
     - Robotique, synthétique
     - Plus naturelle, humaine
   * - Langues
     - Anglais par défaut
     - Moins, mais courantes
   * - Ajustable
     - Oui (vitesse, hauteur tonale, etc.)
     - Non (seulement la langue)
   * - Performance
     - Très rapide, léger
     - Légèrement plus lent, plus lourd