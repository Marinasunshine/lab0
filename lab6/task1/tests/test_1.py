import unittest
import utils
from lab6.task1.src.task1 import set_operations


class SetTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = ["Y", "N", "N"]

        # when
        commands = ["A 2", "A 5", "A 3", "? 2", "? 4", "A 2", "D 2", "? 2"]
        result = set_operations(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        time_start = utils.start_tracking()

        # when
        commands = [f"A {i}" for i in range(5 * 10**4)] + [f"? {i}" for i in range(5 * 10**4)]
        result = set_operations(commands)

        # then
        time, memory = utils.return_time_memory(time_start)
        self.assertLess(time, 2)
        self.assertLess(memory, 256)


if __name__ == '__main__':
    unittest.main()


