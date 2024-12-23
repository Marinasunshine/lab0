import unittest
import utils
from lab2.task2.src.task2 import merge_sort

class MergeSortTest(unittest.TestCase):

    def test_should_example_1(self):
        # given
        input_data = [9, 7, 5, 8]
        expected_result = [5, 7, 8, 9]

        # when
        output = merge_sort(input_data, 0, len(input_data) - 1)

        # then
        self.assertEqual(output, expected_result)

    def test_should_example_2(self):
        # given
        input_data = [1, 2, 1, 8, 3, 6, 3, 4]
        expected_result = [1, 1, 2, 3, 3, 4, 6, 8]

        # when
        output = merge_sort(input_data, 0, len(input_data) - 1)

        # then
        self.assertEqual(output, expected_result)

    def test_should_edge_case_single_element(self):
        # given
        input_data = [1]
        expected_result = [1]

        # when
        output = merge_sort(input_data, 0, len(input_data) - 1)

        # then
        self.assertEqual(output, expected_result)

    def test_should_edge_case_empty(self):
        # given
        input_data = []
        expected_result = []

        # when
        output = merge_sort(input_data, 0, len(input_data) - 1)

        # then
        self.assertEqual(output, expected_result)


    def test_should_time_memory(self):
        # given
        input_data = [i for i in range(100000, 0, -1)]
        time_start = utils.start_tracking()

        # when
        merge_sort(input_data, 0, len(input_data) - 1)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 3)
        self.assertLess(result[1], 256)

if __name__ == '__main__':
    unittest.main()
