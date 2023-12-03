# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os, subprocess

class Libsigcpp(MesonPackage, AutotoolsPackage):
    """Libsigc++ is a C++ library for typesafe callbacks"""

    homepage = "https://libsigcplusplus.github.io/libsigcplusplus/index.html"
    url = "https://ftp.acc.umu.se/pub/GNOME/sources/libsigc++/2.99/libsigc++-2.99.12.tar.xz"
    list_url = "https://ftp.acc.umu.se/pub/GNOME/sources/libsigc++/"
    list_depth = 1

    version("3.6.0", sha256="c3d23b37dfd6e39f2e09f091b77b1541fbfa17c4f0b6bf5c89baef7229080e17")
    version("3.4.0", sha256="02e2630ffb5ce93cd52c38423521dfe7063328863a6e96d41d765a6116b8707e")
    version("3.2.0", sha256="8cdcb986e3f0a7c5b4474aa3c833d676e62469509f4899110ddf118f04082651")
    version("3.0.7", sha256="bfbe91c0d094ea6bbc6cbd3909b7d98c6561eea8b6d9c0c25add906a6e83d733")
    version("3.0.6", sha256="b70edcf4611651c54a426e109b17196e1fa17da090592a5000e2d134c03ac5ce")
    version("3.0.4", sha256="a3a37410186379df1908957e7aba7519bdcf5bcc8ed70ee8dfea9362c393d545")
    version("3.0.3", sha256="e4f4866a894bdbe053e4fb22ccc6bc4b6851fd31a4746fdd20b2cf6e87c6edb6")
    version("3.0.2", sha256="4b77676de1e74774ec456bcc6ac6f04a2791a12cc1fe07f8305d4c3c86e2f339")
    version("3.0.1", sha256="82e2764aab217755a83b90a082ce451b05bba3ed1ce9b6e21fe412d4d8b38d48")
    version("3.0.0", sha256="50a0855c1eb26e6044ffe888dbe061938ab4241f96d8f3754ea7ead38ab8ed06")

    version("2.99.12", sha256="d902ae277f5baf2d56025586e2153cc2f158472e382723c67f49049f7c6690a8")
    version("2.9.3", sha256="0bf9b301ad6198c550986c51150a646df198e8d1d235270c16486b0dda30097f")
    version("2.1.1", sha256="7a2bd0b521544b31051c476205a0e74ace53771ec1a939bfec3c297b50c9fd78")
    version("2.0.3", sha256="6ee6d5f164d8a34da33d2251cdb348b4f5769bf993ed8a6d4055bd47562f94a2")

    build_system(
        conditional("meson", when="@3:"),
        conditional("autotools", when="@:2"),
        default="meson",
    )

    depends_on("m4", when="@:2.9", type="build")

    def url_for_version(self, version):
        """Handle version-based custom URLs."""
        url = "https://ftp.acc.umu.se/pub/GNOME/sources/libsigc++"
        ext = ".tar.gz" if version < Version("2.2.10") else ".tar.xz"
        return url + "/%s/libsigc++-%s%s" % (version.up_to(2), version, ext)

    def configure_args(self):
        return ["--enable-static"]
