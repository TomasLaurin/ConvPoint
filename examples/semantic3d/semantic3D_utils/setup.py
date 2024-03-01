from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os
import numpy

ext_modules = [Extension(
    "semantic3D",
    sources=["Semantic3D.pyx", "Sem3D.cxx",],
    include_dirs=["./", numpy.get_include()],
    language="c++",
    extra_compile_args=['/std:c++latest', '/openmp'] if os.name == 'nt' else ["-std=c++11", "-fopenmp"],
    extra_link_args=['/openmp'] if os.name == 'nt' else ['-fopenmp'],
  )]

setup(
    name="Semantic3D_utils",
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
)
