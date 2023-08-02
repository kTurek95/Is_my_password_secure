class ValidationException(Exception):
    pass


class Password:
    def __init__(self, user_password):
        self.user_password = user_password

    def correct_length(self):
        if len(self.user_password) >= 8:
            return True

        raise ValidationException('Password is to short')

    def at_least_one_number(self):
        numbers = '0123456789'
        for letter in self.user_password:
            if letter in numbers:
                return True

        raise ValidationException('Missing at least one number')
