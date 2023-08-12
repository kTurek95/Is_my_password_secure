from api import Api

# wymogi bezpiecznego hasła:
# min 8 znaków
# min jedna cyfra
# min jeden znak specjalny
# wielkie i małe litery


def main():
    with open('passwords.txt', mode='r', encoding='utf-8') as input_file, \
            open('safe_password.txt', mode='w', encoding='utf-8') as output_file:
        for line in input_file:
            password = Api(line.strip())
            requirements = [
                ('correct_length', password.correct_length()),
                ('at_least_one_number', password.at_least_one_number()),
                ('at_least_one_special_character', password.at_least_one_special_character()),
                ('upper_and_lower_characters', password.upper_and_lower_characters()),
                ('check_if_password_not_in_api', password.check_if_password_not_in_api())
            ]
            if all([result for method, result in requirements])\
                    and password.check_if_password_not_in_api():
                output_file.write(str(password) + '\n')
            else:
                print(f'Hasło {str(password)} nie spełnia poniższych wymogów:')
                for method, result in requirements:
                    if not result:
                        print(f' - {method}')


if __name__ == '__main__':
    # main()
    api = Api('xxKacper95xx')
    print(api.connect_with_api())
    # print(api.convert_password_into_sha())