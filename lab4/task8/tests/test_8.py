import unittest
from lab4.task8.src.task8 import postfix
import utils

class TestPostfix(unittest.TestCase):

    def test_single_number(self):
        data = ["5"]
        expected = 5
        self.assertEqual(postfix(data), expected)

    def test_simple_addition(self):
        data = ["3", "4", "+"]
        expected = 7
        self.assertEqual(postfix(data), expected)

    def test_simple_subtraction(self):
        data = ["10", "3", "-"]
        expected = 7
        self.assertEqual(postfix(data), expected)

    def test_simple_multiplication(self):
        data = ["6", "2", "*"]
        expected = 12
        self.assertEqual(postfix(data), expected)

    def test_combination_operations(self):
        data = ["3", "4", "+", "2", "*"]
        expected = 14
        self.assertEqual(postfix(data), expected)

    def test_complex_expression(self):
        data = ["8", "9", "+", "1", "7", "-", "*"]
        expected = -102
        self.assertEqual(postfix(data), expected)

    def test_edge_case_large_numbers(self):
        data = ["-102", "8", "9", "+", "1", "7", "-", "*"]
        expected = -102
        self.assertEqual(postfix(data), expected)

    def test_should_time_memory(self):
        data = ["1000000", "999999", "+", "100000", "*"] * 10000

        time_start = utils.start_tracking()
        postfix(data)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 2)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()
