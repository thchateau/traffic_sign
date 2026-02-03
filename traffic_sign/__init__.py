"""
Traffic Sign Recognition Package

This package provides tools for traffic sign recognition using three approaches:
1. Florence (Microsoft) - Generative AI for traffic sign description
2. OpenCLIP - Image comparison with description database
3. Mapillary API - Traffic sign recognition in images
"""

__version__ = "0.1.0"

from . import florence
from . import openclip
from . import mapillary

__all__ = ["florence", "openclip", "mapillary"]
