Introduction
============

.. image:: https://readthedocs.org/projects/sparkfun-circuitpython-qwiicjoystick/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/qwiicjoystick/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/fourstix/Sparkfun_CircuitPython_QwiicJoystick.svg?branch=master
    :target: https://travis-ci.com/fourstix/Sparkfun_CircuitPython_QwiicJoystick
    :alt: Build Status

CircuitPython library for Sparkfun Qwiic Joystick

.. image:: https://cdn.sparkfun.com/assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg
    :target: https://www.sparkfun.com/products/15168
    :alt: SparkFun Qwiic Joystick (DEV-15168)
SparkFun Qwiic Joystick (DEV-15168)

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!
.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/sparkfun-circuitpython-qwiicjoystick/>`_. To install for current user:

.. code-block:: shell

    pip3 install sparkfun-circuitpython-qwiicjoystick

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install sparkfun-circuitpython-qwiicjoystick

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install sparkfun-circuitpython-qwiicjoystick

Usage Example
=============

* `Qwiic Joystick Hookup Guide <https://learn.sparkfun.com/tutorials/qwiic-joystick-hoookup-guide>' - Hookup guide for the Qwiic Joystick
* `CircuitPython on a Raspberry Pi <https://learn.adafruit.com/circuitpython-on-raspberrypi-linux> - Basic information on how to install CircuitPython on a Raspberry Pi.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/fourstix/Sparkfun_CircuitPython_QwiicJoystick/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix sparkfun-circuitpython-qwiicjoystick --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
