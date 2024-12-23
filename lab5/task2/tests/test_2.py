import unittest
import utils
from lab5.task2.src.task2 import find_height

class TestFindHeight(unittest.TestCase):

    def test_single_node(self):
        parents = [-1]
        n = 1
        expected = 1
        self.assertEqual(find_height(parents, n), expected)

    def test_small_tree(self):
        parents = [4, -1, 4, 1, 1]
        n = 5
        expected = 3
        self.assertEqual(find_height(parents, n), expected)

    def test_another_small_tree(self):
        parents = [-1, 0, 4, 0, 3]
        n = 5
        expected = 4
        self.assertEqual(find_height(parents, n), expected)

    def test_linear_tree(self):
        parents = [-1, 0, 1, 2, 3]
        n = 5
        expected = 5
        self.assertEqual(find_height(parents, n), expected)

    def test_star_tree(self):
        parents = [-1, 0, 0, 0, 0]
        n = 5
        expected = 2
        self.assertEqual(find_height(parents, n), expected)

    def test_large_tree(self):
        n = 10**5
        parents = [-1] + [0] * (n - 1)
        expected = 2
        self.assertEqual(find_height(parents, n), expected)

    def test_large_linear_tree(self):
        n = 10**5
        parents = [-1] + [i for i in range(n - 1)]
        expected = n
        self.assertEqual(find_height(parents, n), expected)

    def test_should_time_memory(self):
        n = 10**5
        parents = [-1] + [0] * (n - 1)

        time_start = utils.start_tracking()
        find_height(parents, n)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 3)
        self.assertLess(memory, 512)

if __name__ == '__main__':
    unittest.main()
