import unittest
from Lesson_9_task_2 import *


class PhonebookTest(unittest.TestCase):
    def test_adding(self):
        correct_answer = {
          "First name": "Andrei",
          "Last name": "Korotenko",
          "Phone number": "+380667641139",
          "City": "Hlobyne",
          "State": "Poltava"
         }
        self.assertDictEqual(add_new_entries(), correct_answer)

    def test_search_by_firstname(self):
        correct_answer = {
          "First name": "Andrei",
          "Last name": "Korotenko",
          "Phone number": "+380667641139",
          "City": "Hlobyne",
          "State": "Poltava"
         }
        self.assertDictEqual(search_by_first_name('Andrei'), correct_answer)

    def test_search_by_lastname(self):
        correct_answer = {
          "First name": "Andrei",
          "Last name": "Korotenko",
          "Phone number": "+380667641139",
          "City": "Hlobyne",
          "State": "Poltava"
        }
        self.assertDictEqual(search_by_last_name('Korotenko'), correct_answer)

    def test_search_by_fullname(self):
        correct_answer = {
            "First name": "Andrei",
            "Last name": "Korotenko",
            "Phone number": "+380667641139",
            "City": "Hlobyne",
            "State": "Poltava"
        }
        self.assertDictEqual(search_by_full_name('Andrei Korotenko'), correct_answer)

    def test_search_by_telephone_number(self):
        correct_answer = {
            "First name": "Andrei",
            "Last name": "Korotenko",
            "Phone number": "+380667641139",
            "City": "Hlobyne",
            "State": "Poltava"
        }
        self.assertDictEqual(search_by_telephone_number('+380667641139'), correct_answer)

    def test_search_by_city_or_state(self):
        correct_answer = {
            "First name": "Andrei",
            "Last name": "Korotenko",
            "Phone number": "+380667641139",
            "City": "Hlobyne",
            "State": "Poltava"
        }
        self.assertDictEqual(search_by_city_or_state('Hlobyne', 'Poltava'), correct_answer)

    def test_update_record(self):
        correct_answer = {
            "First name": "1",
            "Last name": "1",
            "Phone number": "1",
            "City": "1",
            "State": "1"
        }
        self.assertDictEqual(update_record(1), correct_answer)

    def test_delete_telephone_number(self):
        correct_answer = {
            "First name": "1",
            "Last name": "1",
            "Phone number": "1",
            "City": "1",
            "State": "1"
        }
        self.assertDictEqual(delete_telephone_number(1), correct_answer)


if __name__ == '__main__':
    unittest.main()
