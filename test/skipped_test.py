import pytest


@pytest.mark.skip(reason="passed")
def test_7():
    """
    Skipped with @pytest.mark.skip
    """
    pass


def test_8():
    """
    Skipped with pytest.skip
    """
    pytest.skip("skip")
