import pytest


@pytest.mark.xfail(reason="xfailed")
def test_1():
    """
    XFailed
    """
    assert False
