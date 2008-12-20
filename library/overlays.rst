OpenLayers Feature Overlays
===========================

OpenLayers is a pure JavaScript library for displaying map data in most
modern web browsers, with no server-side dependencies. OpenLayers implements a
`JavaScript API`_ for building rich web-based geographic applications, similar
to the Google Maps and MSN Virtual Earth APIs, with one important difference --
OpenLayers is Free Software, developed for and by the Open Source software
community.

.. _Javascript API: http://trac.openlayers.org/wiki/Documentation

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
there are some things you can not do with vectors as they are current
implemented, and they provide a different type of interface for event
registration. 
