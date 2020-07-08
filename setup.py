from setuptools import setup
import os
import sys
import json
from shutil import copy

_here = os.path.abspath(os.path.dirname(__file__))

sys.path.append('AutomatedCICD/')
import version

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

pythonPath = os.path.join('lib','python{}.{}'.format(*sys.version_info[:2]),'site-packages','AutomatedCICD')
setup(
    name='AutomatedCICD',
    version=version.version(),
    description=('Testing software for automatic upload to git when successful pr.'),
    long_description=long_description,
    author='Jakob Lass',
    author_email='lass.jakob@gmail.com',
    packages=['AutomatedCICD'],
    package_dir={'AutomatedCICD': 'AutomatedCICD'},
    package_data={'AutomatedCICD': ['version.txt']},
    data_files=[('AutomatedCICD', ['AutomatedCICD/version.txt'])],
    url='https://github.com/Jakob-Lass/AutomatedCICD',
    license='MPL-2.0',
    python_requires='>=3.5,<=3.7'
    )
