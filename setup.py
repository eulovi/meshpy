# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# MeshPy: A beam finite element input generator
#
# MIT License
#
# Copyright (c) 2021 Ivo Steinbrecher
#                    Institute for Mathematics and Computer-Based Simulation
#                    Universitaet der Bundeswehr Muenchen
#                    https://www.unibw.de/imcs-en
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

from setuptools import setup
import os
import numpy as np
from Cython.Build import cythonize

setup(
    name="meshpy",
    version="0.1",
    author="Ivo Steinbrecher",
    author_email="ivo.steinbrecher@unibw.de",
    description="MeshPy: A beam finite element input generator",
    install_requires=[
        "autograd",
        "black==22.12.0",
        "Cython",
        "geomdl",
        "matplotlib",
        "numpy",
        "scipy",
        "vtk",
    ],
    extras_require={
        "CI-CD": ["coverage", "coverage-badge"],
    },
    license_files=["LICENSE"],
    packages=[
        "meshpy",
        "meshpy.mesh_creation_functions",
        "meshpy.simulation_manager",
        "meshpy.utility_baci",
    ],
    package_data={"meshpy.simulation_manager": ["batch_template.sh"]},
    ext_modules=cythonize(
        "meshpy/find_close_points_cython.pyx",
        annotate=True,
        build_dir=os.path.join("build", "cython_generated_code"),
    ),
    include_dirs=[np.get_include()],
)
