# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHaoda(PythonPackage):
    """Reusable Python utilities for hardware-aware optimization and design automation"""

    homepage = "https://github.com/Blaok/haoda"
    pypi = "haoda/haoda-0.0.20230106.dev1.tar.gz"

    version("0.0.20230106.dev1", sha256="58e9b908a6ed2ad52580bb2605068e8b5e704cf4959a89b114261852c0aa489c")

    depends_on("py-setuptools", type="build")
