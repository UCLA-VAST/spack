# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOrderedmultidict(PythonPackage):
    """omdict is an ordered multivalue dictionary that retains method parity"""

    homepage = "https://github.com/gruns/orderedmultidict"
    pypi = "orderedmultidict/orderedmultidict-1.0.1.tar.gz"

    version("1.0.1", sha256="04070bbb5e87291cc9bfa51df413677faf2141c73c61d2a5f7b26bea3cd882ad")

    depends_on("py-setuptools", type="build")
