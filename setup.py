import os
from setuptools import setup

rq = 'requirements'
rq_list = []
if os.path.exists(rq):
    with open(rq) as f:
        rq_list = f.read().split()

os.chdir(os.path.normpath(os.path.dirname(__file__)))

setup(
    name='django-scan',
    version='0.1',
    packages=['Learning', 'api', 'scan'],
    include_package_data=True,
    license='MIT License',
    author='J_z10',
    install_requires=rq_list if rq_list else None
)
