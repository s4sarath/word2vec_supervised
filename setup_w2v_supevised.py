from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

import numpy

setup(
  name = 'Word2vec_Supervised',
  ext_modules = cythonize("word2vec_inner_supervised.pyx"),
   cmdclass = {'build_ext': build_ext},
  language="c++",
  include_dirs=[numpy.get_include()]
)