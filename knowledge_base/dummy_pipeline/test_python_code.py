import python_code

import unittest

class TestPythonCode(unittest.TestCase):
    def test_func1(self):
        val = python_code.func1()
        self.assertEqual("Hello", val)

    def test_func2(self):
        val = python_code.func2()
        self.assertEqual(" world", val)


if __name__ == "__main__":
    unittest.main()
