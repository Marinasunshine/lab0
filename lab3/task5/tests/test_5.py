import unittest
from lab3.task5.src.task5 import h_index
import utils

class TestHIndex(unittest.TestCase):

    def test_smallest_case(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        self.assertEqual(h_index(citations), expected)

    def test_small_case(self):
        citations = [1, 3, 1]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_case_with_n_equals_4(self):
        citations = [10, 8, 5, 4, 3]
        expected = 4
        self.assertEqual(h_index(citations), expected)

    def test_case_with_n_equals_5(self):
        citations = [100, 90, 80, 70, 60]
        expected = 5
        self.assertEqual(h_index(citations), expected)

    def test_case_with_decreasing_citations(self):
        citations = [7, 6, 5, 4, 3, 2, 1]
        expected = 4
        self.assertEqual(h_index(citations), expected)

    def test_edge_case_large_citations(self):
        citations = [0] * 1000 + [1]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_should_time_memory(self):
        citations = [i for i in range(5000, 0, -1)]  # Large case
        time_start = utils.start_tracking()
        h_index(citations)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 2)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()
