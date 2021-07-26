import unittest
from Lesson_19_task_1 import ConManager, mycon


class TestConManager(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, ConManager.counter)

    def test_2(self):
        self.assertEqual('test.txt', mycon.file_name)
