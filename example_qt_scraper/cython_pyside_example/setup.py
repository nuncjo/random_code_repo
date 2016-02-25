from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="CythonExample",
    ext_modules=cythonize("*.pyx"),
)
