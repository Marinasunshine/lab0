import unittest
import utils
from lab4.task5.src.task5 import stack_max

class TestStackMax(unittest.TestCase):

    def test_empty_commands(self):
        commands = []
        expected = []
        self.assertEqual(stack_max(commands), expected)

    def test_single_push_and_max(self):
        commands = [
            ["push", "10"],
            ["max"]
        ]
        expected = ["10"]
        self.assertEqual(stack_max(commands), expected)

    def test_multiple_push_pop_and_max(self):
        commands = [
            ["push", "2"],
            ["push", "1"],
            ["max"],
            ["pop"],
            ["max"]
        ]
        expected = ["2", "2"]
        self.assertEqual(stack_max(commands), expected)

    def test_large_input_success(self):
        n = 100000
        commands = [["push", str(i)] for i in range(1, n + 1)] + [["max"], ["pop"]] * n
        expected = [str(i) for i in range(n, 0, -1)]
        self.assertEqual(stack_max(commands), expected)

    def test_mixed_operations(self):
        commands = [
            ["push", "5"],
            ["push", "1"],
            ["push", "7"],
            ["max"],
            ["pop"],
            ["max"]
        ]
        expected = ["7", "5"]
        self.assertEqual(stack_max(commands), expected)

    def test_should_time_memory(self):
        n = 100000
        commands = [["push", str(i)] for i in range(1, n + 1)] + [["max"], ["pop"]] * n

        time_start = utils.start_tracking()
        stack_max(commands)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 5)
        self.assertLess(memory, 512)

if __name__ == "__main__":
    unittest.main()
