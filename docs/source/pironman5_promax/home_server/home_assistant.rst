.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

Configuración de Home Assistant
======================================

Home Assistant es una plataforma de automatización del hogar que se ejecuta sobre un centro central (Raspberry Pi, PC, etc.). Se puede utilizar para controlar y monitorear todo tipo de dispositivos, desde luces y termostatos hasta cámaras de seguridad y electrodomésticos inteligentes.

**Preparación**

Antes de comenzar, asegúrese de tener lo siguiente:

* Una Raspberry Pi que pueda ejecutar Home Assistant.
* Una conexión a internet estable.
* Una cuenta en Home Assistant Cloud (opcional, pero recomendada para acceso remoto).

**Instalación**

Abra la terminal e ingrese los siguientes comandos:

1. Instalar Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Instalar Home Assistant

.. code-block:: bash

   sudo docker pull homeassistant/home-assistant

**Ejecutar el Contenedor de Home Assistant**

Aquí, usamos Docker Compose para ejecutar Home Assistant. Puede pensar en Docker Compose como un "script de automatización". Escribirá todas las configuraciones (como nombre de la imagen, puertos, montajes de volúmenes, variables de entorno, etc.) en un archivo ``docker-compose.yml``. Después de eso, con solo un simple comando ``docker compose up -d``, Docker creará e iniciará automáticamente todos los contenedores configurados según este "script".

1. **Ingrese al directorio del proyecto**: Vaya a esa carpeta.

   .. code-block:: bash

      cd ~/homeassistant

2. **Cree el archivo de configuración**: En el directorio ``~/homeassistant``, cree un archivo llamado ``docker-compose.yml`` y copie la configuración anterior en él.

   .. code-block:: bash

      sudo nano docker-compose.yml

3. Pegue el siguiente contenido en el archivo ``docker-compose.yml``:

   .. note:: Reemplace ``- TZ=Asia/Shanghai`` con su zona horaria.

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

4. Presione ``Ctrl+X`` para salir del editor, y luego presione ``Y`` para guardar los cambios.

5. **Iniciar Home Assistant**: En el directorio ``~/homeassistant``, ejecute el siguiente comando. Docker Compose extraerá automáticamente la imagen e iniciará el contenedor.

   .. code-block:: bash

      sudo docker compose up -d

   * ``up``: Crea e inicia los servicios.
   * ``-d``: Ejecuta en segundo plano (modo desconectado).

6. **Verificar el estado de ejecución**:

    .. code-block:: bash

      docker compose ps

    Debería ver el estado de ``homeassistant`` como ``Up``.

7. **Ver los registros** (si hay problemas al iniciar):

   .. code-block:: bash

      docker compose logs -f

8. Para más comandos, consulte:

   .. code-block:: bash

      docker compose --help

**Configuración Inicial**

Ahora, puede abrir el navegador de su computadora e ingresar: ``http://<Dirección de su Raspberry Pi>:8123`` para acceder a Home Assistant.

.. image:: img/home_assistant/ha_welcome.png

Seleccione **CREATE MY SMART HOME** y luego cree su cuenta.

.. image:: img/home_assistant/ha_onboarding.png

Siga las instrucciones para elegir su ubicación y otras configuraciones. Una vez completado, ingresará al panel de Home Assistant.

.. image:: img/home_assistant/ha_overview.png