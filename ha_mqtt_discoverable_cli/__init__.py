from importlib import metadata

__version__ = metadata.version(__package__)


def module_version():
    print(__version__)
