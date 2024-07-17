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

    variant("shared", default=True, description="Also build shared library")
    variant("pic", default=True, description="Build static library with PIC")

    patch("configure.patch")
    patch("makefile.in.patch")

    def configure_args(self):
        args = []

        if "+shared" in self.spec:
            args.append("-shared")

        if "+pic" in self.spec:
            args.append("-fpic")

        return args

