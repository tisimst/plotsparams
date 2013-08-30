plotsparams
===========

A basic S-Parameter plotting utility (with command-line functionality)

Usage
-----

This plotter takes a simplified set of inputs and creates a plot using 
`Matplotlib`_ from within the `scikit-rf`_ package.

If using this as a python import, then the function has the following 
construct::

    plotsparams(filename, n, m, scale, title)

where,

filename : str
    Any valid ``.s?p`` file name.
n : int (or None)
    The output port number (zero-based, thus n=0 for S1,?), defaults to all
m : int (or None)
    The input port number (zero-based, thus m=0 for S?,1), defaults to all
scale : str
    Valid options are "db" (Default), "mag", "re", "im".
title : str
    An optional, custom plot title, defaults to None

If using at the command-line, the following syntax is available::

    > plotsparams [OPTIONS]
    
    Valid Options:
      -i            Input ".s?p" file name
      -n            Output port number (zero-based)
      -m            Input port number (zero-based)
      -s, --scale   Plot scale, "db", "mag", "re", "im"
      -t, --title   Plot title
      -h, --help    Display this help and exit

For the time being, these are the only options that will be implemented, since it's
intended to be a simple plotter and nothing more (or fancier).

Examples
--------

Usage in python might go something like this::

    filename = 'filter.s2p'
    inport = 0
    output = 1
    scale = 'db'
    title = 'Filter $S_{2 1}$'
    
    plotsparams(filename, outport, inport, scale, title)

Usage at the command-line might go something like this::

    $ python plotsparams.py -i "filter.s2p" -n 0 -m 0 -s "mag" -t "my cool filter"
    
Requires
--------

- `Matplotlib`_ : the de-facto plotting library for python
- `scikit-rf`_ : an object-oriented approach to RF/Microwave engineering 
  implemented in the Python programming language.

Contact
-------

Any questions, bug-reports, etc. can be forwarded to the author: `Abraham Lee`_


.. _Matplotlib: http://matplotlib.org/
.. _scikit-rf: http://scikit-rf.org/
.. _Abraham Lee: mailto:tisimst@gmail.com
