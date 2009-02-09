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

.. _control.attribution:

Attribution
+++++++++++

The attribution control will display attribution properties set on any layers
in the map in the lower right corner of the map, by default. The style and
location of this control can be overridden by overriding the
'olControlAttribution' CSS class. 

Use of the attribution control is demonstrated in the `Attribution example`_.
For API information, see the `Attribution API Docs`_.

.. _`Attribution Example`: http://openlayers.org/dev/examples/attribution.html

.. _`Attribution API Docs`: http://dev.openlayers.org/apidocs/files/OpenLayers/Control/Attribution-js.html

.. _control.dragfeature:

DragFeature
+++++++++++

.. _control.dragpan:

DragPan
+++++++

The DragPan control implements map dragging interactions. 

.. _control.drawfeature:

DrawFeature
+++++++++++

.. _control.editingtoolbar:

EditingToolbar
++++++++++++++

.. _control.keyboarddefaults:

KeyboardDefaults
++++++++++++++++

.. _control.layerswitcher:

LayerSwitcher
+++++++++++++

.. _control.measure:

Measure
+++++++

A planar distance measuring tool.

.. _control.modifyfeature:

ModifyFeature
+++++++++++++

The ModifyFeature control can be used to edit an existing vector object.

This control causes three different types of events to fire on the layer:
* beforefeaturemodified - triggered when a user selects the feature to begin editing. 
* featuremodified - triggered when a user changes something about the feature.
* afterfeaturemodified - triggered after the user unselects the feature.

To register for one of these events, register on the layer:

.. code-block:: javascript

  var layer = new OpenLayers.Layer.Vector("");
  layer.events.on({
    'beforefeaturemodified': function(evt) {
        console.log("Selected " + evt.feature.id  + " for modification");
    },    
    'afterfeaturemodified': function(evt) {
        console.log("Finished with " + evt.feature.id);
    }
  });  

There are several different modes that the ModifyFeature control can work in.
These can be combined to work together.

* RESHAPE -- The default. Allos changing the vertices of a feature by dragging existing vertices, creating new vertices by dragging 'virtual vertices', or deleting vertices by hovering over a vertice and pressing the delete key.
* RESIZE -- Allows changing the size of a geometry.
* ROTATE -- change the orientation of the geometry
* DRAG -- change the position of the geometry.

When creating the control, you can use a bitwise OR to combine these:

.. code-block:: javascript

  var modifyFeature = new OpenLayers.Control.ModifyFeature(layer, {
    mode: OpenLayers.Control.ModifyFeature.RESIZE | OpenLayers.Control.ModifyFeature.DRAG
  });  

For an example of using the ModifyFeature control, see the `ModifyFeature
example`_. For API information, see the `ModifyFeature API Documentation`_.

The ModifyFeature control can only be used with a single layer at any given
time. To modify multiple layers, use multiple ModifyFeature controls. 

Deprecation Warning
@@@@@@@@@@@@@@@@@@@

As of OpenLayers 2.6, the onModificationStart, onModification and
onModificationEnd functions on this control are no longer the recommended way
to receive modification events. Instead, use the beforefeaturemodified,
featuremodified, and afterfeaturemodified events to handle these cases.

.. _`ModifyFeature API Documentation`: http://dev.openlayers.org/apidocs/files/OpenLayers/Control/ModifyFeature-js.html 
.. _`ModifyFeature example`: http://openlayers.org/dev/examples/modify-feature.html

.. _control.mouseposition:

MousePosition
+++++++++++++

.. _control.navtoolbar:

NavToolbar
++++++++++

.. _control.navigation:

Navigation
++++++++++

The replacement control for the former :ref:`control.mousedefaults` control. 
This control is a combination of:

* :ref:`control.dragpan`
* :ref:`control.zoombox`
* Handler.Click, for double click zooming
* Handler.Wheel, for wheel zooming

The most common request for the Navigation control is to disable wheel 
zooming when using the control. To do this, ensure that no other navigation
controls are added to your map -- for example, by an
:ref:`control.editingtoolbar` -- and call disableWheelNavigation on the 
Navigation control.


NavigationHistory
+++++++++++++++++

OverviewMap
+++++++++++

.. _control.panpanel:

PanPanel
++++++++
A set of visual buttons for controlling the location of the map. A subclass
of Control.Panel, this is easily controlled by styling via CSS. The
``.olControlPanPanel`` class, and its internal divs, control the styling of  
the PanPanel. If you wish to customize the look and feel of the controls
in the upper left corner of the map, this control is the one for you.

This control is designed to work with the :ref:`control.zoompanel` control
to replicate the functionality of the :ref:`control.panzoom` control.

.. _control.panzoom:

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

.. _control.zoombox:

ZoomBox
+++++++

.. _control.zoompanel:

ZoomPanel
+++++++++

A set of visual buttons for controlling the zoom of the map. A subclass
of Control.Panel, this is easily controlled by styling via CSS. The
``.olControlZoomPanel`` class, and its internal divs, control the styling of  
the PanPanel. If you wish to customize the look and feel of the controls
in the upper left corner of the map, this control is the one for you.

This control is designed to work with the :ref:`control.panpanel` control
to replicate the functionality of the :ref:`control.panzoom` control.

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

.. _control.mousedefaults:

MouseDefaults
+++++++++++++

Replaced by the :ref:`control.navigation` control.

MouseToolbar
++++++++++++

Replaced by the :ref:`control.navtoolbar` control.
