import unittest
from Lesson_14_task_1 import *


class MyTestCase(unittest.TestCase):
    def test_add_func(self):
        self.assertEqual(add(1, 2), 3)

    def test_square_all_func(self):
        self.assertEqual(square_all(2, 3), [4, 9])


if __name__ == '__main__':
    unittest.main()
