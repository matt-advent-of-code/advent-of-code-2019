import sys

class Intcode:
    END_OPERATOR = 99

    def __init__(self):
        pass

    @staticmethod
    def program(inital_state):
        result_state = list(inital_state)
        Intcode.__program(result_state, 0)
        return result_state

    @staticmethod
    def __program(state, operator_index):
        operator = state[operator_index]
        if operator != Intcode.END_OPERATOR:
            first = state[operator_index + 1]
            second = state[operator_index + 2]
            index_to_replace = state[operator_index + 3]
            modified_value = Intcode.__calculate_new_value(operator, state[first], state[second])
            state[index_to_replace] = modified_value
            Intcode.__program(state, operator_index+4)

    @staticmethod
    def __calculate_new_value(operator, first, second):
        if operator == 1:
            return first + second
        else:
            return first * second

if __name__ == '__main__':
    for noun in range(0, 99):
        for verb in range(0, 99):
            f = open("input.txt")
            state = [ int(pos) for pos in f.readline().split(",")]
            f.close()
            state[1] = noun
            state[2] = verb
            state = Intcode.program(state)
            if state[0] == 19690720:
                print 100 * noun + verb
                sys.exit()