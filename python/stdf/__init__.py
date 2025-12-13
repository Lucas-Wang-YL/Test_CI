"""
STDF (Standard Test Data Format) Parser
Semiconductor test data processing module
"""

__version__ = '1.0.0'
__author__ = 'Lucas'

from .parser import STDFParser
from .records import *

__all__ = ['STDFParser']
