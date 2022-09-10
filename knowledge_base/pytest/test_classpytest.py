class TestWithAClass(object):
    def setUp(self):
        print(" this happened before test")
        
    def test_1(self):
        assert True

    def test_2(self):
        assert False

class TestWithAnotherClass(object):
    def test4(self):
        assert True

    def test5(self):
        assert False