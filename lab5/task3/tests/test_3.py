import unittest
import utils
from lab5.task3.src.task3 import process_packets

class TestProcessPackets(unittest.TestCase):

    def test_no_packets(self):
        S = 1
        packets = []
        expected = []
        self.assertEqual(process_packets(S, packets), expected)

    def test_single_packet(self):
        S = 1
        packets = [(0, 1)]
        expected = [0]
        self.assertEqual(process_packets(S, packets), expected)

    def test_two_packets_buffer_full(self):
        S = 1
        packets = [(0, 1), (0, 1)]
        expected = [0, -1]
        self.assertEqual(process_packets(S, packets), expected)

    def test_two_packets_buffer_not_full(self):
        S = 2
        packets = [(0, 1), (0, 1)]
        expected = [0, 1]
        self.assertEqual(process_packets(S, packets), expected)

    def test_sequential_packets(self):
        S = 1
        packets = [(0, 1), (1, 1)]
        expected = [0, 1]
        self.assertEqual(process_packets(S, packets), expected)

    def test_overlapping_packets(self):
        S = 2
        packets = [(0, 2), (1, 2), (2, 2)]
        expected = [0, 2, 4]
        self.assertEqual(process_packets(S, packets), expected)

    def test_large_buffer(self):
        S = 5
        packets = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        expected = [0, 1, 3, 6, 10, -1]
        self.assertEqual(process_packets(S, packets), expected)

    def test_large_input(self):
        S = 100000
        n = 100000
        packets = [(i, 1) for i in range(n)]
        expected = list(range(n))
        self.assertEqual(process_packets(S, packets), expected)

    def test_should_time_memory(self):
        S = 100000
        packets = [(i, 1) for i in range(100000)]

        time_start = utils.start_tracking()
        process_packets(S, packets)
        time, memory = utils.return_time_memory(time_start)

        self.assertLess(time, 10)
        self.assertLess(memory, 512)

if __name__ == "__main__":
    unittest.main()
