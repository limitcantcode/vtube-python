Hotkeys Guide
=============

This guide covers working with hotkeys in VTube Studio.

Getting Hotkeys
---------------

To get a list of hotkeys for the current model:

.. code-block:: python

   response = await vts.request_hotkeys_in_current_model()
   hotkeys = response.data
   
   for hotkey in hotkeys:
       print(f"Hotkey: {hotkey.name}")
       print(f"  ID: {hotkey.hotkeyID}")
       print(f"  File: {hotkey.file}")

Triggering Hotkeys
------------------

To trigger a hotkey:

.. code-block:: python

   from vtpy.data.requests import HotkeyTriggerRequestData

   response = await vts.request_hotkey_trigger(
       HotkeyTriggerRequestData(hotkeyID="hotkey-id-here")
   )
   
   if response.data:
       print("Hotkey triggered successfully")

Listening to Hotkey Events
---------------------------

You can listen to hotkey trigger events:

.. code-block:: python

   from vtpy.data.events import EventType, HotkeyTriggeredEvent

   async def on_hotkey_triggered(event: HotkeyTriggeredEvent) -> None:
       data = event.data
       print(f"Hotkey triggered: {data.hotkeyID}")
       print(f"  Name: {data.hotkeyName}")

   vts.on_event(EventType.HotkeyTriggeredEvent, on_hotkey_triggered)
   
   # Subscribe to events
   from vtpy.data.events import (
       HotkeyTriggeredEventSubscriptionRequestData,
   )
   
   await vts.event_sub_hotkey_triggered(
       HotkeyTriggeredEventSubscriptionRequestData(subscribe=True)
   )

Complete Example
----------------

.. code-block:: python

   import asyncio
   from vtpy import VTS
   from vtpy.data.requests import HotkeyTriggerRequestData
   from vtpy.data.events import (
       EventType,
       HotkeyTriggeredEvent,
       HotkeyTriggeredEventSubscriptionRequestData,
   )

   async def on_hotkey_triggered(event: HotkeyTriggeredEvent) -> None:
       print(f"Hotkey triggered: {event.data.hotkeyName}")

   async def main():
       vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
       
       try:
           await vts.start(host="localhost", port=8001)
           
           # Get available hotkeys
           hotkeys_response = await vts.request_hotkeys_in_current_model()
           print("Available hotkeys:")
           for hotkey in hotkeys_response.data:
               print(f"  - {hotkey.name} (ID: {hotkey.hotkeyID})")
           
           # Listen to hotkey events
           vts.on_event(EventType.HotkeyTriggeredEvent, on_hotkey_triggered)
           await vts.event_sub_hotkey_triggered(
               HotkeyTriggeredEventSubscriptionRequestData(subscribe=True)
           )
           
           # Trigger a hotkey (if you know the ID)
           # await vts.request_hotkey_trigger(
           #     HotkeyTriggerRequestData(hotkeyID="some-hotkey-id")
           # )
           
           print("Listening for hotkey events. Press Ctrl+C to stop...")
           await asyncio.Event().wait()
           
       except KeyboardInterrupt:
           print("Stopping...")
       finally:
           if vts.connected:
               await vts.close()

   asyncio.run(main())

