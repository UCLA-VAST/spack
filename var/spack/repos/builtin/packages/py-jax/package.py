# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
import tempfile


class PyJax(PythonPackage, ROCmPackage):
    """JAX is Autograd and XLA, brought together for high-performance
    machine learning research. With its updated version of Autograd,
    JAX can automatically differentiate native Python and NumPy
    functions. It can differentiate through loops, branches,
    recursion, and closures, and it can take derivatives of
    derivatives of derivatives. It supports reverse-mode
    differentiation (a.k.a. backpropagation) via grad as well as
    forward-mode differentiation, and the two can be composed
    arbitrarily to any order."""

    homepage = "https://github.com/google/jax"
    pypi = "jax/jax-0.2.25.tar.gz"

    version(
        "0.4.11-rocm-enhanced",
        sha256="43add28daf5034484bb3c7dc15013cd0babd6a6ae5d27e322fdec3d6ced97d21",
        url="https://github.com/ROCmSoftwarePlatform/jax/archive/refs/tags/jaxlib-v0.4.11-rocm550.tar.gz"
    )
    version("0.4.3", sha256="d43f08f940aa30eb339965cfb3d6bee2296537b0dc2f0c65ccae3009279529ae")
    version("0.3.23", sha256="bff436e15552a82c0ebdef32737043b799e1e10124423c57a6ae6118c3a7b6cd")
    version("0.2.25", sha256="822e8d1e06257eaa0fdc4c0a0686c4556e9f33647fa2a766755f984786ae7446")

    depends_on("python@3.8:", when="@0.4:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.20:", when="@0.3:", type=("build", "run"))
    depends_on("py-numpy@1.18:", type=("build", "run"))
    depends_on("py-opt-einsum", type=("build", "run"))
    depends_on("py-scipy@1.5:", when="@0.3:", type=("build", "run"))
    depends_on("py-scipy@1.2.1:", type=("build", "run"))

    # See _minimum_jaxlib_version in jax/version.py
    jax_to_jaxlib = {
        "0.4.3": "0.4.2",
        "0.3.23": "0.3.15",
        "0.2.25": "0.1.69",
    }

    for jax, jaxlib in jax_to_jaxlib.items():
        depends_on(f"py-jaxlib@{jaxlib}:", when=f"@{jax}", type=("build", "run"))

    # Historical dependencies
    depends_on("py-absl-py", when="@:0.3", type=("build", "run"))
    depends_on("py-typing-extensions", when="@:0.3", type=("build", "run"))
    depends_on("py-etils+epath", when="@0.3", type=("build", "run"))

    # ROCm -- rocm-enhanced treats jax and jaxlib as the same package
    #         so we carry over logic from py-jaxlib
    conflicts("~rocm", when="@0.4.11-rocm-enhanced")
    conflicts("+rocm", when="@:0.4.11-a,0.4.11.0:")

    with when("@0.4.11-rocm-enhanced"):
        # jaxlib/setup.py
        depends_on("python@3.8:", when="@0.4:", type=("build", "run"))
        depends_on("py-setuptools", type="build")
        depends_on("py-numpy@1.20:", when="@0.3:", type=("build", "run"))
        depends_on("py-scipy@1.5:", type=("build", "run"))

        # .bazelversion
        depends_on("bazel@5.1.1:5.9", when="@0.3:", type="build")

    with when("+rocm"): 
        depends_on("miopen-hip")
        depends_on("hipfft")
        depends_on("rocrand")
        depends_on("hipsparse")
        depends_on("hipsolver")
        depends_on("rccl")
        depends_on("hip")
        depends_on("rocfft")
        depends_on("roctracer-dev")
        depends_on("hipblas")
        depends_on("rocm-device-libs")

    @when("@0.4.11-rocm-enhanced")
    def patch(self):
        self.tmp_path = tempfile.mkdtemp(prefix="spack")
        self.buildtmp = tempfile.mkdtemp(prefix="spack")
        filter_file(
            "build --spawn_strategy=standalone",
            f"""
# Limit CPU workers to spack jobs instead of using all HOST_CPUS.
build --spawn_strategy=standalone
build --local_cpu_resources={make_jobs}
""".strip(),
            ".bazelrc",
            string=True,
        )
        filter_file(
            'f"--output_path={output_path}",',
            'f"--output_path={output_path}",'
            f' "--sources_path={self.tmp_path}",'
            ' "--nohome_rc",'
            ' "--nosystem_rc",'
            f' "--jobs={make_jobs}",',
            "build/build.py",
            string=True,
        )
        filter_file(
            "args = parser.parse_args()",
            "args, junk = parser.parse_known_args()",
            "build/build_wheel.py",
            string=True,
        )

    @when("@0.4.11-rocm-enhanced")
    def install(self, spec, prefix):
        args = []
        args.append("build/build.py")
        if "+rocm" in spec:
            args.append("--enable_rocm")
            args.append("--rocm_path={0}".format(self.spec["hip"].prefix))
            #args.append("--bazel_options=--override_repository=xla={0}".format())
        args.append(
            "--bazel_startup_options="
            "--output_user_root={0}".format(self.wrapped_package_object.buildtmp)
        )
        python(*args)
        with working_dir(self.wrapped_package_object.tmp_path):
            args = std_pip_args + ["--prefix=" + self.prefix, "."]
            pip(*args)
        remove_linked_tree(self.wrapped_package_object.tmp_path)
        remove_linked_tree(self.wrapped_package_object.buildtmp)
