import unittest
from lab3.task1.src.task1 import randomized_quick_sort_best
from utils import worst_array

class QuickSortTest(unittest.TestCase):

    def test_should_quick_sort(self):
        expected_result = [n for n in range(1, 10**4+1)]
        data = worst_array(10**4)

        result = randomized_quick_sort_best(data, 0, len(data)-1)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()