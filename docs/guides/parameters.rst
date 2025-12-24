Parameters Guide
=================

This guide covers working with input parameters in VTube Studio.

Getting Input Parameters
------------------------

To get a list of input parameters:

.. code-block:: python

   response = await vts.request_input_parameter_list()
   parameters = response.data
   
   for param in parameters:
       print(f"Parameter: {param.name}")
       print(f"  Value: {param.value}")
       print(f"  Min: {param.min}, Max: {param.max}")
       print(f"  Default: {param.defaultValue}")

Getting Parameter Values
-------------------------

To get the current value of a specific parameter:

.. code-block:: python

   from vtpy.data.requests import ParameterValueRequestData

   response = await vts.request_parameter_value(
       ParameterValueRequestData(name="MouthOpen")
   )
   
   value = response.data.value
   print(f"MouthOpen value: {value}")

Getting Live2D Parameters
--------------------------

To get Live2D-specific parameters:

.. code-block:: python

   response = await vts.request_live2d_parameter_list()
   parameters = response.data
   
   for param in parameters:
       print(f"Live2D Parameter: {param.name}")
       print(f"  Value: {param.value}")
       print(f"  Min: {param.min}, Max: {param.max}")

Creating Custom Parameters
---------------------------

You can create custom input parameters:

.. code-block:: python

   from vtpy.data.requests import ParameterCreationRequestData

   response = await vts.request_parameter_creation(
       ParameterCreationRequestData(
           parameterName="MyCustomParameter",
           explanation="A custom parameter",
           min=0.0,
           max=1.0,
           defaultValue=0.5
       )
   )
   
   if response.data:
       print("Parameter created successfully")

Deleting Custom Parameters
---------------------------

To delete a custom parameter:

.. code-block:: python

   from vtpy.data.requests import ParameterDeletionRequestData

   response = await vts.request_parameter_deletion(
       ParameterDeletionRequestData(parameterName="MyCustomParameter")
   )
   
   if response.data:
       print("Parameter deleted successfully")

Injecting Parameter Data
------------------------

To inject parameter values (for face tracking or custom control):

.. code-block:: python

   from vtpy.data.requests import InjectParameterDataRequestData, ParameterInjectionValue

   values = [
       ParameterInjectionValue(
           id="MouthOpen",
           value=0.5,
           weight=1.0
       ),
       ParameterInjectionValue(
           id="EyeOpenLeft",
           value=0.8,
           weight=1.0
       )
   ]
   
   response = await vts.request_inject_parameter_data(
       InjectParameterDataRequestData(
           faceFound=True,
           mode="set",
           parameterValues=values
       )
   )

Parameter Injection Modes
--------------------------

The injection mode can be:

- **"set"**: Set the parameter to the specified value
- **"add"**: Add the value to the current parameter value
- **"multiply"**: Multiply the current value by the specified value

Complete Example
----------------

.. code-block:: python

   import asyncio
   from vtpy import VTS
   from vtpy.data.requests import (
       ParameterValueRequestData,
       InjectParameterDataRequestData,
       ParameterInjectionValue,
   )

   async def main():
       vts = VTS(plugin_name="MyPlugin", plugin_developer="MyName")
       
       try:
           await vts.start(host="localhost", port=8001)
           
           # Get all input parameters
           params_response = await vts.request_input_parameter_list()
           print("Available parameters:")
           for param in params_response.data:
               print(f"  - {param.name}: {param.value}")
           
           # Get specific parameter value
           mouth_response = await vts.request_parameter_value(
               ParameterValueRequestData(name="MouthOpen")
           )
           print(f"\nMouthOpen value: {mouth_response.data.value}")
           
           # Inject parameter values
           await vts.request_inject_parameter_data(
               InjectParameterDataRequestData(
                   faceFound=True,
                   mode="set",
                   parameterValues=[
                       ParameterInjectionValue(
                           id="MouthOpen",
                           value=0.7,
                           weight=1.0
                       )
                   ]
               )
           )
           print("\nInjected MouthOpen = 0.7")
           
       finally:
           if vts.connected:
               await vts.close()

   asyncio.run(main())

