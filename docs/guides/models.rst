Models Guide
============

This guide covers working with Live2D models in VTube Studio.

Getting Current Model
---------------------

To get information about the currently loaded model:

.. code-block:: python

   from vtpy.data.requests import CurrentModelRequestData

   response = await vts.request_current_model(CurrentModelRequestData())
   model = response.data
   
   print(f"Model ID: {model.modelID}")
   print(f"Model Name: {model.modelName}")
   print(f"Model Position: ({model.modelPosition.positionX}, {model.modelPosition.positionY})")

Listing Available Models
------------------------

To get a list of all available models:

.. code-block:: python

   response = await vts.request_available_models()
   models = response.data
   
   for model in models:
       print(f"Model: {model.modelName}")
       print(f"  ID: {model.modelID}")
       print(f"  Path: {model.modelPath}")

Loading a Model
---------------

To load a specific model:

.. code-block:: python

   from vtpy.data.requests import ModelLoadRequestData

   response = await vts.request_model_load(
       ModelLoadRequestData(modelID="model-id-here")
   )
   
   if response.data:
       print(f"Model loaded: {response.data.modelID}")

Moving a Model
--------------

To change a model's position, rotation, or size:

.. code-block:: python

   from vtpy.data.requests import MoveModelRequestData, ModelPosition

   position = ModelPosition(
       positionX=0.0,
       positionY=0.0,
       rotation=0.0,
       size=1.0
   )
   
   response = await vts.request_move_model(
       MoveModelRequestData(
           timeInSeconds=1.0,
           valuesAreRelativeToModel=False,
           position=position
       )
   )

Model Position Properties
-------------------------

The ``ModelPosition`` class has the following properties:

- **positionX** (float): X position (-1.0 to 1.0)
- **positionY** (float): Y position (-1.0 to 1.0)
- **rotation** (float): Rotation in degrees
- **size** (float): Size multiplier

Listening to Model Events
--------------------------

You can listen to model-related events:

.. code-block:: python

   from vtpy.data.events import EventType, ModelMovedEvent

   async def on_model_moved(event: ModelMovedEvent) -> None:
       data = event.data
       print(f"Model {data.modelName} moved")

   vts.on_event(EventType.ModelMovedEvent, on_model_moved)
   
   # Subscribe to events
   from vtpy.data.events import (
       ModelMovedEventSubscriptionRequestData,
       ModelMovedEventSubscriptionRequestConfig,
   )
   
   await vts.event_sub_model_moved(
       ModelMovedEventSubscriptionRequestData(
           subscribe=True,
           config=ModelMovedEventSubscriptionRequestConfig()
       )
   )

Getting Model Art Meshes
------------------------

To get a list of art meshes in the current model:

.. code-block:: python

   from vtpy.data.requests import ArtMeshListRequestData

   response = await vts.request_art_mesh_list(ArtMeshListRequestData())
   meshes = response.data
   
   for mesh in meshes:
       print(f"Mesh: {mesh.name}")
       print(f"  ID: {mesh.id}")

Tinting Model Art Meshes
-------------------------

To change the color of art meshes:

.. code-block:: python

   from vtpy.data.requests import ColorTintRequestData, ColorTint, ArtMeshMatcherData

   tint = ColorTint(
       colorR=1.0,
       colorG=0.5,
       colorB=0.5,
       colorA=1.0,
       colorMixWithSceneLightingColor=0.5
   )

   artMeshMatcher = ArtMeshMatcherData(
       tintAll=True
   )
   response = await vts.request_color_tint(
       ColorTintRequestData(
           artMeshMatcher=artMeshMatcher,
           colorTint=tint
       )
   )

