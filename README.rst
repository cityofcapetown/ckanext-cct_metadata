.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/cityofcapetown/ckanext-cct_metadata.svg?branch=master
    :target: https://travis-ci.org/cityofcapetown/ckanext-cct_metadata

.. image:: https://coveralls.io/repos/cityofcapetown/ckanext-cct_metadata/badge.svg
  :target: https://coveralls.io/r/cityofcapetown/ckanext-cct_metadata

====================
ckanext-cct_metadata
====================

Applies City of Cape Town metadata standard. Canonical record stored `here <http://teamsites.capetown.gov.za/sites/DataStrategy/_layouts/15/WopiFrame2.aspx?sourcedoc={ED0AD300-FE87-4504-8AD1-AAE19FBC607C}&file=MetadataFields_Descriptors.xlsx&action=default>`_

Uses `custom scheming extension <https://github.com/ckan/ckanext-scheming>`_ to actually implement the schema.

------------
Requirements
------------

ckan==2.8.3

ckanext_scheming==1.2.0

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-cct_metadata:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-cct_metadata Python package into your virtual environment::

     pip install ckanext-cct_metadata

3. Add ``cct_metadata`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.cct_metadata.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-cct_metadata for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/cityofcapetown/ckanext-cct_metadata.git
    cd ckanext-cct_metadata
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------
**NB** I've swapped out nose tests for the built-in unit test framework.

To run the tests, do::

    PYTHONPATH=. python -m unittest tests/test_plugin.py
