''' Module with tests for Password class '''

import pytest
from password import Password, ValidationException


def test_correct_length_positive():
    correct_password = Password('Kacper123')

    assert Password.correct_length(correct_password) is True


def test_correct_length_negative():
    wrong_password = Password('Kacper')

    with pytest.raises(ValidationException) as error:
        wrong_password.correct_length()

    assert 'Password is to short' in str(error.value)


def test_at_least_one_number_positive():
    correct_password = Password('Kacp3r')

    assert Password.at_least_one_number(correct_password) is True


def test_at_least_one_number_negative():
    wrong_password = Password('Kacper')

    with pytest.raises(ValidationException) as error:
        wrong_password.at_least_one_number()

    assert 'Missing at least one number' in str(error.value)


def test_at_least_one_special_character_positive():
    correct_password = Password('Kacp#r')

    assert Password.at_least_one_special_character(correct_password) is True


def test_at_least_one_special_character_negative():
    wrong_password = Password('Kacper')

    with pytest.raises(ValidationException):
        wrong_password.at_least_one_special_character()

    assert 'Missing at least one special character'


def test_upper_and_lower_characters_positive():
    correct_password = Password('Kacper')

    assert Password.upper_and_lower_characters(correct_password) is True


def test_upper_and_lower_characters_negative_lower():
    upper_password = Password('KACPER')

    with pytest.raises(ValidationException) as error:
        upper_password.upper_and_lower_characters()

    assert 'Missing at least one lower character' in str(error.value)


def test_upper_and_lower_characters_negative_upper():
    lower_password = Password('kacper')

    with pytest.raises(ValidationException) as error:
        lower_password.upper_and_lower_characters()

    assert 'Missing at least one upper character' in str(error.value)
