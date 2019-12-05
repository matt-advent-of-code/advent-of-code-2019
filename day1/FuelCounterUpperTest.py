import unittest
from FuelCounterUpper import FuelCounterUpper


class FuelCounterUpperTestCase(unittest.TestCase):
    def test_getFuelDivisibleByThree(self):
        fuel_counter = FuelCounterUpper()
        self.assertEqual(2, fuel_counter.calculate(mass=12))

    def test_getFuelNotDivisibleByThree(self):
        fuel_counter = FuelCounterUpper()
        self.assertEqual(2, fuel_counter.calculate(mass=14))

    def test_largeNumber(self):
        fuel_counter = FuelCounterUpper()
        self.assertEqual(654, fuel_counter.calculate(mass=1969))

    def test_largerNumber(self):
        fuel_counter = FuelCounterUpper()
        self.assertEqual(33583, fuel_counter.calculate(mass=100756))

    def test_calculateList(self):
        fuel_counter = FuelCounterUpper()
        self.assertEqual(4, fuel_counter.calculate_total([12, 14]))


if __name__ == '__main__':
    unittest.main()
