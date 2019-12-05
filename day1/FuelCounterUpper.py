class FuelCounterUpper:
    def __init__(self):
        pass

    @staticmethod
    def calculate(mass):
        return mass / 3 - 2

    @staticmethod
    def calculate_total(masses):
        return sum([FuelCounterUpper.calculate(fuel) for fuel in masses])


if __name__ == '__main__':
    fuel_counter = FuelCounterUpper()
    f = open("FuelCounterInput.txt")
    print fuel_counter.calculate_total([int(line) for line in f.readlines()])
    f.close()
