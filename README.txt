============
  AGDISTIS Py
============

Python bindings for AGDISTIS web service: http://agdistis.aksw.org/demo/ 

Usage
=========

In [1]: from agdistispy.agdistis import Agdistis
In [2]: ag = Agdistis()
In [3]: ag.disambiguate("<entity>Austria</entity>")
Out[3]: 
[{u'disambiguatedURL': u'http://dbpedia.org/resource/Austria',
  u'namedEntity': u'Austria',
    u'offset': 7,
      u'start': 0}]

Contributors
=========

* Ivan Ermilov (AKSW/BIS University of Leipzig)

Notes
=========

The source code is available from:
https://github.com/earthquakesan/agdistispy
