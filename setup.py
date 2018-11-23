from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name="sum_seq",
    version="0.0.1",
    python_requires=">=3.7",
    packages=["sum_seq", "sum_seq.python", "sum_seq.cython", "sum_seq.c"],
    ext_modules=[Extension("sum_seq.c.sum_seq", sources=["./sum_seq/c/_sum_seq.c", "./sum_seq/c/sum_seq.c"])] +\
                cythonize(
                    "sum_seq/cython/sum_seq.pyx",
                    compiler_directives={"language_level": 3}
                ),
)
