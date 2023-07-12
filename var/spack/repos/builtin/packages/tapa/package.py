# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Tapa(CMakePackage):
    """TAPA is a dataflow HLS framework that features fast compilation, 
    expressive programming model and generates high-frequency FPGA 
    accelerators."""

    homepage = "https://tapa.rtfd.io"
    url = "https://github.com/UCLA-VAST/tapa/"
    git = "https://github.com/UCLA-VAST/tapa/"

    # maintainers("github_user1", "github_user2")

    version("2023-01-08", commit="c2617e3e8fe9ab916f16410fd01cd90bebefcc8e")

    variant("backend", default=True, description="TAPA backend")
    variant("coroutine", default=True, description="Boost coroutine")
    variant("stacktrace", default=True, description="Boost stacktrace")

    depends_on("boost")
    depends_on("boost+coroutine", when="+coroutine")
    depends_on("boost+stacktrace", when="+stacktrace")

    depends_on("fpga-runtime")

    patch("backend_CMakeLists.txt.patch")
    patch("backend_MicrosoftDemangleNodes.h.patch")

    def cmake_args(self):
      spec = self.spec
      args = [
          self.define_from_variant("TAPA_BUILD_BACKEND", "backend")
      ]
      return args
