#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from setuptools import Command


class ReleaseCommand(Command):
    """Release options"""
    description = 'Set release options'
    user_options = [('version=', None, 'sets the version, default is 0.1')]

    def initialize_options(self):
        self.version = None

    def finalize_options(self):
        pass

    def run(self):
        if self.version is not None:
            self.distribution.metadata.version = self.version


class CleanCommand(Command):
    """Clean package"""
    description = 'clean package'
    user_options = [('all', None, 'clean all, default is build only')]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        self.all = self.all is not None

    def run(self):
        workdir = os.path.dirname(os.path.abspath(__file__))
        os.system('rm -rf ' + os.path.join(workdir, 'build'))
        if self.all:
            os.system('rm -rf ' + os.path.join(workdir, 'mdeploy.egg-info'))
            os.system('rm -rf ' + os.path.join(workdir, 'dist'))


setup(
    name='mdeploy',
    version='0.1',
    description='Marbles Deployment Helpers',
    author='Tom Tracy',
    author_email = "support@marbles.ai",
    license='Marbles AI Proprietary License',
    url='http://www.marbles.ai',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    packages=find_packages(exclude=['*.test', '*.test.*', 'test.*', '*.log']),
    install_requires=[
        'boto3',
        'watchtower',
    ],
    include_package_data=False,
    cmdclass={
        'clean': CleanCommand,
        'release': ReleaseCommand,
    },
    zip_safe=False,
)
