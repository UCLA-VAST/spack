# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Kissat(AutotoolsPackage):
    """Kissat is a "keep it simple and clean bare metal SAT solver" written in C."""

    homepage = "https://github.com/arminbiere/kissat"
    url = "https://github.com/arminbiere/kissat/archive/refs/tags/rel-3.1.0.tar.gz"

    version("3.1.0", sha256="e85c757179bf7d96d21d2d6e3f0a8f2337d416b0e13ae065a9a8d52e30048bd3")

    patch("configure.patch")
    patch("makefile.in.patch")
