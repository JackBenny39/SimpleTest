import unittest

from SimpleTest import simplepy

class TestSimple(unittest.TestCase):
    
    def test_summer(self):
        in_arr = [1,2,3]
        test_sum = simplepy.summer(in_arr) 
        self.assertEqual(test_sum, 6)
