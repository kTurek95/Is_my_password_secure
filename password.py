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

    def at_least_one_special_character(self):
        spec_char = '!@#$%^&*<>?|()'
        for letter in self.user_password:
            if letter in spec_char:
                return True

        raise ValidationException('Missing at least one special character')

    def upper_and_lower_characters(self):
        is_lower = any(letter.islower() for letter in self.user_password)
        is_upper = any(letter.isupper() for letter in self.user_password)

        if is_lower and is_upper:
            return True
        if is_lower and not is_upper:
            raise ValidationException('Missing at least one upper character')
        if is_upper and not is_lower:
            raise ValidationException('Missing at least one lower character')
