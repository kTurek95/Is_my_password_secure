import pytest
from api import Api, ValidationException


def test_convert_password_into_sha():
    password = Api('xxKacper95xx')

    assert Api.convert_password_into_sha(password) == '648126664f89b27eeb9b0b1a582ccf2ffb15a808'
    assert Api.convert_password_into_sha(password) != '4f1409094bc13fbc83da59de3e8c76d25ce3f74e'


def test_connect_with_api_correct_result(requests_mock):
    api = Api('xxKacper95xx')
    answer = '0086D41786E17D694D9962FFD119C10DD11'
    requests_mock.get('https://api.pwnedpasswords.com/range/64812', text=answer)

    assert api.connect_with_api() == answer


def test_connect_with_api_wrong_result(requests_mock):
    api = Api('xxKacper95xx')
    answer = '0086D41786E17D694D9962FFD119C10DD11'
    wrong_answer = 'FBE8E9E1EEF65CAF99132693F75EF4145E7'
    requests_mock.get('https://api.pwnedpasswords.com/range/64812', text=answer)

    assert api.connect_with_api() != wrong_answer


def test_check_if_password_not_in_api_answer_positive(requests_mock):
    not_in_api = Api('xxKacper95xx')
    not_in_api.convert_password_into_sha()
    true_answer = '0086D41786E17D694D9962FFD119C10DD11'
    requests_mock.get('https://api.pwnedpasswords.com/range/64812', text=true_answer)

    assert not_in_api.check_if_password_not_in_api() is True


def test_check_if_password_not_in_api_answer_negative(requests_mock):
    in_api = Api('polska!23')
    in_api.convert_password_into_sha()
    false_answer = '098CB812DEC5ADD17B97107B34B70134DCF408BF'
    requests_mock.get('https://api.pwnedpasswords.com/range/098CB', text=false_answer)

    with pytest.raises(ValidationException) as error:
        in_api.check_if_password_not_in_api()
        assert 'You have to change yor password!' in str(error.value)


