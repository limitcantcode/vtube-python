Connection Guide
=================

This guide covers how to establish and manage connections to VTube Studio.

Establishing a Connection
--------------------------

The ``VTS`` class manages the WebSocket connection to VTube Studio. To connect:

.. code-block:: python

   from vtpy import VTS

   vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
   await vts.start(host="localhost", port=8001)

Connection Parameters
---------------------

The ``start()`` method accepts several parameters:

- **host** (str): VTube Studio host address (default: "localhost")
- **port** (int): VTube Studio WebSocket port (default: 8001)
- **auth_token** (Optional[str]): Authentication token for reconnection (default: None)
- **auth_file** (Union[str, Path]): Path to the file to save/load the auth token (default: "vts_token.txt")
- **save_auth_token** (bool): Whether to save the auth token to disk (default: True)

Checking Connection Status
---------------------------

You can check if the client is connected and authenticated:

.. code-block:: python

   if vts.connected:
       print("Connected to VTube Studio")
   
   if vts.authenticated:
       print("Authenticated with VTube Studio")

Closing the Connection
----------------------

Always close the connection when done:

.. code-block:: python

   if vts.connected:
       await vts.close()

It's recommended to use a try/finally block:

.. code-block:: python

   try:
       await vts.start(host="localhost", port=8001)
       # Your code here
   finally:
       if vts.connected:
           await vts.close()

Reconnection
------------

If the connection is lost, you can reconnect:

.. code-block:: python

   if not vts.connected:
       await vts.start(
           host="localhost",
           port=8001,
           auth_token=previous_token  # Use saved token
       )

Connection Errors
-----------------

Common connection errors:

- **ConnectionError**: VTube Studio is not running or WebSocket API is disabled
- **ValueError**: Authentication failed or was rejected
- **TimeoutError**: Connection timeout

Handle these appropriately:

.. code-block:: python

   try:
       await vts.start(host="localhost", port=8001)
   except ConnectionError as e:
       print("Could not connect to VTube Studio")
       print("Make sure VTube Studio is running and API is enabled")
   except ValueError as e:
       print("Authentication failed")
       print("Approve the request in VTube Studio")

