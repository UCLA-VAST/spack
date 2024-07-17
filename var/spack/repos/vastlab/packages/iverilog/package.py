# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Iverilog(AutotoolsPackage):
    """Icarus Verilog is intended to compile ALL of the Verilog HDL as described in the IEEE-1364 standard."""

    homepage = "http://iverilog.icarus.com/"
    url = "https://github.com/steveicarus/iverilog/archive/refs/tags/v12_0.tar.gz"

    version("12_0", sha256="a68cb1ef7c017ef090ebedb2bc3e39ef90ecc70a3400afb4aa94303bc3beaa7d")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("gperf", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")

    def autoreconf(self, spec, prefix):
        bash = which("bash")
        bash("autoconf.sh")

