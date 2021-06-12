from samplelib import foo, __version__


def test_foo():
    df = foo()
    assert list(df.columns) == ['a', 'b', 'c']


def test_version():
    print(__version__)
    assert __version__ == '0.0.0'
