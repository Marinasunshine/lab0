import unittest
from lab3.task2.src.task2 import generate_worst_case
import utils

class TestGenerateWorstCase(unittest.TestCase):

    def test_smallest_case(self):
        n = 3
        expected = [3, 2, 1]
        self.assertEqual(generate_worst_case(n), expected)

    def test_small_case(self):
        n = 5
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(generate_worst_case(n), expected)

    def test_case_with_n_equals_7(self):
        n = 7
        expected = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(generate_worst_case(n), expected)

    def test_large_case(self):
        n = 10
        expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(generate_worst_case(n), expected)

    def test_edge_case_large_n(self):
        n = 100
        expected = list(range(100, 0, -1))
        self.assertEqual(generate_worst_case(n), expected)

    def test_should_time_memory(self):
        n = 1000000
        time_start = utils.start_tracking()
        generate_worst_case(n)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 2)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()
