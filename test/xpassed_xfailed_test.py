import pytest


@pytest.mark.xfail(reason="xpassed")
def test_1():
    """
    XPpassed
    """
    pass


@pytest.mark.xfail(reason="xfailure")
def test_2():
    """
    XFailed
    """
    assert False
