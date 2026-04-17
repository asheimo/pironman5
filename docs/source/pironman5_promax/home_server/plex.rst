.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configuración de Plex
=======================================

Plex es una potente plataforma de servidor multimedia que le permite organizar, transmitir y acceder a sus películas, programas de TV, música y fotos en múltiples dispositivos. Al configurar Plex en la serie Pironman5 impulsada por Raspberry Pi, puede crear un centro multimedia doméstico asequible y energéticamente eficiente que funciona 24/7. El tamaño compacto, el bajo consumo de energía y la flexibilidad de la Raspberry Pi la convierten en una excelente opción para alojar Plex, transformando su Pi en un centro de entretenimiento personal accesible desde su red doméstica o incluso de forma remota.

**Preparación**

* Tarjeta MicroSD (16GB+, se recomienda Clase 10)
* Sistema oficial de Raspberry Pi: Raspberry Pi OS (o Raspberry Pi OS Lite)
* Conexión de red estable (se recomienda Ethernet por cable)
* Disco duro externo o memoria USB (para almacenamiento expandido)

**Instalar Portainer**

Abra la terminal e ingrese los siguientes comandos:

1. Instalar Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Instalar Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Reinicie su Raspberry Pi. (Luego complete los siguientes pasos **INMEDIATAMENTE**.)

4. Después de que su Raspberry Pi arranque, abra un navegador web y visite su dirección de Portainer: ``http://<ip-de-su-rpi>:9443``.

5. Por defecto, puede ver una advertencia de que el sitio utiliza un certificado SSL/TLS autofirmado no emitido por una Autoridad de Certificación (CA) conocida. La mayoría de los navegadores web mostrarán dicha advertencia. En este caso, puede ignorarla de manera segura, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

#. En su primer inicio de sesión, se le pedirá que establezca una contraseña de administrador.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Después de crear la cuenta de administrador, ingresará a la interfaz de Portainer. Desde la barra de navegación izquierda, vaya a **Setting -> General**, busque **App Templates** e ingrese la siguiente URL en el campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Haga clic en **Save Application Settings**. La configuración tardará unos 10 segundos en completarse.

**Instalar Plex**

1. Desde la barra de navegación izquierda, haga clic en **Home -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Vaya a **Templates -> Application**. En la barra de búsqueda de la esquina superior derecha, escriba *plex* y haga clic en él.

   .. image:: img/home_server_app/ptn_temp_plex.png

3. Establezca el modo de red en **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

4. Expanda **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

5. En la sección **volume mapping**, configure las rutas de almacenamiento para sus archivos multimedia y otorgue a Plex permisos de lectura/escritura. Las rutas predeterminadas son ``/portainer/TV`` y ``/portainer/Movies``, ambas con acceso de lectura/escritura habilitado.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

6. Haga clic en **Deploy** y espere a que Plex termine de instalarse.

**Configurar el Servidor Plex**

1. Abra su navegador e ingrese: ``http://<su_ip>:32400/web``. Ahora debería ver la interfaz de Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Omita la oferta de suscripción premium.

3. A continuación, verá la pantalla **Server Setup**. Puede marcar *Allow me to access my media outside my home*. Por ahora, se recomienda dejar esto sin marcar y configurarlo más tarde si es necesario.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Luego se le pedirá que organice su biblioteca multimedia. Puede elegir *Skip* y agregar medios más tarde a través de la configuración. Sin embargo, se recomienda agregar directamente las rutas de almacenamiento que configuró en el mapeo de volúmenes de Portainer para que Plex pueda escanear e importar automáticamente sus archivos multimedia.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Seleccione el tipo de biblioteca multimedia, asigne un nombre a su biblioteca y elija el idioma.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Agregue carpetas. Localice las rutas de almacenamiento de medios que configuró anteriormente y haga clic en **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Haga clic en **Finish**. El servidor Plex de su Raspberry Pi ahora está completamente configurado.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Ahora debería ver sus archivos multimedia mostrados en la página de inicio del servidor Plex.

   .. image:: img/home_server_app/plex_index.png