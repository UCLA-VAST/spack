# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMip(PythonPackage):
    """Python MIP is a collection of Python tools for the modeling and 
    solution of Mixed-Integer Linear programs (MIPs)."""

    homepage = "https://www.python-mip.com/"
    pypi = "mip/mip-1.15.0.tar.gz"

    version("1.15.0", sha256="7f6f0381cfe2c52c1b8640203da2cb56974b26e23950ddfb1a76b37d916f197e")

    depends_on("py-setuptools", type="build")
    depends_on("py-cffi", type="run")
