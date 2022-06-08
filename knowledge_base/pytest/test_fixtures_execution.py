import pytest

@pytest.fixture(scope="module")
def my_fixture():
    print("this fixture is called regardsless of whether a test exists or not.")


def test_sometest(my_fixture):
    print("not calling fixture just to see if its executed or not")
    assert True

print("conclusion: the fixture was not called if the method didn't call out for it.")