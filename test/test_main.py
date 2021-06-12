import samplelib
from samplelib import foo
from importlib.metadata import version
__version__ = "2.0.1.dev3+c45a11d"  # expected version of the module


def test_foo():
    df = foo()
    assert list(df.columns) == ['a', 'b', 'c']


def test_version():
    print(samplelib.__version__)
    assert samplelib.__version__ == __version__


def test_metadata_version():
    print(version('samplelib'))
