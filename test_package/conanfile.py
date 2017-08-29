# pylint: disable=missing-docstring
from os import (
    chdir,
    sep
)
from conans import ConanFile, CMake


class DABIPTestConan(ConanFile):
    name = 'libdabip package test'
    version = '1.0.2'
    description = 'The Conan.io package test for libdabip'
    settings = (
        'arch',
        'build_type',
        'compiler',
        'os',
    )
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory)
        cmake.build()

    def test(self):
        chdir('bin')
        self.run('.{separator}package_test'.format(**{
            'separator': sep
        }))
