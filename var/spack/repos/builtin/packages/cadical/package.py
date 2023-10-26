# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cadical(AutotoolsPackage):
    """The goal of CaDiCaL is to provide a clean and efficient state-of-the-art 
    CDCL solver, which is also easy to understand and change."""

    homepage = "https://fmv.jku.at/cadical/"
    url = "https://github.com/arminbiere/cadical/archive/refs/tags/rel-1.8.0.tar.gz"

    version("1.8.0", sha256="f053be060898079f353530b7d2fc25360f9b43ad924ae0891e13cc3193bf8ca0")

    patch("configure.patch")
    patch("makefile.in.patch")

