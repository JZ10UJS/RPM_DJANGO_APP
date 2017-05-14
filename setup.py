import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.dirname(__file__)))

setup(
    name='django-scan',
    version='0.1',
    packages=['Learning', 'api', 'scan'],
    include_package_data=True,
    license='MIT License',
    author='J_z10',
)
