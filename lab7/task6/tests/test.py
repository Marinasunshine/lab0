import unittest
from random import randint
import utils
from lab7.task6.src.task6 import longest_lengths


class TestLIS(unittest.TestCase):

    def test_should_example(self):
        # given
        sequence = [3, 5, 3, 5, 28, 6]
        expected_length = 3

        # when
        result_length, _ = longest_lengths(sequence)

        # then
        self.assertEqual(result_length, expected_length)

    def test_should_time_memory(self):
        # given
        sequence = [randint(-10**9, 10**9) for i in range(1000)]
        time_start = utils.start_tracking()

        # when
        longest_lengths(sequence)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()
