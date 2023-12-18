""" Module with Password class """
import string


class ValidationException(Exception):
    """
    Custom exception class to represent validation errors in the Password class.
    It is raised when the password fails one or more validation checks.
    """


class Password:
    """
    The Password class represents a user password and provides various methods
    to validate its strength. It checks for password length, presence of numbers,
     special characters, uppercase and lowercase characters.
    """
    def __init__(self, user_password):
        """
        Initializes a new Password object with the given user password.

        :param user_password: The user's password to be validated.
        :type user_password: str
        """
        self.user_password = user_password

    def correct_length(self):
        """
        Checks if the password has a minimum length of 8 characters.

        :return: True if the password has a minimum length of 8 characters.
        :rtype: bool
        :raises ValidationException: If the password is too short.
        """

        if len(self.user_password) >= 8:
            return True

        raise ValidationException('Password is to short')

    def at_least_one_number(self):
        """
        Checks if the password contains at least one digit.

        :return: True if the password contains at least one digit.
        :rtype: bool
        :raises ValidationException: If at least one digit is missing.
        """
        numbers = '0123456789'
        for letter in self.user_password:
            if letter in numbers:
                return True

        raise ValidationException('Missing at least one number')

    def at_least_one_special_character(self):
        """
        Checks if the password contains at least one special character.

        :return: True if the password contains at least one special character.
        :rtype: bool
        :raises ValidationException: If at least one special character is missing.
        """
        spec_char = string.punctuation
        for letter in self.user_password:
            if letter in spec_char:
                return True

        raise ValidationException('Missing at least one special character')

    def upper_and_lower_characters(self):
        """
        Checks if the password contains at least one uppercase letter and one lowercase letter.

        :return: True if the password contains at least one uppercase and one lowercase letter.
        :rtype: bool
        :raises ValidationException: If at least one uppercase or one lowercase letter is missing.
        """
        is_lower = any(letter.islower() for letter in self.user_password)
        is_upper = any(letter.isupper() for letter in self.user_password)

        if is_lower and is_upper:
            return True
        if is_lower and not is_upper:
            raise ValidationException('Missing at least one upper character')
        if is_upper and not is_lower:
            raise ValidationException('Missing at least one lower character')
