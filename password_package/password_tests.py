""" Module with tests for Password class """
import pytest
from password import Password, ValidationException


def test_correct_length_positive():
    """
    Tests the correct_length() method of the Password class with a valid password length.
    Checks if the method returns True when the password has the correct length.
    """
    correct_password = Password('Kacper123')

    assert Password.correct_length(correct_password) is True


def test_correct_length_negative():
    """
   Tests the correct_length() method of the Password class with an invalid password length.
   Checks if the method raises a ValidationException with an appropriate message when the password is too short.
   """
    wrong_password = Password('Kacper')

    with pytest.raises(ValidationException) as error:
        wrong_password.correct_length()

    assert 'Password is to short' in str(error.value)


def test_at_least_one_number_positive():
    """
    Tests the at_least_one_number() method of the Password class with a valid password containing at least one number.
    Checks if the method returns True when the password contains at least one number.
    """
    correct_password = Password('Kacp3r')

    assert Password.at_least_one_number(correct_password) is True


def test_at_least_one_number_negative():
    """
    Tests the at_least_one_number() method of the Password class with an invalid password missing numbers.
    Checks if the method raises a ValidationException with an appropriate message when the password does not contain any numbers.
    """
    wrong_password = Password('Kacper')

    with pytest.raises(ValidationException) as error:
        wrong_password.at_least_one_number()

    assert 'Missing at least one number' in str(error.value)


def test_at_least_one_special_character_positive():
    """
   Tests the at_least_one_special_character() method of the Password class with a valid password containing at least one special character.
   Checks if the method returns True when the password contains at least one special character.
   """
    correct_password = Password('Kacp#r')

    assert Password.at_least_one_special_character(correct_password) is True


def test_at_least_one_special_character_negative():
    """
   Tests the at_least_one_special_character() method of the Password class with an invalid password missing special characters.
   Checks if the method raises a ValidationException with an appropriate message when the password does not contain any special characters.
   """
    wrong_password = Password('Kacper')

    with pytest.raises(ValidationException):
        wrong_password.at_least_one_special_character()

    assert 'Missing at least one special character'


def test_upper_and_lower_characters_positive():
    """
    Tests the upper_and_lower_characters() method of the Password class with a valid password containing both upper and lower characters.
    Checks if the method returns True when the password contains both upper and lower characters.
    """
    correct_password = Password('Kacper')

    assert Password.upper_and_lower_characters(correct_password) is True


def test_upper_and_lower_characters_negative_lower():
    """
    Tests the upper_and_lower_characters() method of the Password class with an invalid password missing lowercase characters.
    Checks if the method raises a ValidationException with an appropriate message when the password does not contain any lowercase characters.
    """
    upper_password = Password('KACPER')

    with pytest.raises(ValidationException) as error:
        upper_password.upper_and_lower_characters()

    assert 'Missing at least one lower character' in str(error.value)


def test_upper_and_lower_characters_negative_upper():
    """
   Tests the upper_and_lower_characters() method of the Password class with an invalid password missing uppercase characters.
   Checks if the method raises a ValidationException with an appropriate message when the password does not contain any uppercase characters.
   """
    lower_password = Password('kacper')

    with pytest.raises(ValidationException) as error:
        lower_password.upper_and_lower_characters()

    assert 'Missing at least one upper character' in str(error.value)
