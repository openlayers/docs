OpenLayers Feature Overlays
===========================

OpenLayers allows you to lay many different types of data on top of its various
data sources. Currently, there are two main ways of displaying vector feature
overlays in OpenLayers, each with benefits and drawbacks. This document seeks
to describe the differences, and ways in which each can be used.

Overlay Basics
++++++++++++++

There are two different types of feature rendering in OpenLayers.  One type is
the OpenLayers "Vector Layer" support, which uses vector drawing capabilities
in the browser (SVG, VML, or Canvas) to display data. The other type is the
OpenLayers "Marker Layer" support. This type of layer displays HTML image
objects inside the DOM.

In general, the Vector layer provides more capabilities, with the ability to
draw lines, polygons, and more. The Vector-based Layers are better maintained,
and are the place where most new OpenLayers development is taking place.
There is more support for various styling options, and more configurability
over layer behavior and interactions with remote servers.

However, the Markers layer is maintained for backwards compatibility, because
there are some things you can not do with vectors as they are currently
implemented, and they provide a different type of interface for event
registration. 

Vector Overlays
---------------

Vector Layers form the core of Vector overlays. Vector overlays are powered
by adding sets of OpenLayers.Feature.Vectors to the map. These can be a number
of types of geometry:
 
  * Point / MultiPoint
  * Line / MultiLine
  * Polygon / MultiPolygon

They are styled using the OpenLayers.Style / OpenLayers.StyleMap properties.

.. _`StyleMap Example`: http://openlayers.org/dev/examples/stylemap.html
.. _`Context Example`: http://openlayers.org/dev/examples/styles-context.html
.. _`Rotation Example`: http://openlayers.org/dev/examples/styles-rotation.html
.. _`Unique Value Style Example`: http://openlayers.org/dev/examples/styles-unique.html

Examples: 
 
 * `StyleMap Example`_: 
     Use "Rules" to determine style attributes based on feature properties.
     This is useful for rendering based on data attributes like population. 

 * `Context Example`_: 
     Use a custom Javascript function to determine feature
     style properties. This example shows how to use which quadrant of the
     world a feature is in to determine its color. Similar rules can be
     used to do computations on a feature property to generate a style value
     (like size).

 * `Rotation Example`_: 
     Vector features support advanced styling, like feature rotation. This can
     be used, for example, to display vehicle direction, wind direction, or
     other direction-based attributes.

 * `Unique Value Style Example`_: 
     A common use case is to pick a specific style value based on a key/value
     mapping of a feature. This example demonstrates how to do that.

Marker Overlays
---------------

Markers support only point geometries. They are styled only using the
OpenLayers.Icon class. They do not support anything other than point
geometries.

