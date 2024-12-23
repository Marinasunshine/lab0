import unittest
import utils
from lab5.task6.src.task6 import priority_queue

class TestPriorityQueue(unittest.TestCase):

    def test_empty_operations(self):
        operations = []
        expected = []
        self.assertEqual(priority_queue(operations), expected)

    def test_add_and_extract_min(self):
        operations = [
            "A 3",
            "A 2",
            "X",
            "X"
        ]
        expected = ["2", "3"]
        self.assertEqual(priority_queue(operations), expected)

    def test_extract_from_empty(self):
        operations = [
            "X"
        ]
        expected = ["*"]
        self.assertEqual(priority_queue(operations), expected)

    def test_decrease_key(self):
        operations = [
            "A 3",
            "A 5",
            "A 4",
            "D 2 1",
            "X",
            "X",
            "X"
        ]
        expected = ["3", "1", "5"]
        self.assertEqual(priority_queue(operations), expected)

    def test_large_input(self):
        n = 10**4
        operations = [f"A {i}" for i in range(n, 0, -1)] + ["X"] * n
        expected = [str(i) for i in range(1, n + 1)]
        self.assertEqual(priority_queue(operations), expected)

    def test_mixed_operations(self):
        operations = [
            "A 3",
            "X",
            "X",
            "A 4",
            "A 2",
            "X",
            "D 1 1",
            "X"
        ]
        expected = ["3", "*", "2", "1"]
        self.assertEqual(priority_queue(operations), expected)

    def test_should_time_memory(self):
        n = 10**4
        operations = [f"A {i}" for i in range(n, 0, -1)] + ["X"] * n

        time_start = utils.start_tracking()
        priority_queue(operations)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 2)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()
