# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAutobridge(PythonPackage):
    """AutoBridge is a floorplanning tool for Vivado HLS dataflow designs."""

    homepage = "https://github.com/Licheng-Guo/AutoBridge"
    pypi = "autobridge/autobridge-0.0.20220512.dev1.tar.gz"

    # maintainers("github_user1", "github_user2")

    version("0.0.20220512.dev1", sha256="0221fa88574cef9fc145aa2c93ad10a50a1e1c3efb75e51cb98fdb0c8fcc2f4a")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-mip", type="run")
    depends_on("py-pyverilog", type="run")
    depends_on("py-prettytable", type="run")
