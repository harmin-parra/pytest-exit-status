import pytest


@pytest.fixture
def setup():
    assert False
    yield


@pytest.fixture
def teardown():
    yield
    assert False


class TestClass:

    def test_01(self):
        """
        Passed test
        """
        pass

    def test_02(self):
        """
        Failed test
        """
        x = 2 / 0

    def test_03(self):
        """
        Failed with pytest.fail
        """
        pytest.fail("reason fail")

    @pytest.mark.xfail(reason="reason xpassed")
    def test_04(self):
        """
        XPassed
        """
        pass

    @pytest.mark.xfail(reason="reason xfailure")
    def test_05(self):
        """
        XFailed with @pytest.mark.xfail
        """
        assert False

    def test_06(self):
        """
        XFailed with pytest.xfail
        """
        pytest.xfail("reason xfail")

    @pytest.mark.skip(reason="reason passed")
    def test_07(self):
        """
        Skipped with @pytest.mark.skip
        """
        pass

    def test_08(self):
        """
        Skipped with pytest.skip
        """
        pytest.skip("reason skip")

    def test_09(self, setup):
        """
        Setup
        """
        pass

    def test_10(self, teardown):
        """
        Teardown
        """
        pass
