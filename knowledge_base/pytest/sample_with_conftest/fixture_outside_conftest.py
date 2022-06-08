# I'll try using this by importing it into the conftest file

import pytest

@pytest.fixture()
def my_fix_outside_conftest():
    print("This fixture is defined in another file and imported into conftest")