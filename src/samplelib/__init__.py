from pandas import DataFrame

__version__ = "0.0.0"


def foo():
    return DataFrame([[1, 2, 3], [4, 5, 6]], columns=list('abc'))
