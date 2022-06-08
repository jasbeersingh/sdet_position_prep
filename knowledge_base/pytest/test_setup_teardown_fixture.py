import pytest

@pytest.fixture()
def my_fixture():
    print("this is setup")
    yield
    print("this is teardown")


def test_sometest(my_fixture):
    print("this is test_execution")
    assert True