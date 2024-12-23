import unittest
from lab3.task3.src.task3 import scarecrow_sort
import utils


class TestScarecrowSort(unittest.TestCase):

    def test_smallest_case(self):
        n, k = 3, 2
        matr = [2, 1, 3]
        expected = "НЕТ"
        self.assertEqual(scarecrow_sort(n, k, matr), expected)

    def test_small_case(self):
        n, k = 5, 3
        matr = [1, 5, 3, 4, 1]
        expected = "ДА"
        self.assertEqual(scarecrow_sort(n, k, matr), expected)

    def test_case_with_n_equals_7_and_k_3(self):
        n, k = 7, 3
        matr = [6, 2, 7, 1, 8, 5, 4]
        expected = "НЕТ"
        self.assertEqual(scarecrow_sort(n, k, matr), expected)

    def test_case_with_n_equals_8_and_k_4(self):
        n, k = 8, 4
        matr = [5, 2, 8, 6, 3, 1, 7, 4]
        expected = "НЕТ"
        self.assertEqual(scarecrow_sort(n, k, matr), expected)

    def test_large_case(self):
        n, k = 100, 10
        matr = [i % 100 for i in range(100, 0, -1)]
        expected = "НЕТ"
        self.assertEqual(scarecrow_sort(n, k, matr), expected)

    def test_edge_case_large_k(self):
        n, k = 100, 50
        matr = [i % 100 for i in range(100, 0, -1)]
        expected = "НЕТ"
        self.assertEqual(scarecrow_sort(n, k, matr), expected)

    def test_should_time_memory(self):
        n, k = 1000000, 100
        matr = [i % 1000 for i in range(1000000)]

        time_start = utils.start_tracking()
        scarecrow_sort(n, k, matr)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 2)
        self.assertLess(memory, 256)


if __name__ == "__main__":
    unittest.main()
