'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee Registration - Python program to validate user input for registration
'''

import re, MyLogging

logger = MyLogging.logger_init("UC_7")

def validate_input(prompt, validation_function, error_message):
    
    '''
    Description: 
        Prompts the user for input and validates it using the provided validation function.
        The user gets up to 3 attempts to provide valid input.
    Parameters:
        prompt (str): The message displayed to the user for input.
        validation_function (callable): A function that validates the input.
        error_message (str): The error message displayed if validation fails.
    Return:
        str or None: Returns the valid input if successful, otherwise None if validation fails after 3 attempts.
    '''
    
    attempts = 1
    while attempts <= 3:
        user_input = input(prompt)
        if validation_function(user_input):
            return user_input
        else:
            print(f'{error_message} {attempts} out of 3 attempts used.')
            attempts += 1
    return None

def check_name_format(name):
    
    '''
    Description: 
        Checks if the name follows the format of starting with a capital letter followed by at least two lowercase letters.
    Parameters:
        name (str): The name to validate.
    Return:
        bool: True if the name is valid, False otherwise.
    '''
    
    pattern = "^[A-Z][a-z]{2,}$"
    return bool(re.fullmatch(pattern, name))

def check_email_format(email):
    
    '''
    Description: 
        Checks if the email follows a valid email format.
    Parameters:
        email (str): The email to validate.
    Return:
        bool: True if the email is valid, False otherwise.
    '''
    
    pattern = r"^[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)?@[A-Za-z0-9]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?$"
    return bool(re.fullmatch(pattern, email))

def check_phone_number_format(phone_number):
    
    '''
    Description: 
        Checks if the phone number follows the format: country code followed by space and a 10-digit number.
    Parameters:
        phone_number (str): The phone number to validate.
    Return:
        bool: True if the phone number is valid, False otherwise.
    '''
    
    pattern = "^[0-9]{2} [0-9]{10}$"
    return bool(re.fullmatch(pattern, phone_number))

def check_password_format(password):
    
    '''
    Description: 
        Checks if the password is at least 8 characters long.
    Parameters:
        password (str): The password to validate.
    Return:
        bool: True if the password is valid, False otherwise.
    '''
    
    pattern="^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$"
    return bool(re.fullmatch(pattern, password))

def main():
    
    first_name = validate_input(
        "Enter your First name (Eg - 'Rahul'): ",
        check_name_format,
        "Invalid first name."
    )
    
    if not first_name:
        logger.warning("First name invalid, Registration failed")
        return

    last_name = validate_input(
        "Enter your Last name (Eg - 'Jaganathan'): ",
        check_name_format,
        "Invalid last name."
    )
    
    if not last_name:
        logger.warning("Last name invalid, Registration failed")
        return

    email = validate_input(
        "Enter your email (Eg - 'rahul637j@gmail.com'): ",
        check_email_format,
        "Invalid email."
    )
    
    if not email:
        logger.warning("Invalid email, Registration failed")
        return

    phone_number = validate_input(
        "Enter your phone number (e.g., 91 1234567890): ",
        check_phone_number_format,
        "Invalid phone number."
    )
    
    if not phone_number:
        logger.warning("Invalid phone number, Registration failed")
        return

    password = validate_input(
        "Enter your password (minimum 8 characters): ",
        check_password_format,
        "Invalid password."
    )
    
    if not password:
        logger.warning("Invalid password, Registration failed")
        return

    logger.info(f'Hi {first_name} {last_name}, you have registered successfully!!!')

if __name__ == "__main__":
    main()