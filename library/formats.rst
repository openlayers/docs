=======
Formats
=======

Formats are classes that parse different sources of data into OpenLayers 
internal objects. Most (but not all) formats are centered around reading data
from an XML DOM or a string and converting them to OpenLayers.Feature.Vector
objects.

.. _format.kml:

KML
---

The KML format reads KML data and returns an array of OpenLayers.Feature.Vector
objects. 

The KML parser supports parsing local and remote styles. 

The KML parser supports fetching network links.

For fetching remoteData, the maxDepth option must be greater than 0. This
option tells the KML parser how far the traverse before giving up. 

.. #1796, #1877

*Note*: Prior to OpenLayers 2.8, the maxDepth option was broken. No setting in
the KML format would cause it to fetch network links or remote styles. 
