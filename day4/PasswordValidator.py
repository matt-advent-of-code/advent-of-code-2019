import re

class PasswordValidator:
    @staticmethod
    def is_valid_password(password):
        return ( len(str(password)) == 6 and PasswordValidator.__contains_adjacent_repeating_digets(password) and PasswordValidator.__is_increasing(password))

    @staticmethod
    def __contains_adjacent_repeating_digets(password):
        password_as_string = str(password)
        for char in password_as_string:
            if re.search(char+"{2}", password_as_string) and not re.search(char+"{3}", password_as_string):
                return True
        return False


    @staticmethod
    def __is_increasing(password):
        password_as_string = str(password)
        for i in range(0, len(password_as_string) - 1):
            if password_as_string[i] > password_as_string[i+1]:
                return False
        return True

if __name__ == '__main__':
    number_of_valid_passwords = 0
    for password in range(235741, 706948+1):
        if PasswordValidator.is_valid_password(password):
            number_of_valid_passwords += 1

    print number_of_valid_passwords
