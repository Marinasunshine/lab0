import unittest
from lab2.task1.src.task1 import merge_sort
from utils import worst_array

class MergeSortTest(unittest.TestCase):

    def test_should_merge_sort(self):
        expected_result = [n for n in range(1, 2*10**4+1)]
        data = worst_array(2*10**4)

        result = merge_sort(data)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()