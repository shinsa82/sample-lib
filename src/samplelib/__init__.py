from pandas import DataFrame


def foo():
    return DataFrame([[1, 2, 3], [4, 5, 6]], columns=list('abc'))
