import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'hyperoperation/hyperoperation.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="hyperoperation",
    version=__version__,
    description="Dummy test for Python3",
    py_modules=['hyperoperation.hyperoperation'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
