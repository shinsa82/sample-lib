from samplelib import foo


def test_foo():
    df = foo()
    assert list(df.columns) == ['a', 'b', 'c']
