Events Guide
=============

vtpy supports event-driven programming with VTube Studio. This guide shows how to subscribe to and handle events.

Event Types
-----------

VTube Studio provides various event types you can subscribe to:

- **ModelLoadedEvent**: Fired when a model is loaded
- **ModelMovedEvent**: Fired when a model's position changes
- **TrackingStatusChangedEvent**: Fired when face tracking status changes
- **BackgroundChangedEvent**: Fired when the background changes
- **HotkeyTriggeredEvent**: Fired when a hotkey is triggered
- **ModelAnimationEvent**: Fired when a model animation plays
- And more...

Registering Event Handlers
---------------------------

To handle events, register a handler function:

.. code-block:: python

   from vtpy.data.events import EventType, ModelMovedEvent

   async def on_model_moved(event: ModelMovedEvent) -> None:
       """Handle model moved events."""
       data = event.data
       print(f"Model {data.modelName} moved to ({data.modelPosition.positionX}, {data.modelPosition.positionY})")

   vts.on_event(EventType.ModelMovedEvent, on_model_moved)

Event handlers must be async functions that accept the event object as a parameter.

Subscribing to Events
---------------------

After registering a handler, subscribe to the event:

.. code-block:: python

   from vtpy.data.events import (
       ModelMovedEventSubscriptionRequestData,
       ModelMovedEventSubscriptionRequestConfig,
   )

   # Subscribe to model moved events
   await vts.event_sub_model_moved(
       ModelMovedEventSubscriptionRequestData(
           subscribe=True,
           config=ModelMovedEventSubscriptionRequestConfig()
       )
   )

Unsubscribing from Events
--------------------------

To stop receiving events:

.. code-block:: python

   await vts.event_sub_model_moved(
       ModelMovedEventSubscriptionRequestData(
           subscribe=False,
           config=ModelMovedEventSubscriptionRequestConfig()
       )
   )

Removing Event Handlers
-----------------------

To remove an event handler:

.. code-block:: python

   vts.remove_event_handler(EventType.ModelMovedEvent, on_model_moved)

Or remove all handlers for an event type:

.. code-block:: python

   vts.remove_event_handler(EventType.ModelMovedEvent)

Complete Example
----------------

.. code-block:: python

   import asyncio
   from vtpy import VTS
   from vtpy.data.events import (
       EventType,
       ModelMovedEvent,
       ModelMovedEventSubscriptionRequestData,
       ModelMovedEventSubscriptionRequestConfig,
   )

   async def on_model_moved(event: ModelMovedEvent) -> None:
       data = event.data
       position = data.modelPosition
       print(f"Model: {data.modelName}")
       print(f"Position: ({position.positionX:.2f}, {position.positionY:.2f})")
       print(f"Rotation: {position.rotation:.2f}°")

   async def main():
       vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
       
       try:
           await vts.start(host="localhost", port=8001)
           
           # Register handler
           vts.on_event(EventType.ModelMovedEvent, on_model_moved)
           
           # Subscribe to events
           await vts.event_sub_model_moved(
               ModelMovedEventSubscriptionRequestData(
                   subscribe=True,
                   config=ModelMovedEventSubscriptionRequestConfig()
               )
           )
           
           # Keep running to receive events
           print("Listening for events. Press Ctrl+C to stop...")
           await asyncio.Event().wait()
           
       except KeyboardInterrupt:
           print("Stopping...")
       finally:
           if vts.connected:
               await vts.close()

   asyncio.run(main())

Available Event Subscriptions
------------------------------

vtpy provides methods for subscribing to all VTube Studio events:

- ``event_sub_test()`` - Test event subscription
- ``event_sub_model_loaded()`` - Model loaded events
- ``event_sub_tracking_status_changed()`` - Face tracking status changes
- ``event_sub_background_changed()`` - Background changes
- ``event_sub_model_config_modified()`` - Model configuration changes
- ``event_sub_model_moved()`` - Model position changes
- ``event_sub_model_outline()`` - Model outline changes
- ``event_sub_hotkey_triggered()`` - Hotkey triggers
- ``event_sub_model_animation()`` - Model animations
- ``event_sub_item()`` - Item events
- ``event_sub_model_clicked()`` - Model click events
- ``event_sub_post_processing()`` - Post-processing events
- ``event_sub_live2d_cubism_editor_connected()`` - Live2D Cubism editor connection

See the :doc:`../api/vtpy.vts` documentation for details on each method.

