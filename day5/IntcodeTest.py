import unittest
import sys
from StringIO import StringIO

from Intcode import Intcode

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.intcode = Intcode()

    def test_singleAdd(self):
        expected = [2,0,0,0,99]
        initial_state = [1,0,0,0,99]

        self.assertEqual(expected, self.intcode.program(initial_state))

    def test_singleMultiply(self):
        expected = [2,3,0,6,99]
        initial_state = [2,3,0,3,99]
        self.assertEqual(expected, self.intcode.program(initial_state))

    def test_largeMultiply(self):
        expected = [2,4,4,5,99, 9801]
        initial_state = [2,4,4,5,99, 0]
        self.assertEqual(expected, self.intcode.program(initial_state))

    def test_multi(self):
        expected = [30,1,1,4,2, 5,6,0,99]
        initial_state = [1,1,1,4,99,5,6,0,99]
        self.assertEqual(expected, self.intcode.program(initial_state))

    def test_multi_with_end(self):
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        initial_state = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected, self.intcode.program(initial_state))

    def test_input_mode(self):
        expected = [1, 0, 99]
        initial_state = [3, 0, 99]
        self.assertEqual(expected, self.intcode.program(initial_state))

    def test_output_mode(self):
        inital_state = [4, 0, 99]
        self.intcode.program(inital_state)

    def test_parameter_mode(self):
        expected = [1002, 4, 3, 4, 99]
        inital_state = [1002, 4, 3, 4, 33]
        self.assertEqual(expected, self.intcode.program(inital_state))

    def test_parameter_add(self):
        expected = [1101, 100, -1, 4, 99]
        inital_state = [1101, 100, -1, 4, 0]
        self.assertEqual(expected, self.intcode.program(inital_state))

    def test_parameter_output(self):
        inital_state = [104, 0, 99]
        self.intcode.program(inital_state)



if __name__ == '__main__':
    unittest.main()
