from hashlib import sha1
from requests import get
from password import Password, ValidationException


class Api(Password):
    def __init__(self, user_password):
        super().__init__(user_password)
        self.sha_password = self.convert_password_into_sha()

    def __str__(self):
        return self.user_password

    def convert_password_into_sha(self):
        sha_password = sha1(self.user_password.encode('utf-8'))
        return sha_password.hexdigest()

    def connect_with_api(self):
        response = get('https://api.pwnedpasswords.com/range/' + self.sha_password[:5].upper())
        api_answer = response.text
        return api_answer
