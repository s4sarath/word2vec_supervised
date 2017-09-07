from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Word2Vec Supervised App',
  ext_modules = cythonize("word2vec_inner_supervised.pyx"),
)