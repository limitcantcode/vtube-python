Getting Started
===============

This guide will help you get started with vtube-python (vtpy). You'll learn how to install the library, establish a connection to VTube Studio, and perform basic operations.

Installation
------------

Install from PyPI
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install vtube-python

Install from Repository
~~~~~~~~~~~~~~~~~~~~~~~

To install directly from the repository:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/limitcantcode/vtube-python.git
   cd vtube-python

   # Install in development mode
   pip install -e .

   # Or install normally
   pip install .

For development with all optional dependencies:

.. code-block:: bash

   pip install -e ".[dev]"

Prerequisites
-------------

Before using vtpy, make sure you have:

1. **VTube Studio** installed and running
2. **WebSocket API enabled** in VTube Studio settings
3. **Python 3.8+** installed

To enable the WebSocket API in VTube Studio:

1. Open VTube Studio
2. Go to Settings → API
3. Enable "Enable API Server"
4. Note the port (default is 8001)

Basic Connection
----------------

The first step is to create a VTS client and connect to VTube Studio:

.. code-block:: python

   import asyncio
   from vtpy import VTS

   async def main():
       # Initialize VTS client
       vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
       
       try:
           # Connect to VTube Studio
           auth_token = await vts.start(
               host="localhost",
               port=8001,
               save_auth_token=False
           )
           print(f"Connected! Auth token: {auth_token[:20]}...")
           
       except ConnectionError as e:
           print(f"Connection error: {e}")
       finally:
           if vts.connected:
               await vts.close()

   asyncio.run(main())

Authentication
--------------

VTube Studio requires authentication for API access. The ``start()`` method handles this automatically:

- If you don't have an auth token, it will request one from VTube Studio
- You'll need to approve the authentication request in VTube Studio
- The token can be saved for future use (set ``save_auth_token=True``)

.. code-block:: python

   # First time - request authentication
   auth_token = await vts.start(
       host="localhost",
       port=8001,
       save_auth_token=True  # Save token for next time
       auth_file="vts_token.txt"  # Save location of existing or new token
   )

   # Subsequent connections - use in-memory token
   auth_token = await vts.start(
       host="localhost",
       port=8001,
       auth_token=auth_token
   )

   # Subsequent connections - use saved token
   auth_token = await vts.start(
       host="localhost",
       port=8001,
       auth_file="vts_token.txt"
   )

Making Requests
---------------

Once connected, you can make API requests. Here's an example of getting VTube Studio statistics:

.. code-block:: python

   from vtpy.data.requests import StatisticsRequestData

   # Request statistics
   stats_response = await vts.request_statistics(StatisticsRequestData())
   stats = stats_response.data
   
   print(f"Version: {stats.vTubeStudioVersion}")
   print(f"Framerate: {stats.framerate} FPS")
   print(f"Uptime: {stats.uptime} seconds")

Handling Events
---------------

vtpy supports event-driven programming. You can subscribe to VTube Studio events:

.. code-block:: python

   from vtpy.data.events import (
       EventType,
       ModelMovedEvent,
       ModelMovedEventSubscriptionRequestData,
       ModelMovedEventSubscriptionRequestConfig,
   )

   # Define event handler
   async def on_model_moved(event: ModelMovedEvent) -> None:
       print(f"Model moved: {event.data.modelName}")

   # Register handler
   vts.on_event(EventType.ModelMovedEvent, on_model_moved)

   # Subscribe to events
   await vts.event_sub_model_moved(
       ModelMovedEventSubscriptionRequestData(
           subscribe=True,
           config=ModelMovedEventSubscriptionRequestConfig()
       )
   )

Error Handling
--------------

vtpy provides specific exception types for better error handling:

.. code-block:: python

   from vtpy.error import VTSRequestError

   try:
       await vts.request_statistics(StatisticsRequestData())
   except VTSRequestError as e:
       print(f"VTube Studio error: {e.message}")
       print(f"Error ID: {e.error_id}")
   except ConnectionError as e:
       print(f"Connection error: {e}")

Next Steps
----------

- Read the :doc:`guides/index` for common use cases
- Explore the :doc:`api/index` for complete API reference
- Check out :doc:`examples/index` for code examples
- See the `VTube Studio API Documentation <https://github.com/DenchiSoft/VTubeStudio>`_ for API details

