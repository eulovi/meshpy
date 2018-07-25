# -*- coding: utf-8 -*-
"""
This module defines classes and functions to create and edit a Baci input file.
"""

# Global configuration object.
from .conf import mpy

# Find close node Cython function.
from .meshpy.find_close_nodes import find_close_nodes

# Utility functions and base classes.
from .utility import get_close_nodes, flatten, compare_xml
from .base_mesh_item import BaseMeshItem

# 3D rotations for nodes.
from .rotation import Rotation, get_relative_rotation

# VTK writer.
from .vtk_writer import add_point_data_node_sets, VTKWriter

# Mesh items.
from .function import Function
from .material import Material, MaterialBeam, MaterialReissner
from .node import Node
from .element import Element
from .element_solid import SolidElement, SolidHEX8, SolidRigidSphere
from .element_beam import Beam, Beam3rHerm2Lin3
from .geometry_set import GeometrySet

# Containers that group mesh items together.
from .container import GeometryName, BoundaryConditionContainer, \
    GeometrySetContainer

# Boundary conditions and couplings for geometry in the mesh.
from .boundary_condition import BoundaryCondition
from .coupling import Coupling

# The mesh class itself and the input file classes.
from .mesh import Mesh
from .inputfile import InputFile, InputSection, InputLine

# Define the itCouplingems that will be exported by default.
__all__ = [
    # Option object.
    'mpy',
    # Utility functions.
    'flatten',
    # Basic stuff.
    'Rotation', 'get_relative_rotation', 'Function', 'MaterialReissner',
    'MaterialBeam', 'GeometrySet', 'BoundaryCondition', 'Coupling',
    # Mesh items
    'Beam3rHerm2Lin3', 'Mesh', 'InputFile', 'InputSection'
    ]
