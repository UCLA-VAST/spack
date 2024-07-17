# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGraphTool(AutotoolsPackage):
    """graph-tool is an efficient Python module for manipulation and statistical
    analysis of graphs (a.k.a. networks)."""

    homepage = "http://graph-tool.skewed.de/"
    url = "https://git.skewed.de/count0/graph-tool/-/archive/release-2.58/graph-tool-release-2.58.tar.gz"

    version("2.58", sha256="f150a09ac210693206da7a32346ba48afb317ed6c1b5f8bfbc3aaa70954778a6")

    variant("sparsehash", default=True, description="Use sparsehash")
    variant("drawing", default=True, description="Enable drawing support")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("pkg-config", type="build")
    depends_on("python@3:", type=("build", "link", "run"))

    depends_on("boost@1.55:+python+iostreams+regex+context+coroutine+graph+thread", type=("build", "link"))
    depends_on("expat", type=("build", "link"))
    depends_on("cgal@3.5:", type=("build", "link"))
    depends_on("py-numpy@1.7:", type="build")
    depends_on("sparsehash", type=("build", "link"), when="+sparsehash")
    depends_on("cairomm", type=("build", "link"), when="+drawing")
    depends_on("py-pycairo", type=("build", "run"), when="+drawing")
    depends_on("gtkplus@3:", type=("build", "link"), when="+drawing")

    depends_on("py-scipy", type="run")
    depends_on("py-matplotlib", type="run", when="+drawing")
    depends_on("py-pygobject@3:", type="run", when="+drawing")

    def configure_args(self):
        spec = self.spec
        args = []

        python_version = self.spec["python"].version.up_to(2)
        args.append("--with-python-module-path={}".format(
            join_path(self.prefix.lib, "python{0}".format(python_version), "site-packages")
        ))

        args.append("--with-boost={}".format(spec["boost"].prefix))
        args.append("--with-cgal={}".format(spec["cgal"].prefix))

        if not spec.variants["drawing"].value:
            args.append("--disable-cairo")

        if not spec.variants["sparsehash"].value:
            args.append("--disable-sparsehash")

        return args

    def setup_run_environment(self, env):
        spec = self.spec
        # libglib-2.0.so.0, libgdk-3.so.0
        ld_preload = []
        ld_preload.extend(find_libraries(f"libglib-[0-9.]*[0-9]", root=spec["glib"].prefix.lib))
        ld_preload.extend(find_libraries(f"libgtk-[0-9]", root=spec["gtkplus"].prefix.lib))
        env.prepend_path("LD_PRELOAD", ':'.join(ld_preload))
        env.prepend_path("PYTHONPATH", python_platlib)
