.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

1. TTS con Espeak y Pico2Wave
=================================================

En esta lección, usaremos dos motores de conversión de texto a voz (TTS) integrados en Raspberry Pi — **Espeak** y **Pico2Wave** — para hacer hablar al Pironman 5 Pro MAX.

Estos dos motores son simples y funcionan sin conexión, pero suenan bastante diferentes:

* **Espeak**: muy ligero y rápido, pero la voz es robótica. Puede ajustar velocidad, tono y volumen.
* **Pico2Wave**: produce una voz más suave y natural que Espeak, pero tiene menos opciones de configuración.

Escuchará la diferencia en **calidad de voz** y **características**.

----

1. Probando Espeak
--------------------

Espeak es un motor TTS ligero incluido en Raspberry Pi OS.
Su voz suena robótica, pero es altamente configurable: puede ajustar volumen, tono, velocidad y más.

**Ejecutar el programa**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_espeak.py

  * Debería escuchar al Pironman 5 Pro MAX decir: “Hello! I'm Espeak TTS.”
  * Intente cambiar los parámetros de ajuste en el código para experimentar cómo ``amp``, ``speed``, ``gap`` y ``pitch`` afectan el sonido.

**Código**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Espeak

  # Crear instancia de Espeak TTS
  tts = Espeak()
  # Establecer amplitud 0-200, por defecto 100
  tts.set_amp(200)
  # Establecer velocidad 80-260, por defecto 150
  tts.set_speed(150)
  # Establecer espacio entre palabras 0-200, por defecto 1
  tts.set_gap(1)
  # Establecer tono 0-99, por defecto 80
  tts.set_pitch(80)

  tts.say("Hello! I'm Espeak TTS.")

**Explicación del código:**

* ``tts.set_amp()`` — Controla el volumen (0–200).
* ``tts.set_speed()`` — Ajusta la velocidad del habla (80–260).
* ``tts.set_gap()`` — Establece el espacio entre palabras (0–200).
* ``tts.set_pitch()`` — Establece el tono (0–99).
* ``tts.say()`` — Convierte texto a voz y lo reproduce.

💡 **Consejo:** Intente aumentar el tono y la velocidad para que el robot suene alegre, o disminuirlos para que suene serio.

----

2. Probando Pico2Wave
-------------------------

Pico2Wave produce una **voz más natural y humana** en comparación con Espeak.
Es muy fácil de usar, pero menos flexible — solo puede **cambiar el idioma**, no el tono, la velocidad ni el volumen.
Esto hace que Pico2Wave sea una excelente opción cuando desea un habla clara y suave sin demasiada configuración.

**Ejecutar el programa**

  .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_pico2wave.py

* Debería escuchar al Pironman 5 Pro MAX decir: “Hello! I'm Pico2Wave TTS.”
* Intente cambiar el idioma (por ejemplo, ``es-ES`` para español) y escuche cómo cambia la voz.

**Código**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Pico2Wave

  # Crear instancia de Pico2Wave TTS
  tts = Pico2Wave()

  # Establecer el idioma
  tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  # Saludo rápido (verificación)
  tts.say("Hello! I'm Pico2Wave TTS.")

**Explicación del código:**

* ``tts.set_lang()`` — Establece el idioma de salida para la síntesis de voz.

  - ``en-US`` (por defecto)
  - ``en-GB``
  - ``de-DE``
  - ``es-ES``
  - ``fr-FR``
  - ``it-IT``

* ``tts.say()`` — Convierte el texto a voz y lo reproduce inmediatamente.

----

Solución de Problemas
------------------------

* **No hay sonido al ejecutar Espeak o Pico2Wave**

  * Verifique que sus altavoces/auriculares estén conectados y que el volumen no esté silenciado.
  * Ejecute una prueba rápida en la terminal:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

    Si no escucha nada, el problema es la salida de audio, no su código Python.

* **La voz de Espeak suena demasiado rápida o demasiado robótica**

  * Intente ajustar los parámetros en su código:

    .. code-block:: python

       tts.set_speed(120)   # más lento
       tts.set_pitch(60)    # tono diferente

* **Permiso denegado al ejecutar el código**

  * Intente ejecutar con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

Comparación: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Característica
     - Espeak
     - Pico2Wave
   * - Calidad de voz
     - Robótica, sintética
     - Más natural, humana
   * - Idiomas
     - Inglés por defecto
     - Menos, pero los comunes
   * - Ajustable
     - Sí (velocidad, tono, etc.)
     - No (solo idioma)
   * - Rendimiento
     - Muy rápido, ligero
     - Ligeramente más lento, más pesado