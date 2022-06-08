def test_single_fix(my_fix):
    print("this comes from the test")
    assert True

def test_both_fix(my_fix, my_fix1):
    print("this is from the second test with two fix")
    assert True

def test_fix_outside_conf(my_fix_outside_conftest):
    print("this is to check if the non conftest fix was called")
    assert True