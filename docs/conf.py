"""Sphinx configuration for vtube-python documentation."""
import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = "vtube-python"
copyright = "2025, limitcantcode"
author = "limitcantcode"
release = "0.1.0"

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

# HTML theme
html_theme = "sphinx_rtd_theme"

# Autodoc settings
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

