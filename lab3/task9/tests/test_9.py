import unittest
from lab3.task9.src.task9 import find_closest_pair
import utils

class TestFindClosestPair(unittest.TestCase):

    def test_smallest_case(self):
        points = [(0, 0), (3, 4)]
        expected = 5.0
        self.assertAlmostEqual(find_closest_pair(points), expected, places=4)

    def test_multiple_pairs(self):
        points = [(7, 7), (1, 100), (4, 8), (7, 7)]
        expected = 0.0
        self.assertAlmostEqual(find_closest_pair(points), expected, places=4)

    def test_case_with_negative_coords(self):
        points = [(4, 4), (-2, -2), (-3, -4), (-1, 3)]
        expected = 2.23606797749979
        self.assertAlmostEqual(find_closest_pair(points), expected, places=4)

    def test_case_with_duplicate_points(self):
        points = [(-1, -1), (-2, -2), (-2, 4), (-1, 3)]
        expected = 1.41421356
        self.assertAlmostEqual(find_closest_pair(points), expected, places=4)

    def test_edge_case_large_points(self):
        points = [(0, 0)] * 1000 + [(1, 1)]
        expected = 0.0
        self.assertAlmostEqual(find_closest_pair(points), expected, places=4)

    def test_should_time_memory(self):
        points = [(i, i * i) for i in range(5000, 0, -1)]
        time_start = utils.start_tracking()
        find_closest_pair(points)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 10)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()