import unittest
import utils
from lab7.task7.src.task7 import is_match


class TemplateTest(unittest.TestCase):

    def test_should_example(self):
        # given
        expected_result = "YES"

        # when
        result = is_match("k?t*n", "kitten")

        # then
        self.assertEqual(result, expected_result)

    def test_should_time_memory(self):
        # given
        template = "a?s*e"*100
        word = "asdce"*100
        time_start = utils.start_tracking()

        # when
        is_match(template, word)
        result = utils.return_time_memory(time_start)

        # then
        self.assertLess(result[0], 2)
        self.assertLess(result[1], 256)


if __name__ == '__main__':
    unittest.main()



