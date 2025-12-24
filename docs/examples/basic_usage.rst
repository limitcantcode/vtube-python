Basic Usage Example
===================

This example demonstrates the basic usage of vtpy: connecting to VTube Studio, authenticating, and retrieving statistics.

Full Code
---------

.. literalinclude:: ../../examples/basic_usage.py
   :language: python
   :linenos:

Explanation
-----------

1. **Import Required Modules**

   .. code-block:: python

      import asyncio
      from vtpy import VTS
      from vtpy.data.requests import StatisticsRequestData
      from vtpy.error import VTSRequestError

2. **Initialize VTS Client**

   .. code-block:: python

      vts = VTS(plugin_name="ExamplePlugin", plugin_developer="ExampleDeveloper")

   The ``VTS`` class is the main interface for interacting with VTube Studio.

3. **Connect and Authenticate**

   .. code-block:: python

      auth_token = await vts.start(host="localhost", port=8001, save_auth_token=False)

   The ``start()`` method:
   - Connects to VTube Studio via WebSocket
   - Handles authentication automatically
   - Returns the authentication token

4. **Make API Requests**

   .. code-block:: python

      stats_response = await vts.request_statistics(StatisticsRequestData())
      stats = stats_response.data

   Request statistics from VTube Studio and access the response data.

5. **Error Handling**

   The example handles various error types:
   - ``ConnectionError``: Connection issues
   - ``ValueError``: Authentication failures
   - ``VTSRequestError``: API request errors

6. **Cleanup**

   .. code-block:: python

      if vts.connected:
          await vts.close()

   Always close the connection when done.

Expected Output
---------------

When run successfully, you should see output like:

.. code-block:: text

   Connecting to VTube Studio at localhost:8001...
   Successfully authenticated! Token: abc123def456...
   
   Requesting VTube Studio statistics...
   
   === VTube Studio Statistics ===
   Version: 1.x.x
   Uptime: 1234 seconds
   Framerate: 60 FPS
   Allowed Plugins: 10
   Connected Plugins: 1
   Started with Steam: False
   Window Size: 1920x1080
   Fullscreen: False
   
   Closing connection...
   Disconnected.

