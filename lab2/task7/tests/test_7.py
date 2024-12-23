import unittest
from lab2.task7.src.task7 import max_sub

class MaxSubarrayTest(unittest.TestCase):

    def test_should_return_max_subarray(self):
        data = [7, -5, 8, 3, -6, -8, 5, 2, -6, 9]
        expected_result = [7, -5, 8, 3]
        result = max_sub(data)
        self.assertEqual(result, expected_result)

    def test_all_negative(self):
        data = [-7, -5, -8, -3, -6]
        expected_result = [-3]
        result = max_sub(data)
        self.assertEqual(result, expected_result)

    def test_single_element(self):
        data = [5]
        expected_result = [5]
        result = max_sub(data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


