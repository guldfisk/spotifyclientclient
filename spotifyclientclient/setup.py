import os

from setuptools import setup


def package_files(directory):
    paths = []
    for path, directories, file_names in os.walk(directory):
        for filename in file_names:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('spotifyclientclient')

setup(
    name = 'spotifyclientclient',
    version = '1.0',
    packages = ['spotifyclientclient'],
    package_data = {'': extra_files},
    include_package_data = True,
)
