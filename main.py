from api import Api
from password import ValidationException


def validate_password(password):
    """
    Validates the given password based on certain requirements.

    Args:
        password (Api): An instance of the Api class representing the password.

    Returns:
        tuple: A tuple containing two elements.
    """
    requirements = [
        ('correct_length', password.correct_length()),
        ('at_least_one_number', False),
        ('at_least_one_special_character', False),
        ('upper_and_lower_characters', False)
    ]

    validation_errors = []

    for method, _ in requirements:
        if hasattr(password, method):
            try:
                requirements[requirements.index((method, _))] = (method, getattr(password, method)())
            except ValidationException as e:
                validation_errors.append((method, str(e)))

    return all([result for _, result in requirements]), validation_errors


def main():
    """
    Reads passwords from 'passwords.txt', validates each password, and writes
    valid passwords to 'safe_password.txt' while displaying validation errors
    for invalid passwords.
    """
    with open('passwords.txt', mode='r', encoding='utf-8') as input_file, \
            open('safe_password.txt', mode='w', encoding='utf-8') as output_file:
        for line in input_file:
            password = Api(line.strip())
            valid, errors = validate_password(password)

            if valid and password.check_if_password_not_in_api():
                output_file.write(str(password) + '\n')
            else:
                print(f'Hasło {str(password)} nie spełnia poniższych wymogów:')
                for method, error in errors:
                    print(f' - {method}: {error}')


if __name__ == '__main__':
    main()