import unittest
import teachercode

class TestCountMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(teachercode.add(2, 2), 4)

    def test_multiply(self):
        self.assertEqual(teachercode.multiply(1, 4), 4)
        self.assertEqual(teachercode.multiply(10, 6), 60)

    def test_power(self):
        self.assertEqual(teachercode.power(2, 8), 256)

if __name__ == '__main__':
    unittest.main()