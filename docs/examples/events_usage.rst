Events Usage Example
=====================

This example demonstrates how to subscribe to and handle VTube Studio events, specifically model movement events.

Full Code
---------

.. literalinclude:: ../../examples/events_usage.py
   :language: python
   :linenos:

Explanation
-----------

1. **Import Required Modules**

   .. code-block:: python

      from vtpy.data.events import (
          EventType,
          ModelMovedEvent,
          ModelMovedEventSubscriptionRequestData,
          ModelMovedEventSubscriptionRequestConfig,
      )

2. **Define Event Handler**

   .. code-block:: python

      async def on_model_moved(event: ModelMovedEvent) -> None:
          """Handle model moved events."""
          data = event.data
          position = data.modelPosition
          
          print(f"Model: {data.modelName}")
          print(f"Position: ({position.positionX:.2f}, {position.positionY:.2f})")
          print(f"Rotation: {position.rotation:.2f}°")

   Event handlers must be async functions that accept the event object.

3. **Register Event Handler**

   .. code-block:: python

      vts.on_event(EventType.ModelMovedEvent, on_model_moved)

   Register the handler with the VTS client.

4. **Subscribe to Events**

   .. code-block:: python

      data = ModelMovedEventSubscriptionRequestData(
          subscribe=True,
          config=ModelMovedEventSubscriptionRequestConfig()
      )
      await vts.event_sub_model_moved(data)

   Subscribe to model moved events from VTube Studio.

5. **Keep Connection Alive**

   .. code-block:: python

      await asyncio.Event().wait()  # Wait indefinitely

   Keep the connection alive to receive events. The script will run until interrupted.

Expected Output
---------------

When run successfully, you should see output like:

.. code-block:: text

   Connecting to VTube Studio at localhost:8001...
   Successfully authenticated! Token: abc123def456...
   
   Registering handler for model moved events...
   Subscribing to model moved events...
   Listening for model moved events. Press Ctrl+C to stop...
   
   === Model Moved Event ===
   Model ID: model-123
   Model Name: MyModel
   Position X: 0.12
   Position Y: -0.05
   Rotation: 2.34°
   Size: 1.00
   
   === Model Moved Event ===
   Model ID: model-123
   Model Name: MyModel
   Position X: 0.13
   Position Y: -0.04
   Rotation: 2.35°
   Size: 1.00

The events will continue to fire as the model moves in VTube Studio.

Stopping the Script
-------------------

Press ``Ctrl+C`` to stop the script. The ``KeyboardInterrupt`` exception is caught, and the connection is properly closed.

