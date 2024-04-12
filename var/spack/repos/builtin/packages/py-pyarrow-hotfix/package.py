# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyarrowHotfix(PythonPackage):
    """This is a hotfix for the PyArrow security vulnerability CVE-2023-47248."""

    homepage = "https://pypi.org/project/pyarrow-hotfix"
    pypi = "pyarrow_hotfix/pyarrow_hotfix-0.6.tar.gz"

    version("0.6", sha256="79d3e030f7ff890d408a100ac16d6f00b14d44a502d7897cd9fc3e3a534e9945")

    depends_on("py-hatchling", type="build")

