import unittest
from lab2.task4.src.task4 import binary_search

class BinSearchTest(unittest.TestCase):

    def test_should_bin_search(self):
        expected_result = [2,0,-1,0,-1]
        data = [[1,5,8,12,13],[8,1,23,1,11]]

        result = [binary_search(data[0], number) for number in data[1]]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()