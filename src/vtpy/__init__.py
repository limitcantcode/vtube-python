"""vtube-python: Python library for interfacing with VTube Studio API."""

__version__ = "0.1.0"
__author__ = "limitcantcode"

from . import data, error
from .vts import VTS

__all__ = ["__version__", "data", "error", "VTS"]
