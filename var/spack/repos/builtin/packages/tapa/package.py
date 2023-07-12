# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class Tapa(CMakePackage, PythonExtension):
    """TAPA is a dataflow HLS framework that features fast compilation, 
    expressive programming model and generates high-frequency FPGA 
    accelerators."""

    homepage = "https://tapa.rtfd.io"
    url = "https://github.com/UCLA-VAST/tapa/"
    git = "https://github.com/UCLA-VAST/tapa/"

    # maintainers("github_user1", "github_user2")

    version("2023-01-08", commit="c2617e3e8fe9ab916f16410fd01cd90bebefcc8e")

    variant("python", default=True, description="TAPA python")
    variant("backend", default=True, description="TAPA backend")
    variant("coroutine", default=True, description="Boost coroutine")
    variant("stacktrace", default=True, description="Boost stacktrace")

    depends_on("fpga-runtime")

    extends("python", when="+python")
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-wheel", when="+python", type="build")
    depends_on("py-setuptools", when="+python", type="build")

    depends_on("boost")
    depends_on("boost+coroutine", when="+coroutine")
    depends_on("boost+stacktrace", when="+stacktrace")

    patch("backend_CMakeLists.txt.patch")
    patch("backend_MicrosoftDemangleNodes.h.patch")

    def cmake_args(self):
      spec = self.spec
      args = [
          self.define_from_variant("TAPA_BUILD_BACKEND", "backend")
      ]
      return args

    @run_after("install")
    def install_python(self):
        if "+python" in self.spec:
            with working_dir(os.path.join("backend", "python")):
                args = std_pip_args + ["--prefix=" + prefix, "."]
                pip(*args)
