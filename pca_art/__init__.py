from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pca_art")
except PackageNotFoundError:
    # package is not installed
    pass
