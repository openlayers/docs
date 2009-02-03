========
Controls
========

Controls are OpenLayers classes which affect the state of the map, or display
additional information to the user. Controls are the primary interface for
map interactions.

Default Controls
----------------

The following controls are default controls on the map:
 
* :ref:`control.argparser`
* Attribution
* Navigation
* PanZoom

Panels
------

Control panels allow collections of multiple controls together, as is common
in many applications. 

Styling Panels
++++++++++++++

Panels are styled by CSS. The "ItemActive" and "ItemInactive" are added to the 
control's displayClass.

.. add more

Controls to be used with Panels
+++++++++++++++++++++++++++++++

Panels can have controls of many 'types' inside of them. Each tool in a panel
should have a 'type' attribute which is one of:
    
* OpenLayers.Control.TYPE_TOOL (the default)
* OpenLayers.Control.TYPE_BUTTON
* OpenLayers.Control.TYPE_TOGGLE

Map Controls
------------

.. _control.argparser:

ArgParser
+++++++++

Takes URL arguments, and updates the map.

In order for the ArgParser control to work, you must check that 'getCenter()'
returns null before centering your map for the first time. Most applications
use a setCenter or zoomToMaxExtent call: this call should be avoided if the
center is already set.

.. code-block:: javascript

    var map = new OpenLayers.Map('map');
    var layer = new OpenLayers.Layer();
    map.addLayer(layer);

    // Ensure that center is not set
    if (!map.getCenter()) {
        map.setCenter(new OpenLayers.LonLat(-71, 42), 4);
    }    

The ArgParser control is enabled by default.

Attribution
+++++++++++

The attribution control will display attribution properties set on any layers
in the map in the lower right corner of the map, by default. The style and
location of this control can be overridden by overriding the
'olControlAttribution' CSS class.

Use of the attribution control is demonstrated in the `Attribution example`_.

.. _`Attribution Example`: http://openlayers.org/dev/examples/attribution.html

DragFeature
+++++++++++

DragPan
+++++++

DrawFeature
+++++++++++

EditingToolbar
++++++++++++++

KeyboardDefaults
++++++++++++++++

LayerSwitcher
+++++++++++++

Measure
+++++++

ModifyFeature
+++++++++++++

MousePosition
+++++++++++++

NavToolbar
++++++++++

Navigation
++++++++++

NavigationHistory
+++++++++++++++++

OverviewMap
+++++++++++

PanPanel
++++++++

PanZoom
+++++++

PanZoomBar
++++++++++

Permalink
+++++++++

Scale
+++++

ScaleLine
+++++++++

SelectFeature
+++++++++++++

ZoomBox
+++++++

ZoomPanel
+++++++++

Button Classes
--------------

These classes have no UI on their own, and are primarily designed to be used
inside of a control panel.

Pan
+++

Used inside the PanPanel; when triggered, causes the map to pan in a 
specific direction.

ZoomIn
++++++

Used inside the PanPanel; when triggered, causes the map to zoom in. 

ZoomOut
+++++++

Used inside the PanPanel; when triggered, causes the map to zoom out. 

ZoomToMaxExtent
+++++++++++++++

Used inside the PanPanel; when triggered, causes the map to zoomToMaxExtent. 


Generic Base Classes
--------------------

The following classes are used primarily for subclassing, and are not meant
to be used directly.

Button
++++++

Used inside of Panel controls.

Panel
+++++

Used as a base for NavToolbar and EditingToolbar controls, as well as others.
Gathers up buttons/tools to be used together.

Deprecated Controls
------------------- 

MouseDefaults
+++++++++++++

Replaced by the Navigation control.

MouseToolbar
++++++++++++

Replaced by the NavToolbar control.
