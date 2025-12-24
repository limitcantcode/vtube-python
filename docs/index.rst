vtube-python Documentation
==========================

vtube-python (vtpy) is a Python library for interfacing with VTube Studio's WebSocket API. VTube Studio is a desktop application that allows users to control Live2D avatars using face tracking.

Features
--------

- 🚀 **Async/Await Support**: Built with Python's ``asyncio`` for efficient asynchronous operations
- 🔌 **WebSocket Communication**: Direct WebSocket connection to VTube Studio
- 🎭 **Event-Driven**: Subscribe to and handle VTube Studio events in real-time
- 📦 **Type Hints**: Full type hint support for better IDE integration
- 🛡️ **Error Handling**: Comprehensive error handling with clear, actionable messages

Quick Start
-----------

.. code-block:: python

   import asyncio
   from vtpy import VTS
   from vtpy.data.requests import StatisticsRequestData

   async def main():
       vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
       await vts.start(host="localhost", port=8001)
       
       stats = await vts.request_statistics(StatisticsRequestData())
       print(f"VTube Studio Version: {stats.data.vTubeStudioVersion}")
       
       await vts.close()

   asyncio.run(main())

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   guides/index
   api/index
   examples/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

