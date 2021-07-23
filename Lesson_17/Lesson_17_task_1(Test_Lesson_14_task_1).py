import unittest
import Lesson_14_task_1


class MyTestCase(unittest.TestCase):
    def test_add_func(self):
        self.assertEqual(Lesson_14_task_1.add(1, 2), 3)

    def test_square_all_func(self):
        self.assertEqual(Lesson_14_task_1.square_all(2, 3), [4, 9])


if __name__ == '__main__':
    unittest.main()
