import unittest
import utils
from lab6.task5.src.task5 import vote

class TestVote(unittest.TestCase):

    def test_single_candidate(self):
        data = [
            "McCain 10",
            "McCain 5",
            "McCain 1"
        ]
        expected = ["McCain 16"]
        self.assertEqual(vote(data), expected)

    def test_multiple_candidates(self):
        data = [
            "McCain 10",
            "Obama 9",
            "Obama 8",
            "McCain 5"
        ]
        expected = ["McCain 15", "Obama 17"]
        self.assertEqual(vote(data), expected)

    def test_lexicographical_order(self):
        data = [
            "ivanov 100",
            "ivanov 500",
            "ivanov 300",
            "petr 70",
            "tourist 1",
            "tourist 2"
        ]
        expected = ["ivanov 900", "petr 70", "tourist 3"]
        self.assertEqual(vote(data), expected)

    def test_single_vote(self):
        data = [
            "bur 1"
        ]
        expected = ["bur 1"]
        self.assertEqual(vote(data), expected)

    def test_should_time_memory(self):
        time_start = utils.start_tracking()

        data = [f"candidate{i % 10} {i}" for i in range(10**5)]
        vote(data)

        time, memory = utils.return_time_memory(time_start)
        self.assertLess(time, 2)
        self.assertLess(memory, 64)

if __name__ == '__main__':
    unittest.main()
