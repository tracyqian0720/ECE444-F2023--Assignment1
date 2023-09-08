# pylint: disable=all
from utils import Utils
import unittest

utils_case = Utils()

class TestUtils(unittest.TestCase):
    def test_reverse_int(self):
        self.assertEqual(utils_case.reversed(123),321)
    
    def test_reverse_str(self):
        with self.assertRaises(ValueError):
            utils_case.reversed("onetwothree")
    
    def test_reverse_float(self):
        with self.assertRaises(ValueError):
            utils_case.reversed(12.3)

    def test_formatter_int(self):
        self.assertEqual(utils_case.formatter(2),("0b10","0o2"))
    
    def test_formatter_str(self):
        with self.assertRaises(TypeError):
            utils_case.formatter("2")
    
    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils_case.formatter(2.2)
    

if __name__ == "__main__":
    unittest.main()