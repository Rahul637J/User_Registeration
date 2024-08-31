'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration
'''

import re
from MyLogging import logger_init

logger = logger_init("UC_4")

def validate_input(prompt, validation_function, error_message):
    
    '''
    Description: 
        Prompts the user for input and validates it using the provided validation function.
        Allows up to 3 attempts for the user to input valid data.
    Parameters:
        prompt (str): The message displayed to the user for input.
        validation_function (callable): A function that validates the input.
        error_message (str): The error message displayed if validation fails.
    Return:
        str or None: Returns the valid input if successful, otherwise None after 3 attempts.
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
        Checks if the name follows the format: 
        First letter uppercase followed by at least two lowercase letters.
    Parameters:
        name (str): The name to validate.
    Return:
        bool: True if the name is valid, False otherwise.
    '''
    
    pattern = "^[A-Z][a-z]{2,}"
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
    return bool(re.match(pattern, email))

def check_phone_number_format(phone_number):
    
    '''
    Description: 
        Checks if the phone number follows the format: 
        Two digits country code followed by 10 digit phone number (e.g., 91 1234567890).
    Parameters:
        phone_number (str): The phone number to validate.
    Return:
        bool: True if the phone number is valid, False otherwise.
    '''
    
    pattern = "^[0-9]{2} [0-9]{10}$"
    return bool(re.fullmatch(pattern, phone_number))

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
        "Enter your email (Eg - 'rahuj637j@gmail.com'): ", 
        check_email_format, 
        "Invalid email."
    )
    
    if not email:
        logger.warning("Registration expired, Register again!!!")
        return

    phone_number = validate_input(
        "Enter your phone number (e.g., 91 1234567890): ", 
        check_phone_number_format, 
        "Invalid phone number."
    )
    
    if not phone_number:
        logger.warning("Registration expired, Register again!!!")
        return

    logger.info(f'Hi! {first_name} {last_name} successfully registered!!!')

if __name__ == "__main__":
    main()
