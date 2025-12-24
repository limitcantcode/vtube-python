Items Guide
===========

This guide covers working with items (accessories, effects, etc.) in VTube Studio.

Getting Item List
-----------------

To get a list of all available items:

.. code-block:: python

   from vtpy.data.requests import ItemListRequestData

   response = await vts.request_item_list(ItemListRequestData())
   items = response.data
   
   for item in items:
       print(f"Item: {item.name}")
       print(f"  ID: {item.itemID}")
       print(f"  File: {item.fileName}")

Loading Items
-------------

To load an item:

.. code-block:: python

   from vtpy.data.requests import ItemLoadRequestData

   response = await vts.request_item_load(
       ItemLoadRequestData(fileName="item-name.vtsitem")
   )
   
   if response.data:
       print(f"Item loaded: {response.data.itemID}")

Unloading Items
---------------

To unload an item:

.. code-block:: python

   from vtpy.data.requests import ItemUnloadRequestData

   response = await vts.request_item_unload(
       ItemUnloadRequestData(itemID="item-id-here")
   )
   
   if response.data:
       print("Item unloaded successfully")

Controlling Item Animations
---------------------------

To control item animations:

.. code-block:: python

   from vtpy.data.requests import ItemAnimationControlRequestData

   response = await vts.request_item_animation_control(
       ItemAnimationControlRequestData(
           itemInstanceID="item-instance-id",
           animationType="SetAnimation",
           animationName="animation-name"
       )
   )

Animation Types
---------------

Available animation types:

- **"SetAnimation"**: Set a specific animation
- **"SetAnimationFrame"**: Set animation to a specific frame
- **"SetSpeed"**: Set animation speed
- **"SetPause"**: Pause/unpause animation

Moving Items
------------

To move an item:

.. code-block:: python

   from vtpy.data.requests import ItemMoveRequestData, ItemPosition

   position = ItemPosition(
       positionX=0.0,
       positionY=0.0,
       rotation=0.0,
       size=1.0
   )
   
   response = await vts.request_item_move(
       ItemMoveRequestData(
           itemInstanceID="item-instance-id",
           timeInSeconds=1.0,
           valuesAreRelativeToModel=False,
           position=position
       )
   )

Sorting Items
-------------

To change the rendering order of items:

.. code-block:: python

   from vtpy.data.requests import ItemSortRequestData

   response = await vts.request_item_sort(
       ItemSortRequestData(
           itemInstanceID="item-instance-id",
           moveUp=True  # or False to move down
       )
   )

Pinning Items
-------------

To pin an item to a specific position:

.. code-block:: python

   from vtpy.data.requests import ItemPinRequestData

   response = await vts.request_item_pin(
       ItemPinRequestData(
           itemInstanceID="item-instance-id",
           pin=True  # or False to unpin
       )
   )

Listening to Item Events
-------------------------

You can listen to item-related events:

.. code-block:: python

   from vtpy.data.events import EventType, ItemEvent

   async def on_item_event(event: ItemEvent) -> None:
       data = event.data
       print(f"Item event: {data.itemName}")

   vts.on_event(EventType.ItemEvent, on_item_event)
   
   # Subscribe to events
   from vtpy.data.events import ItemEventSubscriptionRequestData
   
   await vts.event_sub_item(
       ItemEventSubscriptionRequestData(subscribe=True)
   )

Complete Example
----------------

.. code-block:: python

   import asyncio
   from vtpy import VTS
   from vtpy.data.requests import (
       ItemListRequestData,
       ItemLoadRequestData,
       ItemMoveRequestData,
       ItemPosition,
   )

   async def main():
       vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
       
       try:
           await vts.start(host="localhost", port=8001)
           
           # Get available items
           items_response = await vts.request_item_list(ItemListRequestData())
           print("Available items:")
           for item in items_response.data:
               print(f"  - {item.name} ({item.fileName})")
           
           # Load an item (if you know the filename)
           # load_response = await vts.request_item_load(
           #     ItemLoadRequestData(fileName="some-item.vtsitem")
           # )
           # item_id = load_response.data.itemID
           
           # Move an item
           # await vts.request_item_move(
           #     ItemMoveRequestData(
           #         itemInstanceID=item_id,
           #         timeInSeconds=1.0,
           #         valuesAreRelativeToModel=False,
           #         position=ItemPosition(
           #             positionX=0.5,
           #             positionY=0.5,
           #             rotation=0.0,
           #             size=1.0
           #         )
           #     )
           # )
           
       finally:
           if vts.connected:
               await vts.close()

   asyncio.run(main())

