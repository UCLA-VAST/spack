# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cairomm(MesonPackage, AutotoolsPackage):
    """Cairomm is a C++ wrapper for the cairo graphics library."""

    homepage = "https://www.cairographics.org/cairomm/"
    url = "https://cairographics.org/releases/cairomm-1.6.2.tar.gz"

    version("1.18.0", sha256="b81255394e3ea8e8aa887276d22afa8985fc8daef60692eb2407d23049f03cfb")
    version("1.17.1", sha256="343e8463ff7dd4d2c90991d6284a2203431e711026575207fd4c313cd323fdbe")
    version("1.16.2", sha256="6a63bf98a97dda2b0f55e34d1b5f3fb909ef8b70f9b8d382cb1ff3978e7dc13f")
    version("1.16.1", sha256="6f6060d8e98dd4b8acfee2295fddbdd38cf487c07c26aad8d1a83bb9bff4a2c6")
    version("1.16.0", sha256="7e881492c5f9f546688c31160deb742c166fc4c68b6b8eb9920c00a0f0f144f9")
    version("1.6.4", sha256="3cb2c898d0ceb94ad2deb722b50a3a6ee46abdda741ecd6e5a40517c85ecea4c")
    version("1.6.2", sha256="068edc1743d92ff1d102141ba7597ba02a47379f9cb97799b0c3310848b56eff")

    build_system(
        conditional("meson", when="@1.16:"),
        conditional("autotools", when="@:1.15"),
        default="meson",
    )

    with when("@1.16:"):
      depends_on("cairo@1.16:")
      depends_on("libsigcpp@3:")

    depends_on("cairo")
    depends_on("libsigcpp")
    depends_on("pkgconfig", type="build")

    def url_for_version(self, version):
        url = "https://cairographics.org/releases/cairomm-{}{}"
        ext = ".tar.gz" if version < Version("1.14.0") else ".tar.xz"
        return url.format(version, ext)
