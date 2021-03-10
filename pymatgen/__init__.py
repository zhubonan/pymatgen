# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.
# pylint: disable=C0413

"""
Pymatgen (Python Materials Genomics) is a robust, open-source Python library
for materials analysis. This is the root package.
"""
__author__ = "Pymatgen Development Team"
__email__ = "pymatgen@googlegroups.com"
__maintainer__ = "Shyue Ping Ong"
__maintainer_email__ = "shyuep@gmail.com"
__version__ = "2021.3.9"

import warnings

# Useful aliases for commonly used objects and modules.
# Allows from pymatgen import <class> for quick usage.
# Note that these have to come after the SETTINGS have been loaded. Otherwise, import does not work.

from .core import SETTINGS, SETTINGS_FILE  # noqa
from .core.composition import Composition  # noqa
from .core.lattice import Lattice  # noqa
from .core.operations import SymmOp  # noqa
from .core.periodic_table import DummySpecie, DummySpecies, Element, Specie, Species  # noqa
from .core.sites import PeriodicSite, Site  # noqa
from .core.structure import IMolecule, IStructure, Molecule, Structure  # noqa
from .core.units import ArrayWithUnit, FloatWithUnit, Unit  # noqa
from .electronic_structure.core import Orbital, Spin  # noqa
from .ext.matproj import MPRester  # noqa


warnings.warn(
    "All convenience imports in pymatgen/__init__.py will be removed from pymatgen>=2022.0.3. Please see "
    "https://pymatgen.org/compatibility.html for instructions on how to make your code compatible with newer versions "
    "of pymatgen. You should no longer use from pymatgen import Element, but rather from pymatgen.core import Structre."
    " MPRester should be imported from pymatgen.ext.matproj. This will still be compatible with older versions of "
    "pymatgen",
    FutureWarning,
)
