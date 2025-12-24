vtpy.error Package
==================

Error Handling
--------------

The ``vtpy.error`` package contains exception classes for error handling.

VTSRequestError
---------------

.. automodule:: vtpy.error.error
   :members:
   :undoc-members:
   :show-inheritance:

Usage Example
-------------

.. code-block:: python

   from vtpy.error import VTSRequestError

   try:
       await vts.request_statistics(StatisticsRequestData())
   except VTSRequestError as e:
       print(f"Error: {e.message}")
       print(f"Error ID: {e.error_id}")

