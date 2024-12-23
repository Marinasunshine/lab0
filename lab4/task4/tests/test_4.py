import unittest
import utils
from lab4.task4.src.task4 import brackets

class TestBrackets(unittest.TestCase):

    def test_empty_string(self):
        s = ""
        expected = "Success"
        self.assertEqual(brackets(s), expected)

    def test_single_bracket(self):
        s = "("
        expected = 1
        self.assertEqual(brackets(s), expected)

    def test_correct_brackets(self):
        s = "[()]{}{[()()]()}"
        expected = "Success"
        self.assertEqual(brackets(s), expected)

    def test_missing_closing_bracket(self):
        s = "{"
        expected = 1
        self.assertEqual(brackets(s), expected)

    def test_unmatched_closing_bracket(self):
        s = "{[}]"
        expected = 3
        self.assertEqual(brackets(s), expected)

    def test_nested_brackets(self):
        s = "foo(bar[i);"
        expected = 10
        self.assertEqual(brackets(s), expected)

    def test_large_input_success(self):
        s = "[" * 50000 + "]" * 50000
        expected = "Success"
        self.assertEqual(brackets(s), expected)

    def test_large_input_error(self):
        s = "[" * 50000 + ")" * 50000
        expected = 50001
        self.assertEqual(brackets(s), expected)

    def test_should_time_memory(self):
        s = "[" * 50000 + "]" * 50000

        time_start = utils.start_tracking()
        brackets(s)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 5)
        self.assertLess(memory, 256)

if __name__ == "__main__":
    unittest.main()
