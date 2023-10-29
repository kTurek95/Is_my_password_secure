""" Module with Api class """

from hashlib import sha1
from requests import get
from password import Password, ValidationException


class Api(Password):
    """
    A class representing an API connection with password checking using SHA-1 hash.

    """
    def __init__(self, user_password):
        """
        Initializes a new Api instance with the provided user password.

        Args:
            user_password (str): The user's password.
        """
        super().__init__(user_password)
        self.sha_password = self.convert_password_into_sha()

    def __str__(self):
        """
        Returns the user's password as a string.

        Returns:
            str: The user's password.
        """
        return self.user_password

    def convert_password_into_sha(self):
        """
        Converts the user's password into its SHA-1 hash.

        Returns:
            str: The SHA-1 hash of the user's password.
        """
        sha_password = sha1(self.user_password.encode('utf-8'))
        return sha_password.hexdigest()

    def connect_with_api(self):
        """
        Connects to the API using the SHA-1 hash of the password.

        Returns:
            str: The response from the API.
        """
        response = get('https://api.pwnedpasswords.com/range/' + self.sha_password[:5].upper())
        api_answer = response.text
        return api_answer

    def check_if_password_not_in_api(self):
        """
       Checks if the password's hash is compromised in the API.

       Raises:
           ValidationException: If the password's hash is found in the API response.

       Returns:
           bool: True if the password's hash is not found in the API response.
       """
        response = self.connect_with_api()
        if self.convert_password_into_sha()[5:].upper() in response:
            raise ValidationException('You have to change your password!')

        return True
