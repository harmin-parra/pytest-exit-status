import pytest


def test_1():
    """
    Passed test
    """
    pass


@pytest.mark.xfail(reason="xpassed")
def test_2():
    """
    XPpassed with @pytest.mark.xfail
    """
    pass
