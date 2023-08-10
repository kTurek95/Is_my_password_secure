"""Module with test for Api class"""
import pytest
from api import Api, ValidationException


def test_convert_password_into_sha():
    """
    Tests the convert_password_into_sha() function of the Api class.
    Checks if the function correctly converts a password into the SHA-1 hash.

    Expected values:
    - The password 'xxKacper95xx' should be converted to '648126664f89b27eeb9b0b1a582ccf2ffb15a808'.
    """
    password = Api('xxKacper95xx')

    assert Api.convert_password_into_sha(password) == '648126664f89b27eeb9b0b1a582ccf2ffb15a808'
    assert Api.convert_password_into_sha(password) != '4f1409094bc13fbc83da59de3e8c76d25ce3f74e'


def test_connect_with_api_correct_result(requests_mock):
    """
    Tests the connect_with_api() function of the Api class with the correct result.
    Checks if the function correctly connects to the API and returns the expected result.

    Expected values:
    - The API response for the range '64812' should be '0086D41786E17D694D9962FFD119C10DD11'.
    """
    api = Api('xxKacper95xx')
    answer = '0086D41786E17D694D9962FFD119C10DD11'
    requests_mock.get('https://api.pwnedpasswords.com/range/64812', text=answer)

    assert api.connect_with_api() == answer


def test_connect_with_api_wrong_result(requests_mock):
    """
    Tests the connect_with_api() function of the Api class with an incorrect result.
    Checks if the function correctly connects to the API and returns a result different from the expected one.

    Expected values:
    - The API response for the range '64812' should not be 'FBE8E9E1EEF65CAF99132693F75EF4145E7'.
    """
    api = Api('xxKacper95xx')
    answer = '0086D41786E17D694D9962FFD119C10DD11'
    wrong_answer = 'FBE8E9E1EEF65CAF99132693F75EF4145E7'
    requests_mock.get('https://api.pwnedpasswords.com/range/64812', text=answer)

    assert api.connect_with_api() != wrong_answer


def test_check_if_password_not_in_api_answer_positive(requests_mock):
    """
   Tests the check_if_password_not_in_api() function of the Api class with a positive result.
   Checks if the function correctly indicates the absence of the password in the API response.

   Expected values:
   - The check_if_password_not_in_api() function should return True, as the password 'xxKacper95xx' does not exist in the API response.
   """
    not_in_api = Api('xxKacper95xx')
    not_in_api.convert_password_into_sha()
    true_answer = '0086D41786E17D694D9962FFD119C10DD11'
    requests_mock.get('https://api.pwnedpasswords.com/range/64812', text=true_answer)

    assert not_in_api.check_if_password_not_in_api() is True


def test_check_if_password_not_in_api_answer_negative(requests_mock):
    """
    Tests the check_if_password_not_in_api() function of the Api class with a negative result.
    Checks if the function correctly handles the case when the password exists in the API response.

    Expected values:
    - The check_if_password_not_in_api() function should raise a ValidationException with the appropriate message.
    """
    in_api = Api('polska!23')
    in_api.convert_password_into_sha()
    false_answer = '098CB812DEC5ADD17B97107B34B70134DCF408BF'
    requests_mock.get('https://api.pwnedpasswords.com/range/098CB', text=false_answer)

    with pytest.raises(ValidationException) as error:
        in_api.check_if_password_not_in_api()
        assert 'You have to change yor password!' in str(error.value)


