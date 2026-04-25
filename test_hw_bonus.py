import unittest
from hw_bonus import *
class TestFunctions(unittest.TestCase):
    def test_count_substrings(self):
        self.assertEqual(count_substrings("ababab","ab"),3)
    def test_find_smallest_divisor(self):
        self.assertEqual(find_smallest_divisor(21),3)
    def test_check_divisible_by_any(self):
        self.assertEqual(check_divisible_by_any(24,"2 3 5"),True)
    def test_find_nth_root(self):
        self.assertAlmostEqual(find_nth_root(8,3),2.0,places=3)
    def test_collatz_sequence_length(self):
        self.assertEqual(collatz_sequence_length(6),8)
if __name__=='__main__':
    unittest.main()