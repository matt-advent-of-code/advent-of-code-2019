import unittest

from day7.AmplifierController import AmplifierController


class MyTestCase(unittest.TestCase):
    def test_calculate_signal(self):
        sequence = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        setting_sequence = [4,3,2,1,0]
        amplifier_controller = AmplifierController()
        output_signal = amplifier_controller.calculate_signal(sequence, setting_sequence)
        self.assertEqual(43210, output_signal)

    def test_calculate_signal2(self):
        sequence = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        setting_sequence = [0,1,2,3,4]
        amplifier_controller = AmplifierController()
        output_signal = amplifier_controller.calculate_signal(sequence, setting_sequence)
        self.assertEqual(54321, output_signal)

    def test_calculate_signal3(self):
        sequence = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        setting_sequence = [1,0,4,3,2]
        amplifier_controller = AmplifierController()
        output_signal = amplifier_controller.calculate_signal(sequence, setting_sequence)
        self.assertEqual(65210, output_signal)

    def test_larget_signal(self):
        sequence = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        amplifier_controller = AmplifierController()
        output_signal = amplifier_controller.calculate_larget_signal(sequence)
        self.assertEqual(43210, output_signal)


    def test_larget_signal2(self):
        sequence = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        amplifier_controller = AmplifierController()
        output_signal = amplifier_controller.calculate_larget_signal(sequence)
        self.assertEqual(54321, output_signal)

    def test_larget_signal3(self):
        sequence = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        amplifier_controller = AmplifierController()
        output_signal = amplifier_controller.calculate_larget_signal(sequence)
        self.assertEqual(65210, output_signal)

if __name__ == '__main__':
    unittest.main()
