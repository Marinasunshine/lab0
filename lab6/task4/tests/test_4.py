import unittest
import utils
from lab6.task4.src.task4 import array_command

class TestArrayCommand(unittest.TestCase):

    def test_put_and_get(self):
        commands = [
            "put zero a",
            "put one b",
            "put two c",
            "get zero",
            "get one",
            "get two"
        ]
        expected = ["a", "b", "c"]
        self.assertEqual(array_command(commands), expected)

    def test_get_not_found(self):
        commands = [
            "get unknown"
        ]
        expected = ["<none>"]
        self.assertEqual(array_command(commands), expected)

    def test_delete_and_get(self):
        commands = [
            "put zero a",
            "delete zero",
            "get zero"
        ]
        expected = ["<none>"]
        self.assertEqual(array_command(commands), expected)

    def test_prev_and_next(self):
        commands = [
            "put one b",
            "put two c",
            "put three d",
            "prev two",
            "next two",
            "prev one",
            "next three"
        ]
        expected = ["b", "d", "<none>", "<none>"]
        self.assertEqual(array_command(commands), expected)

    def test_complex_operations(self):
        commands = [
            "put one b",
            "put two c",
            "put three d",
            "delete two",
            "get two",
            "prev three",
            "next one"
        ]
        expected = ["<none>", "b", "d"]
        self.assertEqual(array_command(commands), expected)

    def test_should_time_memory(self):
        time_start = utils.start_tracking()

        commands = [f"put key{i} value{i}" for i in range(5 * 10**4)] + [f"get key{i}" for i in range(5 * 10**4)]
        array_command(commands)

        time, memory = utils.return_time_memory(time_start)
        self.assertLess(time, 4)
        self.assertLess(memory, 256)

if __name__ == '__main__':
    unittest.main()