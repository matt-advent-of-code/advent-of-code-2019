import unittest

from PasswordValidator import PasswordValidator


class MyTestCase(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(PasswordValidator.is_valid_password(112233))
        self.assertTrue(PasswordValidator.is_valid_password(111122))


    def test_less_than_six_digits(self):
        self.assertFalse(PasswordValidator.is_valid_password(1))

    def test_does_not_contain_adjacent(self):
        self.assertFalse(PasswordValidator.is_valid_password(123789))
        self.assertFalse(PasswordValidator.is_valid_password(135679))

    def test_decreases(self):
        self.assertFalse(PasswordValidator.is_valid_password(223450))

    def test_too_many_repeats(self):
        self.assertFalse(PasswordValidator.is_valid_password(123444))


if __name__ == '__main__':
    unittest.main()
