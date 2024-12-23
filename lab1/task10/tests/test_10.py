import unittest
import utils
from lab1.task10.src.task10 import palindrome

class LongestPalindromeTest(unittest.TestCase):

    def test_should_example_1(self):
        # given
        input_data = ("AAB")
        expected_result = "ABA"

        # when
        result = palindrome(input_data)

        # then
        self.assertEqual(expected_result, result)

    def test_should_example_2(self):
        # given
        input_data = ("QAZQAZ")
        expected_result = "AQZZQA"

        # when
        result = palindrome(input_data)

        # then
        self.assertEqual(expected_result, result)

    def test_should_example_3(self):
        # given
        input_data = ("A")
        expected_result = "A"

        # when
        result = palindrome(input_data)

        # then
        self.assertEqual(expected_result, result)

    def test_should_edge_case_empty(self):
        # given
        input_data = ("")
        expected_result = ""

        # when
        result = palindrome(input_data)

        # then
        self.assertEqual(expected_result, result)

    def test_should_time_memory(self):
        # given
        input_data = ("A" * 100000)
        time_start = utils.start_tracking()

        # when
        palindrome(input_data)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 1)
        self.assertLess(result[1], 64)

if __name__ == '__main__':
    unittest.main()