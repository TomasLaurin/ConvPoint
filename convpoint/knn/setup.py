from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy
import os

ext_modules = [Extension(
    "nearest_neighbors",
    sources=["knn.pyx", "knn_.cxx"],  # source file(s)
    include_dirs=["./", numpy.get_include()],
    language="c++",
    extra_compile_args=['/std:c++ latest', '/openmp'] if os.name == 'nt' else ["-std=c++11", "-fopenmp"],
    extra_link_args=['/openmp'] if os.name == 'nt' else ['-fopenmp'],
)]

setup(
    name="KNN NanoFLANN",
    ext_modules=cythonize(ext_modules, language_level="3str"),
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
    script_args=["build_ext", "--build-lib", "lib/python/"],
)