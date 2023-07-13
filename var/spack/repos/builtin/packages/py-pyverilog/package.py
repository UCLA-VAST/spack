# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyverilog(PythonPackage):
    """Python-based Hardware Design Processing Toolkit for Verilog HDL"""

    homepage = "https://github.com/PyHDI/Pyverilog"
    pypi = "pyverilog/pyverilog-1.3.0.tar.gz"

    version("1.3.0", sha256="59d93e9004ebe9e713e2fd6a9784a09e2d6b3c098091fd367795eb20329ae4a8")

    depends_on("py-setuptools", type="build")
    depends_on("py-ply", type="run")
