import unittest
import utils
from lab4.task1.src.task1 import stacks

class TestStacks(unittest.TestCase):

    def test_empty_commands(self):
        commands = []
        expected = []
        self.assertEqual(stacks(commands), expected)

    def test_single_push_and_pop(self):
        commands = [
            "+ 10",
            "-"
        ]
        expected = [10]
        self.assertEqual(stacks(commands), expected)

    def test_multiple_push_and_pop(self):
        commands = [
            "+ 1",
            "+ 2",
            "+ 3",
            "-",
            "-",
            "-"
        ]
        expected = [3, 2, 1]
        self.assertEqual(stacks(commands), expected)

    def test_alternating_push_and_pop(self):
        commands = [
            "+ 5",
            "-",
            "+ 7",
            "-",
            "+ 9",
            "-"
        ]
        expected = [5, 7, 9]
        self.assertEqual(stacks(commands), expected)

    def test_large_input(self):
        n = 10**6
        commands = [f"+ {i}" for i in range(1, n + 1)] + ["-"] * n
        expected = list(range(n, 0, -1))
        self.assertEqual(stacks(commands), expected)

    def test_should_time_memory(self):
        n = 10**6
        commands = [f"+ {i}" for i in range(1, n + 1)] + ["-"] * n

        time_start = utils.start_tracking()
        stacks(commands)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 2)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()
