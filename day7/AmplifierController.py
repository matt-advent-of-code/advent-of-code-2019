from day5.Intcode import Intcode
import itertools

class AmplifierController:
    def calculate_signal(self, sequence, setting_sequence):
        input_signal = 0
        for i in range(0, 5):
            phase_setting = setting_sequence[i]
            intcode = Intcode()
            intcode.input = [phase_setting, input_signal]
            intcode.program(sequence)
            input_signal = intcode.output[0]
        return input_signal

    def calculate_larget_signal(self, sequence):
        setting_sequences = list(self.get_permutations())
        max_output = 0
        for setting_sequence in setting_sequences:
            output = self.calculate_signal(sequence, setting_sequence)
            if output > max_output:
                max_output = output
        return max_output


    def get_permutations(self):
        setting_sequene = [0, 1, 2, 3, 4]
        for s in range(0, len(setting_sequene) + 1):
            for subset in itertools.permutations(setting_sequene, s):
                if len(subset) == len(setting_sequene):
                    yield list(subset)


if __name__ == '__main__':
    f = open("input.txt")
    sequence = [ int(pos) for pos in f.readline().split(",")]
    f.close()
    amplifier_controller = AmplifierController()
    print amplifier_controller.calculate_larget_signal(sequence)