.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configuración de NextCloudPi
=======================================

NextCloud es una solución de almacenamiento en la nube privada de código abierto, similar a Google Drive o Dropbox. Se puede utilizar para almacenar archivos, compartir documentos, sincronizar fotos y gestionar calendarios y contactos.
A diferencia de los servicios de nube pública, NextCloud brinda a los usuarios control total sobre sus datos, lo que lo hace ideal para individuos y pequeños equipos que valoran la privacidad y la seguridad de los datos.

La serie Pironman5 impulsada por Raspberry Pi ofrece bajo consumo de energía, tamaño compacto y rendimiento confiable, lo que la convierte en una excelente opción para un servidor de nube privada doméstico. Combinado con NextCloud, puede funcionar como un sistema NAS rentable.

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

4. Después de que su Raspberry Pi arranque, abra un navegador web y visite su dirección de Portainer: ``https://<ip-de-su-rpi>:9443``.

5. Por defecto, verá una advertencia de que el sitio utiliza un certificado SSL/TLS autofirmado no emitido por una Autoridad de Certificación (CA) conocida. La mayoría de los navegadores web mostrarán una advertencia sobre dichos certificados. En este caso, puede ignorar la advertencia de manera segura, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

#. En el primer inicio de sesión, deberá establecer una contraseña de administrador.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Después de registrar la cuenta de administrador, ingresará a la interfaz de Portainer. Desde la barra de navegación izquierda, haga clic en **Setting -> General**, busque **App Templates** e ingrese la siguiente URL en el campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Haga clic en **Save Application Settings**. La configuración tardará alrededor de 10 segundos en completarse.

**Instalar NextCloud**

1. Desde la barra de navegación izquierda, haga clic en **Home -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. Vaya a **Templates -> Application**. En la barra de búsqueda de la esquina superior derecha, escriba *nextcloud* y haga clic en él.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Haga clic en **Deploy the stack** y espere a que se complete la implementación. Esto suele tomar unos dos minutos.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Una vez completado, NextCloud estará instalado.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**Usar NextCloud**

1. Abra su navegador y visite su dirección de NextCloud: ``https://<ip-de-su-rpi>:32768``.

.. note::

   De manera similar, verá una advertencia de que el sitio utiliza un certificado SSL/TLS autofirmado no emitido por una Autoridad de Certificación (CA) conocida. La mayoría de los navegadores web mostrarán una advertencia sobre dichos certificados.
   En este caso, puede ignorar la advertencia de manera segura, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

2. En el primer inicio de sesión, deberá establecer una contraseña de administrador.

   .. image:: img/home_server_app/nc_admin_install.png

3. Después del registro, puede comenzar a usar NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png