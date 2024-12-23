import unittest
from lab1.task4.src.task4 import lin_search


class LinearSearchTest(unittest.TestCase):

    def test_should_example(self):
        # given
        array = [1,2,3,4,5,6,7,8,7,7]
        expected_result = (3, [6, 8, 9])

        # when
        result = lin_search(array, 7)

        # then
        self.assertEqual(expected_result, result)

    def test_should_no_target_in_array(self):
        # given
        array = [x for x in range(10**3)]
        expected_result = -1

        # when
        result = lin_search(array, [])

        # then
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()