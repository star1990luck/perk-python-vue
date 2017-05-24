=============================
Python and Vue.js gule
=============================
.. image:: https://img.shields.io/pypi/v/python_vuejs.svg
        :target: https://pypi.python.org/pypi/python_vuejs

.. image:: https://pyup.io/repos/github/cstrap/python_vuejs/shield.svg
     :target: https://pyup.io/repos/github/cstrap/python-vuejs/
     :alt: Updates

Gluing Python and `Vue.js <https://vuejs.org/>`_ with a set of scripts that automate the dev and build process.

Projects aims to be agnostic, just use it in order to automate the boring stuff to setup a Vue.js project.

The point is: you start with SPA app inside your current project and then, extract it without having the dependency with backend framework. 

Feel free to contribute with PRs and opening issues.

Thanks!
Cheers! 🍻

* Free software: MIT license
* Documentation: https://pythonhosted.org/python_vuejs.

------------------
Requirements
------------------

* Python 2.7+ or 3.4+
* nodejs > 5 and npm > 3

------------------
Commands reference
------------------

Vue.js
------

+-----------------+-----------------------------------------------------+
| Command         | Description                                         |
+=================+=====================================================+ 
| ``checkenv``    | Check if ``node`` > 5 and ``npm`` > 3 are installed |
+-----------------+-----------------------------------------------------+
| ``vuecli``      | Install vue-cli                                     |
+-----------------+-----------------------------------------------------+
| ``startvueapp`` | Init Vue.js project via vue-cli                     |
+-----------------+-----------------------------------------------------+
| ``vuedev``      | Start frontend dev server                           |
+-----------------+-----------------------------------------------------+
| ``vuebuild``    | Build Vue.js project via ``npm``                    |
+-----------------+-----------------------------------------------------+

Django
------

+-------------+------------------------------------------------+
| Command     | Description                                    |
+=============+================================================+                            
| ``djvue``   | Make Vue.js project into a django app          |
+-------------+------------------------------------------------+
| ``djbuild`` | Inject into the django way into ``index.html`` |
+-------------+------------------------------------------------+

Flask
-----

* TODO

+---------+----------------------------------------------+
| Command | Description                                  |
+=========+==============================================+  
| WIP     | WIP                                          |
+---------+----------------------------------------------+

--------
Features
--------

* Vue.js starter via vue-cli
* Basic integration with django 

TODO
----

* Supporting flask, eg https://github.com/taogeT/flask-vue (without js inside package)
* Supporting other frameworks
* Some tests 

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

