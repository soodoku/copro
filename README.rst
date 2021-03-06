===============
Overview
===============

CoPro
----------------

Welcome to CoPro, a machine-learning tool for conflict risk projections based on climate, environmental, and societal drivers.

.. image:: https://travis-ci.com/JannisHoch/copro.svg?branch=dev
    :target: https://travis-ci.com/JannisHoch/copro

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://github.com/JannisHoch/copro/blob/dev/LICENSE

.. image:: https://readthedocs.org/projects/copro/badge/?version=latest
    :target: https://copro.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/github/v/release/JannisHoch/copro
    :target: https://github.com/JannisHoch/copro/releases/tag/v0.0.5-pre

.. image:: https://zenodo.org/badge/254407279.svg
    :target: https://zenodo.org/badge/latestdoi/254407279

.. image:: https://badges.frapsoft.com/os/v2/open-source.svg?v=103
    :target: https://github.com/ellerbrock/open-source-badges/

Installation
----------------

To install copro, first clone the code from GitHub. It is advised to create an individual python environment first. 
You can then install the model package into this environment.

.. code-block:: console

    $ git clone https://github.com/JannisHoch/copro.git
    $ cd path/to/copro
    $ conda env create -f environment.yml
    $ conda activate copro
    $ python setup.py develop

Execution
----------------

To be able to run the model, the conda environment has to be activated first.

.. code-block:: console

    $ conda activate copro

Example notebook
^^^^^^^^^^^^^^^^^^

There are jupyter notebooks available to guide you through the model application process.
They can all be run and converted to htmls by executing the provided shell-script.

.. code-block:: console

    $ cd path/to/copro/example
    $ sh run.sh

It is of course also possible to execute the notebook cell by cell using jupyter notebook.

Runner script
^^^^^^^^^^^^^^^^^^

To run the model from command line, a command line script is provided. 
All data and settings are retrieved from the settings-file which needs to be provided as inline argument.

There are two settings-files, one for evaluating the model for the reference situation, and another one for additionally making projections.
To make a projection, both files need to be specified with the latter requiring the -proj flag.

.. code-block:: console

    $ cd path/to/copro/scripts
    $ python runner.py ../example/example_settings.cfg
    $ python runner.py ../example/example_settings.cfg -proj ../example/example_settings_proj.cfg

By default, output is stored to the output directory specified in the specific settings-file. 

Documentation
---------------

Model documentation including model API can be found at http://copro.rtfd.io/

Code of conduct and Contributing
---------------------------------

Please find the relevant information on our Code of Conduct and how to contribute to this package in the relevant files.

Authors
----------------

* Jannis M. Hoch (Utrecht University)
* Sophie de Bruin (Utrecht University, PBL)
* Niko Wanders (Utrecht University)

Corrosponding author: Jannis M. Hoch (j.m.hoch@uu.nl)
