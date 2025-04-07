import pytest


@pytest.fixture
def setup():
    assert False
    yield


@pytest.fixture
def teardown():
    yield
    assert False


def test_01():
    """
    Passed test
    """
    pass


def test_02():
    """
    Failed test
    """
    assert False


def test_03():
    """
    Failed with pytest.fail
    """
    pytest.fail("reason fail")


@pytest.mark.xfail(reason="reason xpassed")
def test_04():
    """
    XPassed
    """
    pass


@pytest.mark.xfail(reason="reason xfailure")
def test_05():
    """
    XFailed with @pytest.mark.xfail
    """
    assert False


def test_06():
    """
    XFailed with pytest.xfail
    """
    pytest.xfail("reason xfail")


@pytest.mark.skip(reason="reason skipped")
def test_07():
    """
    Skipped with @pytest.mark.skip
    """
    pass


def test_08():
    """
    Skipped with pytest.skip
    """
    pytest.skip("reason skipped")


def test_09(setup):
    """
    Setup
    """
    pass


def test_10(teardown):
    """
    Teardown
    """
    pass
