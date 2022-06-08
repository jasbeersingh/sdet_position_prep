import pytest

@pytest.fixture()
def some_fix1():
    print("setup1")
    yield
    print("teardown 1")


@pytest.fixture()
def some_fix2():
    print("setup2")
    yield
    print("td2")

def test_sometest(some_fix1, some_fix2):
    print("testing method")
    assert True