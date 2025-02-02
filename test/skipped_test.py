import pytest


@pytest.mark.skip(reason="reason passed")
def test_1():
    """
    Skipped with @pytest.mark.skip
    """
    pass


def test_2():
    """
    Skipped with pytest.skip
    """
    pytest.skip("reason skip")
