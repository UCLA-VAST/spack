# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Vtr(MakefilePackage):
    """Open-source framework for conducting FPGA architecture and CAD research and development"""

    homepage = "https://docs.verilogtorouting.org/en/latest/"
    url = "https://github.com/verilog-to-routing/vtr-verilog-to-routing/archive/refs/tags/v8.0.0.tar.gz"

    version("8.0.0", sha256="d95bf5dc2587d6b1ca11b261f7f5db22242f8e12a8f439a4d8b2ce46be31622e")

    depends_on("bison")
    depends_on("flex")
    depends_on("gtkplus@3:")
    #depends_on("libx11")
    depends_on("boost")

    depends_on("py-prettytable", type="run")
    depends_on("py-lxml", type="run")
    depends_on("py-psutil", type="run")
    depends_on("py-pandas", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-click@8.0.2", type="run")
    depends_on("py-black@21.4b0", type="run")
    depends_on("py-pylint@2.7.4", type="run")
    depends_on("py-orderedmultidict", type="run")

    with when("@8:"):
        patch("argparse.cpp.patch")
        patch("catch.hpp.patch")
        patch("vtr_small_vector.h.patch")
        patch("vtr_geometry.tpp.patch")
        patch("Hashtable.hpp.patch")

    def patch(self):
        # change SOURCE_DIR to spack-stage
        if self.spec.satisfies("@8:"):
            filter_file(
                r"^SOURCE_DIR := \$\(PWD\)",
                f"SOURCE_DIR := {self.stage.source_path}",
                "Makefile"
            )

    @property
    def build_targets(self):
        return [f"CMAKE_PARAMS='-DCMAKE_INSTALL_PREFIX={self.spec.prefix}'"]

