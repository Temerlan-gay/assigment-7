import unittest
from hw import *
class TestHomeWork7(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2),True)
    def test_nth_fibonacci(self):
        self.assertEqual(nth_fibonacci(6),5)
    def test_factorial(self):
        self.assertEqual(factorial(5),120)
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"),2)
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345),15)
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"),"olleh")
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(4),30)
    def test_is_leap_year(self):
        self.assertEqual(is_leap_year(2000),True)
    def test_count_words(self):
        self.assertEqual(count_words("Hello world"),2)
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("racecar"),True)
    def test_sum_of_multiples(self):
        self.assertEqual(sum_of_multiples(10,3,5),33)
    def test_gcd(self):
        self.assertEqual(gcd(56,98),14)
    def test_lcm(self):
        self.assertEqual(lcm(6,8),24)
    def test_count_characters(self):
        self.assertEqual(count_characters("hello","l"),2)
    def test_digit_count(self):
        self.assertEqual(digit_count(123),3)
    def test_is_power_of_two(self):
        self.assertEqual(is_power_of_two(8),True)
    def test_sum_of_cubes(self):
        self.assertEqual(sum_of_cubes(3),36)
    def test_is_perfect_square(self):
        self.assertEqual(is_perfect_square(9),True)
    def test_is_armstrong_number(self):
        self.assertEqual(is_armstrong_number(153),True)
if __name__=='__main__':
    unittest.main()