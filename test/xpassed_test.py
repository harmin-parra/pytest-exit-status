import pytest


@pytest.mark.xfail(reason="xpassed")
def test_1():
    """
    XPpassed with @pytest.mark.xfail
    """
    pass
