import unittest
from random import randint
from lab7.task4.src.task4 import length
import utils

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_example_1(self):
        # Given
        seq1 = [2, 7, 5]
        seq2 = [2, 5]
        expected_result = 2

        # When
        result = length(seq1, seq2)

        # Then
        self.assertEqual(result, expected_result)

    def test_example_2(self):
        # Given
        seq1 = [1, 2, 3, 4]
        seq2 = [7]
        expected_result = 0

        # When
        result = length(seq1, seq2)

        # Then
        self.assertEqual(result, expected_result)

    def test_example_3(self):
        # Given
        seq1 = [2, 7, 6, 3]
        seq2 = [5, 2, 8, 7]
        expected_result = 2

        # When
        result = length(seq1, seq2)

        # Then
        self.assertEqual(result, expected_result)

    def test_large_input(self):
        # Given
        n, m = 100, 100
        seq1 = [randint(-10**9, 10**9) for _ in range(n)]
        seq2 = [randint(-10**9, 10**9) for _ in range(m)]

        # When
        time_start = utils.start_tracking()
        result = length(seq1, seq2)
        elapsed_time, memory_usage = utils.return_time_memory(time_start)

        # Then
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLess(elapsed_time, 1)

if __name__ == '__main__':
    unittest.main()


