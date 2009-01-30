======
Layers
======

Layers are the 'datasources' in OpenLayers.

BaseLayers and Overlays
-----------------------

OpenLayers has two types of layers when operating in your application: base
layers and overlays. This difference controls several aspects of how you
interact with an OpenLayers Map.

Base Layers
+++++++++++

Base Layers are mutually exclusive layers, meaning only one can be enabled
at any given time. The currently active base layer determines the available
projection (coordinate system) and zoom levels available on the map. 

Whether a layer is a base layer or not is determined by the isBaseLayer 
property on the layer. Most raster layers have the isBaseLayer property set
to true by default. It can be changed in the layer options.

Base Layers always display below overlay layers.

Overlay Layers
++++++++++++++

Overlay layers are the alternative to Base Layers. Multiple overlays can
be enabled at a time. Overlays do not control the zoom levels of the map,
but can be enabled or disabled at certain scales by min/max scale/resolution
parameters so that they are only enabled at a certain level.

Some types of overlays support reprojection to the base layer projection at
layer load time. 

Most vector layers default to being overlays, as does the base Layer class.

Overlay Layers always display above base layers.

Raster Layers
-------------

Raster Layers are imagery layers. These layers are typically in a fixed
projection which can not be changed on the client side.

.. _layer.google:

Google
++++++

Layer for using Google Maps data within OpenLayers. For API information, see the `Google Layer API Docs`_. For an example of usage, see the `Spherical Mercator example`_.

If you are overlaying other data on a Google Maps base layer, you will want 
to be interacting with the Google Maps layer in projected coordinates. (This
is important if you are working with imagery data especially.) You can read
more about the 'Spherical Mercator' projection that Google Maps -- and other
commercial layers -- use in the Spherical Mercator documentation.

The Google Layer class is designed to be used only as a base layer. 

.. _`Google Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Google-js.html

.. _`Spherical Mercator example`: http://openlayers.org/dev/examples/spherical-mercator.html

.. _layer.image:

Image
+++++

For API information, see the `Image Layer API Docs`_.

.. _`Image Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Image-js.html

.. _layer.kamap:

KaMap
+++++

For API information, see the `KaMap Layer API Docs`_.

.. _`KaMap Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/KaMap-js.html

.. _layer.kamapcache:

KaMapCache
++++++++++
For API information, see the `KaMapCache Layer API Docs`_.

.. _`KaMapCache Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/KaMapCache-js.html

.. _layer.mapguide:

MapGuide
++++++++
For API information, see the `MapGuide Layer API Docs`_.

.. _`MapGuide Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/MapGuide-js.html

.. _layer.mapserver:

MapServer
+++++++++

In general, the :ref:`layer.wms` Layer is preferred over the MapServer Layer.
Since MapServer exposes most of its CGI functionality in WMS mode as well,
the WMS layer is preferred. The MapServer layer can often lead to maps which
seem to work, but don't due to projection issues or other similar
misconfigurations.

For API information, see the `MapServer Layer API Docs`_.

.. _`MapServer Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/MapServer-js.html

.. _layer.multimap:

MultiMap
++++++++
For API information, see the `MultiMap Layer API Docs`_.

.. _`MultiMap Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/MultiMap-js.html

.. _layer.tms:

TMS
+++
For API information, see the `TMS Layer API Docs`_.

.. _`TMS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/TMS-js.html

.. _layer.tilecache:

TileCache
+++++++++
For API information, see the `TileCache Layer API Docs`_.

.. _`TileCache Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/TileCache-js.html

.. _layer.virtualearth:

VirtualEarth
++++++++++++
For API information, see the `VirtualEarth Layer API Docs`_.

.. _`VirtualEarth Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/VirtualEarth-js.html

.. _layer.wms:

WMS
+++

Layer type for accessing data served according to the Web Mapping Service
standard.

For API information, see the `WMS Layer API Docs`_.

.. _`WMS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/WMS-js.html

.. _layer.worldwind:

WorldWind
+++++++++

For API information, see the `WorldWind Layer API Docs`_.

.. _`WorldWind Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/WorldWind-js.html

.. _layer.yahoo:

Yahoo
+++++

For API information, see the `Yahoo Layer API Docs`_.

.. _`Yahoo Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Yahoo-js.html


Vector Layers
-------------

Vector layers are any layers that have their source data in a format other than
imagery. This includes subclasses of both OpenLayers.Layer.Markers and 
OpenLayers.Layer.Vector layers.

.. _layer.boxes:

Boxes
+++++

Based on subclassing markers. In general, it is probably better to implement
this functionality with a Vectors layer and polygon geometries. Maintained
for backwards compatibility.

For API information, see the `Boxes Layer API Docs`_.

.. _`Boxes Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Boxes-js.html

.. _layer.gml:

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

.. _layer.georss:

GeoRSS
++++++

The GeoRSS layer uses the GeoRSS format, and displays the results as clickable
markers. It is a subclass of the Markers layer, and does not support lines
or polygons. It has many hardcoded behaviors, and in general, you may be better
off using a GML layer with a SelectFeature Control instead of the GeoRSS
layer if you want configurability of your application behavior.

For API information, see the `GeoRSS Layer API Docs`_.

.. _`GeoRSS Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/GeoRSS-js.html

.. _layer.markers:

Markers
+++++++

The Markers base layer is simple, and allows use of the addMarkers function
to add markers to the layer. It supports only points, not lines or polygons.

For API information, see the `Markers Layer API Docs`_.

.. _`Markers Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Markers-js.html

.. _layer.pointtrack:

PointTrack
++++++++++

For API information, see the `PointTrack Layer API Docs`_.

.. _`PointTrack Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/PointTrack-js.html

.. _layer.text:

Text
++++

The Text layer uses the Text format, and displays the results as clickable
markers. It is a subclass of the Markers layer, and does not support lines
or polygons. It has many hardcoded behaviors, and in general, you may be better
off using a GML layer with a SelectFeature Control instead of the Text
layer if you want configurability of your application behavior.

For API information, see the `Text Layer API Docs`_.

.. _`Text Layer API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Text-js.html

.. _layer.vector:

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

.. _layer.wfs:

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
