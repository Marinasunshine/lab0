import unittest
from lab2.task3.src.task3 import merge_sort

class CountInversesTest(unittest.TestCase):

    def test_should_count_inverses(self):
        expected_result = 17
        data = [1,8,2,1,4,7,3,2,3,6]

        sort, result = merge_sort(data)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()