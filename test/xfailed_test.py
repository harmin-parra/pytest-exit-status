import pytest


@pytest.mark.xfail(reason="xfailed")
def test_1():
    """
    XFailed with @pytest.mark.xfail
    """
    assert False


def test_2():
    """
    XFailed with pytest.xfail
    """
    pytest.xfail("xfail")
