from pandas import DataFrame
from ._version import __version__


def foo():
    return DataFrame([[1, 2, 3], [4, 5, 6]], columns=list('abc'))
