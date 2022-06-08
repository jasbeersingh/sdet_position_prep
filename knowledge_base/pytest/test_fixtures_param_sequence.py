import pytest

@pytest.fixture()
def dummy_val1():
    print("returning dummy val")
    return "val1"


@pytest.fixture()
def dummy_val2():
    return "val2"

def test_check_param_sequence(dummy_val1, dummy_val2):
    print(dummy_val1)
    print(dummy_val2)
    assert True
