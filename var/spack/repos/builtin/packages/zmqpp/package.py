# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Zmqpp(CMakePackage):
    """C++ bindings for zmq"""

    homepage = "https://github.com/zeromq/zmqpp"
    url = "https://github.com/zeromq/zmqpp/archive/refs/tags/4.2.0.tar.gz"

    version("4.2.0", sha256="c1d4587df3562f73849d9e5f8c932ca7dcfc7d8bec31f62d7f35073ef81f4d29")

    depends_on("libzmq")

    def cmake_args(self):
        args = []
        return args
