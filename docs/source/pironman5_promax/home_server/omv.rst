.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_omv_5_promax:

Configuración de OpenMediaVault
=====================================

.. warning::

   OpenMediaVault **no** soporta la instalación en el escritorio de Raspberry Pi OS.

   ⚠️ **Solo se soportan las versiones Lite 11 (Bullseye) y 12 (Bookworm) de Raspberry Pi OS.**

   Asegúrese de haber instalado el sistema operativo correcto y configurado la red.
   El procedimiento aquí es consistente con :ref:`install_os_sd_rpi_promax`, pero al seleccionar una imagen, elija Raspberry Pi OS Lite de Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (abreviado como OMV) es un sistema operativo de almacenamiento conectado a la red (NAS) de código abierto basado en Debian Linux, diseñado para entornos domésticos y pequeñas oficinas, con el objetivo de simplificar la gestión de almacenamiento y proporcionar ricas funciones de servicios de red.

Siga estos pasos para instalar OpenMediaVault en su Raspberry Pi:

1. Conéctese a su Raspberry Pi Usando SSH
-----------------------------------------------------------

   Ingrese el siguiente comando en la terminal:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Si está usando Windows, use PuTTY u otro cliente SSH para conectarse a su Raspberry Pi.

2. Instalar OpenMediaVault
----------------------------

   Ingrese el siguiente comando en la terminal:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install
      chmod +x install
      sudo ./install -n

   Esto descargará y ejecutará el script de instalación de OpenMediaVault. No reinicie su Raspberry Pi después de la instalación.

3. Acceder a OpenMediaVault
-----------------------------

   Ingrese la siguiente URL en su navegador para acceder a OpenMediaVault:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Si no puede acceder a la URL anterior, intente usar la dirección IP en su lugar, por ejemplo, http://192.168.1.100.

   Verá una página de inicio de sesión, inicie sesión usando el nombre de usuario y contraseña predeterminados. El nombre de usuario predeterminado es ``admin`` y la contraseña es ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Después de iniciar sesión, verá la interfaz principal de OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Ahora que ha instalado y accedido correctamente a OpenMediaVault, puede comenzar a configurar y gestionar su almacenamiento.

4. Configurar RAID (Opcional)
---------------------------------------

   RAID NVMe es una solución de almacenamiento que combina múltiples Unidades de Estado Sólido (SSD) NVMe utilizando tecnología RAID, con el objetivo de maximizar el rendimiento de alta velocidad del protocolo NVMe y las características de redundancia/mejora de rendimiento de RAID. Los modos comunes incluyen RAID 0, 1, 5, 10, etc. Para SSD NVMe duales, RAID 0 y RAID 1 son los modos más utilizados.

   * RAID 0 es una tecnología de striping que divide los datos en múltiples tiras y distribuye estas tiras en múltiples discos duros, logrando así mayores velocidades de lectura/escritura. RAID 0 no proporciona protección de redundancia, por lo que si cualquiera de los discos duros falla, todos los datos se perderán.

   * RAID 1 es una tecnología de mirroring que copia los datos en múltiples discos duros, proporcionando así protección de redundancia. Las velocidades de lectura/escritura de RAID 1 dependen de la velocidad de un solo disco duro, ya que los datos deben leerse de múltiples discos duros. Si cualquiera de los discos duros falla, los otros pueden continuar proporcionando datos.

   .. note:: Monte al menos 2 discos para RAID 0 o RAID 1. En RAID 0, la capacidad del volumen RAID será la suma de las capacidades de todos los discos. En RAID 1, la capacidad del volumen RAID será la misma que la capacidad del disco más pequeño.

   1. En el menú ``System``, haga clic en la opción ``Plugins``, busque el plugin ``openmediavault-md`` e instálelo.

   .. image:: img/omv/omv-raid-1.png

   2. En el menú ``Storage``, haga clic en la opción ``Disks``, borre dos SSD.

   .. image:: img/omv/omv-raid-2.png

   3. Tenga en cuenta que esta acción borrará todos los datos en los discos duros, asegúrese de haber respaldado todos los datos importantes.

   .. image:: img/omv/omv-raid-3.png

   4. El modo de borrado ``QUICK`` es suficiente.

   .. image:: img/omv/omv-raid-4.png

   5. Ingrese a la pestaña ``Multiple Device``, haga clic en ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. En la opción Level, puede elegir Stripe (RAID 0) o Mirror (RAID 1). En la opción Devices, seleccione los discos duros que acaba de borrar. Haga clic en ``Save`` y espere a que se complete la configuración RAID.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Si aparece un informe de error (500 - Internal Server Error), intente reiniciar el sistema OMV.

   7. Aplique la configuración haciendo clic en el botón ``Apply``.

   .. image:: img/omv/omv-raid-7.png

   8. Después de que la configuración RAID esté completa, debe esperar a que el estado del RAID sea ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. Después de que la configuración RAID esté completa, sus discos duros ahora están en configuración RAID 0 o RAID 1, y puede usarlos como un solo dispositivo de almacenamiento.

