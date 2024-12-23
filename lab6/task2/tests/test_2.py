import unittest
import utils
from lab6.task2.src.task2 import phonebook_manager

class TestPhoneBookManager(unittest.TestCase):

    def test_add_and_find(self):
        commands = [
            "add 911 police",
            "add 76213 Mom",
            "add 17239 Bob",
            "find 76213",
            "find 911",
            "find 17239"
        ]
        expected = ["Mom", "police", "Bob"]
        self.assertEqual(phonebook_manager(commands), expected)

    def test_find_not_found(self):
        commands = [
            "find 910"
        ]
        expected = ["not found"]
        self.assertEqual(phonebook_manager(commands), expected)

    def test_delete_and_find(self):
        commands = [
            "add 911 police",
            "del 911",
            "find 911"
        ]
        expected = ["not found"]
        self.assertEqual(phonebook_manager(commands), expected)

    def test_overwrite_contact(self):
        commands = [
            "add 76213 Mom",
            "add 76213 daddy",
            "find 76213"
        ]
        expected = ["daddy"]
        self.assertEqual(phonebook_manager(commands), expected)

    def test_complex_operations(self):
        commands = [
            "add 123456 me",
            "add 0 granny",
            "find 0",
            "find 123456",
            "del 0",
            "find 0",
            "del 0",
            "find 0"
        ]
        expected = ["granny", "me", "not found", "not found"]
        self.assertEqual(phonebook_manager(commands), expected)

    def test_should_time_memory(self):
        time_start = utils.start_tracking()

        commands = [f"add {i} name{i}" for i in range(5 * 10**4)] + [f"find {i}" for i in range(5 * 10**4)]
        phonebook_manager(commands)

        time, memory = utils.return_time_memory(time_start)
        self.assertLess(time, 6)
        self.assertLess(memory, 512)

if __name__ == '__main__':
    unittest.main()