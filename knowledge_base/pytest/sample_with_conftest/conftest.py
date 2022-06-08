import pytest
from fixture_outside_conftest import my_fix_outside_conftest

@pytest.fixture()
def my_fix():
    print("this should print before the test runs")

@pytest.fixture()
def my_fix1():
    print("this will be the setup")
    yield
    print("and here comes teardown")