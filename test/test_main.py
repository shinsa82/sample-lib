import samplelib
from samplelib import foo

__version__ = "2.0.1.dev2+74b5115"  # expected version of the module


def test_foo():
    df = foo()
    assert list(df.columns) == ['a', 'b', 'c']


def test_version():
    print(samplelib.__version__)
    assert samplelib.__version__ == __version__
