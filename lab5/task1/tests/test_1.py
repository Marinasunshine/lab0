import unittest
import utils
from lab5.task1.src.task1 import check_heap

class TestCheckHeap(unittest.TestCase):

    def test_valid_heap(self):
        arr = [1, 3, 2, 5, 4]
        expected = "YES"
        self.assertEqual(check_heap(arr), expected)

    def test_invalid_heap(self):
        arr = [0, 1, 2, 0]
        expected = "NO"
        self.assertEqual(check_heap(arr), expected)

    def test_single_element(self):
        arr = [5]
        expected = "YES"
        self.assertEqual(check_heap(arr), expected)

    def test_large_heap(self):
        arr = [i for i in range(1, 100001)]
        expected = "YES"
        self.assertEqual(check_heap(arr), expected)

    def test_large_invalid_heap(self):
        arr = [1] + [0] * 99999
        expected = "NO"
        self.assertEqual(check_heap(arr), expected)

    def test_should_time_memory(self):
        time_start = utils.start_tracking()

        arr = [i for i in range(1, 10**4 + 1)]
        check_heap(arr)

        time, memory = utils.return_time_memory(time_start)
        self.assertLess(time, 2)
        self.assertLess(memory, 256)

if __name__ == '__main__':
    unittest.main()
