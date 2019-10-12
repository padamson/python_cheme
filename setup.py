from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'cheme', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='cheme',
    version=version['__version__'],
    description='Introduction to python for chemical engineers.',
    long_description=('Demonstrate the power of python for chemical' +
                      'engineering applications.'),
    author='Paul Adamson',
    author_email='paul.adamson@nrl.navy.mil',
    license='',
    packages=['cheme'],
    include_package_data=True,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    classifiers=[
        'Development Status :: 1 - Development',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7'],
    )
