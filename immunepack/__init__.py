"""TCR Immune PowerLaw: Power-law analysis pipeline for TCR clonotypes and immune dynamics.

A Python package implementing heavy-tailed analysis of immune clonotypes using robust
power-law fitting, bootstrap inference, and neutral model comparison.
"""

__version__ = '0.1.0'
__author__ = 'Elkin Navarro'
__email__ = 'elkin.navarro@unisimon.edu.co'

# Import main modules
from . import powerlaw
from . import models
from . import loaders
from . import utils
from . import pipelines

__all__ = [
    'powerlaw',
    'models',
    'loaders', 
    'utils',
    'pipelines',
]