5. Configurar el Almacenamiento
---------------------------------------------------------------------

   En la interfaz principal de OpenMediaVault, haga clic en la opción ``Storage`` en el menú lateral izquierdo. En la página ``Storage``, haga clic en la pestaña ``Disks``. En la página ``Disks``, verá todos los discos en su Raspberry Pi. Asegúrese de que su NVMe PIP tenga un disco duro conectado.

   .. image:: img/omv/omv-disk.png

   1. En la barra lateral, haga clic en la opción ``File System``. Luego cree y monte un sistema de archivos. Elija ``ext4`` como tipo de sistema de archivos.

   .. image:: img/omv/omv-mount.png

   2. Seleccione Device y guarde.

   .. note:: Si ha configurado RAID, verá el dispositivo RAID en la lista. Simplemente selecciónelo y guarde.

   .. image:: img/omv/omv-mount-2.png

   3. Aparecerá una ventana informándole que se está creando el sistema de archivos, espere un momento.

   .. image:: img/omv/omv-mount-3.png

   4. Una vez hecho esto, ingresará a la interfaz ``Mount``, seleccione el sistema de archivos que acaba de crear y móntelo en su Raspberry Pi.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Si está usando discos duros duales (y no RAID), debe repetir los pasos anteriores para también montar el segundo disco duro en su Raspberry Pi.

   5. Después de montar, aplique los cambios y luego podrá ver los datos en sus discos duros en el sistema de archivos.

   .. image:: img/omv/omv-mount-5.png

   En este punto, ha configurado correctamente OpenMediaVault y montado sus discos duros. Ahora puede usar OpenMediaVault para gestionar su almacenamiento.

6. Crear una Carpeta Compartida
---------------------------------------

   1. En la página ``Storage``, vaya a la pestaña ``Shared Folders``. Y haga clic en el botón ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. En la página ``Create Shared Folder``, ingrese el nombre de la carpeta compartida, seleccione el disco duro que desea compartir, la ruta de la carpeta compartida y establezca los permisos de la carpeta compartida. Luego haga clic en el botón ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Ahora puede ver la carpeta compartida que acaba de crear. Confirme que es correcta y luego aplique.

   .. image:: img/omv/omv-share-3.png

   Ahora ha creado correctamente una carpeta compartida.

7. Crear un Nuevo Usuario
---------------------------------------

   Para acceder a la carpeta, necesitamos crear un nuevo usuario, siga estos pasos:

   1. En la página ``User``, haga clic en el botón ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. En la página ``Create User``, ingrese el nombre de usuario y la contraseña del nuevo usuario, luego haga clic en el botón ``Save``.

   .. image:: img/omv/omv-user-2.png

   Ahora ha creado correctamente un nuevo usuario.

8. Establecer Permisos para el Nuevo Usuario
------------------------------------------------------------------------

   1. En la página ``Shared Folders``, haga clic en la carpeta compartida que acaba de crear. Luego haga clic en el botón ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. En la página ``Permissions``, establezca los permisos. Luego haga clic en el botón ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Después de completar, haga clic en el botón ``Apply``.

   .. image:: img/omv/omv-user-5.png

   Ahora puede usar este nuevo usuario para acceder a su carpeta compartida.

9. Configurar el Servicio SMB
---------------------------------------

   1. En la página ``Services``, busque la pestaña ``SMB/CIFS`` > ``Setting``. Y marque la opción ``Enable``. Luego haga clic en el botón ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Aplique los cambios haciendo clic en el botón ``Apply``.

   .. image:: img/omv/omv-smb-2.png

   3. Ingrese a la página ``Shares``, haga clic en el botón ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. En la página ``Create Share``, seleccione la ruta de la carpeta compartida. Luego haga clic en el botón ``Save``. De paso, hay muchas opciones en esta página que puede configurar según sea necesario.

   .. image:: img/omv/omv-smb-4.png

   5. Haga clic en ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Ahora ha configurado correctamente el servicio SMB. Ahora puede usar el protocolo SMB para acceder a su carpeta compartida.

10. Acceder a la Carpeta Compartida en Windows
----------------------------------------------------------------

   1. Abra ``Este PC``, luego haga clic en ``Map network drive``.

   .. image:: img/omv/omv-network-location-1.png

   2. En el cuadro de diálogo emergente, ingrese la IP de la Raspberry Pi en el campo ``Folder``, por ejemplo, ``\\192.168.1.100\``, o el nombre de host de la Raspberry Pi, por ejemplo, ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Haga clic en el botón de búsqueda, luego seleccione la carpeta compartida a la que desea acceder. Durante este proceso, deberá ingresar el nombre de usuario y la contraseña que creó anteriormente.

   .. image:: img/omv/omv-network-location-3.png

   4. Marque "Reconnect at sign-in" y haga clic en el botón ``Finish``.

   .. image:: img/omv/omv-network-location-4.png

   5. Ahora puede acceder a la carpeta compartida NAS.

   .. image:: img/omv/omv-network-location-5.png

10. Acceder a la Carpeta Compartida en Mac
---------------------------------------------------------------------------

   1. En el menú ``Go``, haga clic en ``Connect to Server``.

   .. image:: img/omv/omv-mac-1.png

   2. En el cuadro de diálogo emergente, ingrese la IP de la Raspberry Pi, como ``smb://192.168.1.100``, o el nombre de host de la Raspberry Pi, como ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Haga clic en el botón ``Connect``.

   .. image:: img/omv/omv-mac-3.png

   4. En el cuadro de diálogo emergente, ingrese el nombre de usuario y la contraseña que creó anteriormente. Haga clic en el botón ``Connect``.

   .. image:: img/omv/omv-mac-4.png

   5. Ahora puede acceder a la carpeta compartida NAS.

   .. image:: img/omv/omv-mac-5.png