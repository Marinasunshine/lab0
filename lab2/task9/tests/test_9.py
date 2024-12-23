import unittest
import numpy
from lab2.task9.src.task9 import matrix_mult
from lab2.task9.src.task9_1 import strassen

class MatrixMultiplicationTest(unittest.TestCase):

    def test_2x2_matrices(self):
        n = 2
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]

        result_naive = matrix_mult(n, A, B)
        self.assertEqual(result_naive, expected_result)

        result_strassen = strassen(A, B)
        self.assertEqual(result_strassen, expected_result)


    def test_identity_matrix(self):
        n = 2
        A = [[1, 2], [3, 4]]
        B = [[1, 0], [0, 1]]
        expected_result = A

        result_naive = matrix_mult(n, A, B)
        self.assertEqual(result_naive, expected_result)

        result_strassen = strassen(A, B)
        self.assertEqual(result_strassen, expected_result)

    def test_large_matrix(self):
        n = 4
        A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        B = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        expected_result = [[10, 10, 10, 10], [26, 26, 26, 26], [42, 42, 42, 42], [58, 58, 58, 58]]

        result_naive = matrix_mult(n, A, B)
        self.assertEqual(result_naive, expected_result)

        result_strassen = strassen(A, B)
        self.assertEqual(result_strassen, expected_result)


if __name__ == '__main__':
    unittest.main()
