# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTapaFastCosim(PythonPackage):
    """Fast cosim of HLS-generated RTL"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/UCLA-VAST/tapa-fast-cosim"
    pypi = "tapa-fast-cosim/tapa-fast-cosim-0.0.20220424.1.tar.gz"

    version("0.0.20220424.1", sha256="cc1cd5ffe1feabe31d0607bb05bddcfb3eb31e3a09821245e3e48c59655fa0da")

    depends_on("py-setuptools", type="build")
