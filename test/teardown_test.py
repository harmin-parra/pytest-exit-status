import pytest


@pytest.fixture
def setup():
    assert False
    yield


@pytest.fixture
def teardown():
    yield
    assert False


def test_1(teardown):
    """
    Teardown
    """
    pass
