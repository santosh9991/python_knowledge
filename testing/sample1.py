def add(a,b):
    return a+b
import unittest
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(add(2,4),6)
        self.assertEqual(add(1,3), 4)
if __name__ == '__main__':
    unittest.main()
