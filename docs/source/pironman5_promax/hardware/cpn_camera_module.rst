.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _cpn_camera_module:

Kameramodul
====================================


**Beschreibung**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Dies ist ein 5-Megapixel-Raspberry-Pi-Kameramodul mit OV5647-Sensor. Es ist Plug-and-Play-fähig: Schließen Sie das mitgelieferte Flachbandkabel an den CSI-Anschluss (Camera Serial Interface) Ihres Raspberry Pi an, und schon kann es losgehen.

Die Platine ist klein, etwa 25 mm x 23 mm x 9 mm, und wiegt 3 g, was sie ideal für mobile oder andere Anwendungen macht, bei denen Größe und Gewicht entscheidend sind. Das Kameramodul hat eine native Auflösung von 5 Megapixeln und ein fest eingebautes Objektiv mit fester Brennweite, das Standbilder mit 2592 x 1944 Pixeln aufnimmt und auch Video in 1080p30, 720p60 und 640 x 480p90 unterstützt.

.. note:: 

   Das Modul kann nur Bilder und Videos aufnehmen, keinen Ton.



**Technische Daten**

* **Auflösung Standbilder**: 2592×1944 
* **Unterstützte Videoauflösungen**: 1080p/30 fps, 720p/60 fps und 640 x 480p 60/90 Videoaufzeichnung 
* **Blende (F)**: 1,8 
* **Bildwinkel**: 65 Grad 
* **Abmessungen**: 24mm x 23,5mm x 8mm 
* **Gewicht**: 3g 
* **Schnittstelle**: CSI-Anschluss 
* **Unterstütztes Betriebssystem**: Raspberry Pi OS (aktuelle Version empfohlen) 



**Kameramodul zusammenbauen**
-------------------------------------


Auf dem Kameramodul oder dem Raspberry Pi finden Sie einen flachen Kunststoffstecker. Ziehen Sie vorsichtig den schwarzen Fixierschalter heraus, bis er teilweise herausgezogen ist. Führen Sie das FFC-Kabel in der gezeigten Richtung in den Kunststoffstecker ein und drücken Sie den Fixierschalter wieder in seine Position.

Wenn das FFC-Kabel korrekt installiert ist, sitzt es gerade und lässt sich nicht herausziehen, wenn Sie sanft daran ziehen. Wenn nicht, installieren Sie es erneut.


.. image:: img/connect_ffc.png


.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   Installieren Sie die Kamera nicht bei eingeschalteter Stromversorgung, da dies die Kamera beschädigen kann.