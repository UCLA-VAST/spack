# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNvidiaDllogger(PythonPackage):
    """A logging tool for deep learning."""

    homepage = "https://github.com/NVIDIA/dllogger"

    url = "https://github.com/NVIDIA/dllogger/archive/refs/tags/v1.0.0.tar.gz"

    version("1.0.0", sha256="abae2b2ac73b9e176fa87144bf6c2048ddd3dae8e7002d6d5a270bc7e4da6b4d")

    depends_on("py-setuptools", type="build")

