import pytest


def test_1():
    """
    Passed test
    """
    pass


@pytest.mark.xfail(reason="reason xpassed")
def test_2():
    """
    XPassed
    """
    pass


@pytest.mark.xfail(reason="reason xfailure")
def test_3():
    """
    XFailed with @pytest.mark.xfail
    """
    x = 2 / 0


def test_4():
    """XFailed with pytest.xfail"""
    pytest.xfail("reason xfail")
