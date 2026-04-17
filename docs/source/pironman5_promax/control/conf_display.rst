.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configuración de la Pantalla
===================================================================

Este capítulo le guía a través de la configuración de la pantalla para el Pironman 5 Pro MAX, incluyendo la habilitación del apagado automático de la pantalla para ahorrar energía y la configuración de la rotación de la pantalla para adaptarse a orientaciones de instalación especiales.

-------------------------------------------------------------------

**Configuración del Reposo de la Pantalla en Inactividad**


Para ahorrar energía cuando no esté usando activamente el Pironman 5 Pro MAX, puede habilitar la función de reposo automático de la pantalla. Cuando el dispositivo ha estado inactivo durante un período determinado, la pantalla principal se apagará automáticamente, entrando en un estado de bajo consumo.

Siga estos pasos para configurarlo:

1. Haga clic en **Menu -> Preferences** en la esquina inferior izquierda de la pantalla, luego busque y abra el **Control Centre**.

   .. image:: img/sleep_screen1.png

2. En la interfaz del Control Centre, haga clic para acceder a la configuración de **Display**.

3. Localice la opción **Screen Blanking** y actívela.

   .. image:: img/sleep_screen2.png

----------------------------------------------------------------------

**Invertir el Pironman 5 Pro MAX**

El Pironman 5 Pro MAX se puede voltear para su uso. En esta configuración, la pantalla táctil quedará en la parte superior y los puertos GPIO en la parte inferior, ofreciendo mayor flexibilidad para varios proyectos. Esta configuración es ideal para aplicaciones como una visualización más conveniente de la pantalla o un acceso más fácil a los pines GPIO al conectar sensores.

Al voltear el dispositivo, ambas pantallas necesitan ajustes separados:

   * Pantalla táctil principal — Requiere configuración de rotación a nivel del sistema operativo
   * Pantalla de estado OLED — Requiere configuración mediante línea de comandos

Para invertir el Pironman 5 Pro MAX, siga estos pasos:

1. Preparación Física

   Retire la cámara del Pironman 5 Pro MAX, voltee toda la unidad y vuelva a instalar la cámara. La instalación debe ser simétrica a su orientación original.

   .. image:: img/inverted_screen0.png

2. Configuración de la Orientación de la Pantalla Táctil

   Encienda el dispositivo. En la pantalla táctil, mantenga presionado el escritorio para que aparezca el menú y seleccione **Desktop Preferences**.

   .. image:: img/inverted_screen1.png

   Desplácese hacia abajo para encontrar la opción **Screens**, luego mantenga presionado el indicador de pantalla en la pantalla. Seleccione **Orientation → Inverted**.

   .. image:: img/inverted_screen2.png

   Aplique, la ventana de actualización mostrará la pantalla, debe hacer clic en OK para confirmar.

   .. image:: img/inverted_screen3.png

3. Configuración de la Pantalla OLED

   En la Terminal, ejecute el siguiente comando para rotar el OLED 180 grados:

   .. code-block:: bash

      sudo pironman5 -or 180

----------------------------------------------------

**Nota**

- Después de voltear, asegúrese de que la unidad esté colocada sobre una superficie estable para evitar que se vuelque.
- Si experimenta desalineación en la entrada táctil, recalibre la pantalla táctil a través de la configuración del sistema.
- Para ajustes avanzados de pantalla, consulte la sección :ref:`promax_view_control_commands` para obtener comandos adicionales relacionados con el OLED y la rotación de pantalla.