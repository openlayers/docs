======
Layers
======

Layers are the 'datasources' in OpenLayers.

Raster Layers
-------------

Raster Layers are imagery layers.

Google
++++++

Layer for using Google Maps data within OpenLayers. For API information, see the `Google Layer API Docs`_. For an example of usage, see the `Spherical Mercator example`_.

.. _`Google Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Google-js.html

.. _`Spherical Mercator example`: http://openlayers.org/dev/examples/spherical-mercator.html

Image
+++++

For API information, see the `Image Layer API Docs`_.

.. _`Image Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Image-js.html

KaMap
+++++

For API information, see the `KaMap Layer API Docs`_.

.. _`KaMap Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/KaMap-js.html

KaMapCache
++++++++++
For API information, see the `KaMapCache Layer API Docs`_.

.. _`KaMapCache Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/KaMapCache-js.html


MapGuide
++++++++
For API information, see the `MapGuide Layer API Docs`_.

.. _`MapGuide Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/MapGuide-js.html


MapServer
+++++++++
For API information, see the `MapServer Layer API Docs`_.

.. _`MapServer Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/MapServer-js.html


MultiMap
++++++++
For API information, see the `MultiMap Layer API Docs`_.

.. _`MultiMap Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/MultiMap-js.html


TMS
+++
For API information, see the `TMS Layer API Docs`_.

.. _`TMS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/TMS-js.html


TileCache
+++++++++
For API information, see the `TileCache Layer API Docs`_.

.. _`TileCache Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/TileCache-js.html


VirtualEarth
++++++++++++
For API information, see the `VirtualEarth Layer API Docs`_.

.. _`VirtualEarth Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/VirtualEarth-js.html


WMS
+++

Layer type for accessing WMS data.  

For API information, see the `WMS Layer API Docs`_.

.. _`WMS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/WMS-js.html


WorldWind
+++++++++

For API information, see the `WorldWind Layer API Docs`_.

.. _`WorldWind Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/WorldWind-js.html


Yahoo
+++++

For API information, see the `Yahoo Layer API Docs`_.

.. _`Yahoo Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Yahoo-js.html


Vector Layers
-------------

Vector layers are any layers that have their source data in a format other than
imagery. This includes subclasses of both OpenLayers.Layer.Markers and 
OpenLayers.Layer.Vector layers.

Boxes
+++++

Based on subclassing markers. In general, it is probably better to implement
this functionality with a Vectors layer and polygon geometries. Maintained
for backwards compatibility.

For API information, see the `Boxes Layer API Docs`_.

.. _`Boxes Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Boxes-js.html


GML
+++

The GML layer is a vector layer subclass designed to read data from a file
once and display it. It is ideal for working with many formats, not just GML,
and can be configured to read other formats via the 'format' option on the 
layer.

The simplest use case of the GML layer is simply to load a GML file. The 
`GML Layer Example`_ shows this: simply add:

.. code-block:: javascript
   
   var layer = new OpenLayers.Layer.GML("GML", "gml/polygon.xml")
   map.addLayer(layer);

If you want to add a different type of format, you can change the format
option of the layer at initialization. The `KML example`_ demonstrates this: 

.. code-block:: javascript
   
   var layer = new OpenLayers.Layer.GML("KML", "kml/lines.kml", {
      format: OpenLayers.Format.KML
   })
   map.addLayer(layer);

You can also add formatOption to the layer: these options are used when
creating the format class internally to the layer.

.. code-block:: javascript
   
   var layer = new OpenLayers.Layer.GML("KML", "kml/lines.kml", {
      format: OpenLayers.Format.KML,
      formatOptions: {
        'extractStyles': true
      }
   });
   map.addLayer(layer);

The format options are determined by the format class.

For API information, see the `GML Layer API Docs`_.

.. _`KML example`: http://openlayers.org/dev/examples/kml-layer.html
.. _`GML Layer example`: http://openlayers.org/dev/examples/gml-layer.html
.. _`GML Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/GML-js.html

GeoRSS
++++++

The GeoRSS layer uses the GeoRSS format, and displays the results as clickable
markers. It is a subclass of the Markers layer, and does not support lines
or polygons. It has many hardcoded behaviors, and in general, you may be better
off using a GML layer with a SelectFeature Control instead of the GeoRSS
layer if you want configurability of your application behavior.

For API information, see the `GeoRSS Layer API Docs`_.

.. _`GeoRSS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/GeoRSS-js.html

Markers
+++++++

The Markers base layer is simple, and allows use of the addMarkers function
to add markers to the layer. It supports only points, not lines or polygons.

For API information, see the `Markers Layer API Docs`_.

.. _`Markers Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Markers-js.html

PointTrack
++++++++++

For API information, see the `PointTrack Layer API Docs`_.

.. _`PointTrack Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/PointTrack-js.html


Text
++++

The Text layer uses the Text format, and displays the results as clickable
markers. It is a subclass of the Markers layer, and does not support lines
or polygons. It has many hardcoded behaviors, and in general, you may be better
off using a GML layer with a SelectFeature Control instead of the Text
layer if you want configurability of your application behavior.

For API information, see the `Text Layer API Docs`_.

.. _`Text Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Text-js.html

Vector
++++++

The Vector Layer is the basis of the advanced geometry support in OpenLayers.
Classes like GML and WFS subclass from the Vector layer. When creating features
in JavaScript code, using the Vector layer directly is likely a good way to go.

As of OpenLayers 2.7, development has begun on extending the Vector Layer to
have additional capabilities for loading data, to replace the large number
of layer subclasses. This work on Strategy and Protocol classes is designed
to make it easier to interact with data from remote datasources. For more
information on Protocols and Strategies, see the OpenLayers API documentation.

For API information, see the `Vector Layer API Docs`_.

.. _`Vector Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Vector-js.html

WFS
+++

For API information, see the `WFS Layer API Docs`_.

.. _`WFS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/WFS-js.html


Generic Subclasses
------------------

* EventPane
* FixedZoomLevels
* Grid
* HTTPRequest
* SphericalMercator
