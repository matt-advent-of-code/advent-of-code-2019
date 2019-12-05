import unittest
from Intcode import Intcode


class MyTestCase(unittest.TestCase):
    def test_singleAdd(self):
        expected = [2,0,0,0,99]
        initial_state = [1,0,0,0,99]
        self.assertEqual(expected, Intcode.program(initial_state))

    def test_singleMultiply(self):
        expected = [2,3,0,6,99]
        initial_state = [2,3,0,3,99]
        self.assertEqual(expected, Intcode.program(initial_state))

    def test_largeMultiply(self):
        expected = [2,4,4,5,99, 9801]
        initial_state = [2,4,4,5,99, 0]
        self.assertEqual(expected, Intcode.program(initial_state))

    def test_multi(self):
        expected = [30,1,1,4,2, 5,6,0,99]
        initial_state = [1,1,1,4,99,5,6,0,99]
        self.assertEqual(expected, Intcode.program(initial_state))

    def test_multi_with_end(self):
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        initial_state = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected, Intcode.program(initial_state))

if __name__ == '__main__':
    unittest.main()
