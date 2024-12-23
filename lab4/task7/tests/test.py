import unittest
from lab4.task7.src.task7 import find_max
import utils

class TestFindMax(unittest.TestCase):

    def test_single_element_window(self):
        n = 5
        arr = [4, 3, 2, 1, 5]
        m = 1
        expected = [4, 3, 2, 1, 5]
        self.assertEqual(find_max(n, arr, m), expected)

    def test_window_size_one(self):
        n = 6
        arr = [3, 5, 7, 2, 8, 6]
        m = 1
        expected = [3, 5, 7, 2, 8, 6]
        self.assertEqual(find_max(n, arr, m), expected)

    def test_window_size_equals_array_length(self):
        n = 6
        arr = [3, 5, 7, 2, 8, 6]
        m = 6
        expected = [8]
        self.assertEqual(find_max(n, arr, m), expected)

    def test_window_size_mid_range(self):
        n = 8
        arr = [7, 5, 6, 6, 3, 1, 5, 2]
        m = 4
        expected = [7, 6, 6, 6, 5]
        self.assertEqual(find_max(n, arr, m), expected)

    def test_should_time_memory(self):
        n = 100000
        arr = [i % 1000 for i in range(n)]
        m = 100

        time_start = utils.start_tracking()
        find_max(n, arr, m)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 5)
        self.assertLess(memory, 512)

if __name__ == "__main__":
    unittest.main()
