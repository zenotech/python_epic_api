#!/usr/bin/env python

import setuptools


from get_version import get_version
__version__ = get_version(__file__)
del get_version

if __name__ == "__main__":
    setuptools.setup(version=__version__)
