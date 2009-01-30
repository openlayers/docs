Deploying
=========

OpenLayers comes with pre-configured examples out of the box: simply download
a release of OpenLayers, and you get a full set of easy to use examples.
However, these examples are designed to be used for development. When you're
ready to deploy your application, you want a highly optimized OpenLayers
distribution, to limit bandwidth and loading time.

Single File Build
+++++++++++++++++

OpenLayers has two different types of usage: Single File, where all Javascript
code is compiled into a single file, OpenLayers.js, and the development
version, where Javascript files are all loaded at application start time.  The
single file build takes a set of OpenLayers Javascript files, orders them
according to dependancies described in the files, and compresses the resulting
file, using the jsmin compression library.

Building a single file version of the OpenLayers library changes the behavior
of the library slightly: by default, the development version of OpenLayers
expects to live in a directory called "lib", and expects that images and
CSS live in the directory above the OpenLayers.js file::

  img/pan-hand.png
  theme/default/style.css
  lib/OpenLayers.js
  lib/OpenLayers/Map.js
  ...

However, when deploying a single file build of OpenLayers, it is expected that
the library will instead be at the same level as the theme and img
directories:: 

  OpenLayers.js
  theme/default/style.css
  img/pan-hand.png
  ...

Building the Single File Build
------------------------------

The single file build tools are deployed with an OpenLayers release in the 
'build' directory. The tools require Python in order to build.

On Linux and other similar operating systems, given that OpenLayers is stored
in the 'openlayers' directory, a single file build could be created by
issuing the following commands:: 

  cd openlayers/build
  ./build.py  

This would create a file in the build directory called "OpenLayers.js", which
contains all the library code for your single file build of OpenLayers.

In Windows, from the Start Menu, select Run. Copy the path to build.py from the address bar of the Explorer Window into the text box and then add the name of the configuration file (or blank for the default):

 C:\Downloads\OpenLayers-2.6\build\build.py lite

Custom Build Profiles
+++++++++++++++++++++

In order to optimize the end-user's experience, the OpenLayers distribution
includes tools which allow you to build your own single file version of the
code. This code uses a configuration file to choose which files should be
included in the build: In this way, for production use, you can remove classes
from your OpenLayers JavaScript library file which are not used in your
application.

OpenLayers ships with two standard configurations to create a single file
version:

    full: 
        This is the full build with all files.
    lite: 
        This file includes a small subset of OpenLayers code, designed to be
        integrated into another application. It includes only the Layer types
        neccesary to create tiled or untiled WMS, and does not include any
        Controls. This is the result of what was at the time called "Webmap.js"
        at the FOSS4G 2006 Web Mapping BOF.

Profiles are simple to create. You can start by copying library.cfg or lite.cfg
to something else, e.g. myversion.cfg in the build directory.

The start of any build profile must include the same [first] section used in
the lite.cfg file::

  [first]
  OpenLayers/SingleFile.js
  OpenLayers.js
  OpenLayers/BaseTypes.js
  OpenLayers/BaseTypes/Class.js
  OpenLayers/Util.js

These files are required for the OpenLayers build to function.

Once you have included these files, you should add more files to the 
'[include]' section of the file. The files listed here should be the list of
files containing any class you use in your application. You can typically find
these classes by looking through your code for any cases where 'new
OpenLayers.ClassName()' is used.

Taking the 'lite.html' example, we see that there are two 'new' statements in
the file: one for the OpenLayers.Map class, and one for the
OpenLayers.Layer.WMS class. We then add the corresponding files to our include
section::

  [include]
  OpenLayers/Map.js
  OpenLayers/Layer/WMS.js

Once we have done that, we can build our profile by adding the profile name
to the end of our ealier build command::

  ./build.py myversion 

This will create a much smaller OpenLayers version, suitable for limited
applications.

Almost all applications can benefit from a custom build profile. OpenLayers
supports many different layer types, but most applications will only use one
or two, and many applications do not need the full support of many of the
features in OpenLayers. In order to limit your download time and library
size, building a custom profile is highly recommended before deploying an
OpenLayers application: it can help shrink the size of your library by a 
factor of five over using the full library.

Deploying Files
+++++++++++++++

In order to deploy OpenLayers, there are several different pieces that must
be deployed.

  OpenLayers.js
    The library. This provides the JavaScript code for your application to
    use.

  theme directory
    The theme directory contains CSS and image files for newer controls,
    whose styling and positioning is controlled entirely by CSS.

  img directory
    This directory provides images to be used for some controls, like the 
    PanZoom control, which do not use CSS for styling.

As described above, when deploying these files with a single file OpenLayers
build, they should all live in the same directory: this allows OpenLayers
to properly find and include them.
