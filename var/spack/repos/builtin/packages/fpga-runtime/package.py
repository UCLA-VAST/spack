# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class FpgaRuntime(CMakePackage):
    """This project provides a convenient runtime for PCIe-based FPGAs 
    programmed under the OpenCL host-kernel model. Both Intel and Xilinx 
    platforms are supported."""

    homepage = "https://github.com/Blaok/fpga-runtime"
    url = "https://github.com/Blaok/fpga-runtime/archive/refs/tags/0.0.20221212.1.tar.gz"

    # maintainers("github_user1", "github_user2")

    version("0.0.20221212.1", sha256="4a42a443c9f752d4d3b8e212283e1e8b9b661a90cda006416d94335b78507af7")

    depends_on("glog", type=("build", "link"))
    depends_on("tinyxml", type=("build", "link"))
    depends_on("googletest", type="test")

    patch("CMakeLists.txt.patch")
    patch("cmake_FRTConfig.cmake.patch")
    patch("cmake_FindTinyXML.cmake.patch")

