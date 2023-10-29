# Is_my_password_secure?

is_my_password_secure? is used to check whether a given password meets the requirements of a secure password. The password needs to be saved in the passwords.txt file, and the program will check them all, saving only the secure ones to the safe_password.txt file and displaying information about what's wrong with the remaining passwords

## Installation
1. Make sure you have Python 3.x installed on your system. 
2. Clone this repository to your local machine.
3. Install the required dependencies by running:
- pip install -r requirements.txt

## Usage
1. Run the main.py script to interact with program:
   - on macOS python3 main.py -p
   - on Windows python main.py -p
2. If all passwords are secure, the program will save them to the safe_password.txt file. If not, it will display information about which password or passwords do not meet the requirements, and the remaining passwords will be saved as secure passwords.

## Modules

### api.py
Module responsible for connecting to the API and checking if the provided password is in its database.
### main.py
The main module responsible for the program's operation.
### password.py
Module responsible for checking if the password meets the requirements of a secure password.
### setup.py
Module responsible for creating a package containing the api and password modules along with tests. To install the package, you need to execute the following commands:
- python setup.py sdist
This will create the dist directory, and from there you should copy the password-0.1.tar.gz file and paste it into another project. To use the modules from the package in another project, you need to enter the command:
  - pip install password-0.1.tar.gz

## Support
If you encounter any issues with my software, please reach out to me:
- Email: k.turek1995@gmail.com

## Dependencies
To run this software, you'll need the libraries and tools listed in requirements.txt

## License
This project is licensed under the MIT License - 
[![Licencja MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](https://opensource.org/licenses/MIT)