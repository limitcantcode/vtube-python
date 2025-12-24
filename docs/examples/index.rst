Examples
========

This section contains code examples demonstrating various features of vtpy.

Basic Examples
--------------

.. toctree::
   :maxdepth: 1

   basic_usage
   events_usage

Basic Usage
-----------

The basic usage example demonstrates:

- Connecting to VTube Studio
- Authenticating
- Retrieving statistics
- Error handling

See :doc:`basic_usage` for the complete example.

Events Usage
------------

The events usage example demonstrates:

- Registering event handlers
- Subscribing to events
- Handling model movement events

See :doc:`events_usage` for the complete example.

Running Examples
----------------

To run the examples:

1. Make sure VTube Studio is running with the WebSocket API enabled
2. Install the package (see :doc:`../getting_started`)
3. Run any example:

.. code-block:: bash

   python examples/basic_usage.py
   python examples/events_usage.py

Additional Examples
-------------------

For more examples, check the `examples/` directory in the repository:

- ``basic_usage.py`` - Basic connection and statistics
- ``events_usage.py`` - Event handling

