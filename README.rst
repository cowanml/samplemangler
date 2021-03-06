===============================
sampleMangler
===============================

Adapter layer between sampleManager and legacy api.


master:  |tci| |cvrg| |qual| |docs|

.. |tci| image:: https://travis-ci.org/cowanml/sampleMangler.svg?branch=master
    :alt: Travis-CI Build Status - master
    :target: https://travis-ci.org/cowanml/sampleMangler/branches


.. |cvrg| image:: https://coveralls.io/repos/cowanml/sampleMangler/badge.png?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/r/cowanml/sampleMangler?branch=master


.. |qual| image:: https://landscape.io/github/cowanml/sampleMangler/master/landscape.svg
    :alt: Code Quality Status
    :target: https://landscape.io/github/cowanml/sampleMangler/master


.. |docs| image:: https://readthedocs.org/projects/samplemangler/badge/?version=latest
    :alt: Documentation Status
    :target: http://samplemangler.readthedocs.org/en/latest


dev:  |tcidev| |cvrgdev| |qualdev| |docsdev|

.. |tcidev| image:: https://travis-ci.org/cowanml/sampleMangler.svg?branch=dev
    :alt: Travis-CI Build Status - dev
    :target: https://travis-ci.org/cowanml/sampleMangler/branches


.. |cvrgdev| image:: https://coveralls.io/repos/cowanml/sampleMangler/badge.png?branch=dev
    :alt: Coverage Status
    :target: https://coveralls.io/r/cowanml/sampleMangler?branch=dev


.. |qualdev| image:: https://landscape.io/github/cowanml/sampleMangler/dev/landscape.svg
    :alt: Code Quality Status
    :target: https://landscape.io/github/cowanml/sampleMangler/dev


.. |docsdev| image:: https://readthedocs.org/projects/samplemangler/badge/?version=dev
    :alt: Documentation Status
    :target: http://samplemangler.readthedocs.org/en/dev



Installation
============

Can't *pip* these yet :(


1st, get sampleManager::

    git clone https://github.com/NSLS-II/sampleManager.git
    cd sampleManager
    python setup.py build && su -c python setup.py install


then sampleMangler::

    git clone https://github.com/cowanml/sampleMangler.git
    cd sampleMangler
    python setup.py build && su -c python setup.py install

    ...eventually just...?
    pip install sampleMangler

Documentation
=============

https://samplemangler.readthedocs.org/


Development
===========

Use `gitflow <https://github.com/nvie/gitflow#readme>`_.


To run tests::

    tox -e pep8
    tox -e flake8
    tox -e 2.7
    ...
