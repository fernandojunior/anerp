===============================
anerp
===============================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://github.com/fernandojunior/anerp/blob/master/LICENSE

.. image:: https://img.shields.io/travis/fernandojunior/anerp.svg
        :target: https://travis-ci.org/fernandojunior/anerp

.. image:: https://img.shields.io/codecov/c/github/fernandojunior/anerp.svg
        :target: https://codecov.io/github/fernandojunior/anerp


An ERP

* Free software: MIT license
* Documentation: https://anerp.readthedocs.org.

Features
--------

* TODO

Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export ANERP_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::
    sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    git clone https://github.com/fernandojunior/anerp
    cd anerp
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen (http://127.0.0.1:5000/public/).

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``ANERP_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::
To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
