import pytest


def test_1():
    """
    Passed test
    """
    pass


@pytest.mark.xfail(reason="xpassed")
def test_2():
    """
    XPassed
    """
    pass


@pytest.mark.xfail(reason="xfailure")
def test_3():
    """
    XFailed with @pytest.mark.xfail
    """
    assert False


def test_4():
    """XFailed with pytest.xfail"""
    pytest.xfail("xfail")
