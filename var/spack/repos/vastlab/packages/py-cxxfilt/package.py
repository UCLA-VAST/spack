# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCxxfilt(PythonPackage):
    """Demangling C++ symbols in Python / interface to abi::__cxa_demangle"""

    homepage = "https://github.com/afq984/python-cxxfilt"
    pypi = "cxxfilt/cxxfilt-0.3.0.tar.gz"

    version("0.3.0", sha256="7df6464ba5e8efbf0d8974c0b2c78b32546676f06059a83515dbdfa559b34214")

    depends_on("py-setuptools", type="build")
    depends_on("py-pytest", type="test")
