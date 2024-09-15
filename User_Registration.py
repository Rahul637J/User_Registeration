'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration

'''

import re
from MyLogging import logger_init


logger = logger_init("UC_3")

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
    return (re.fullmatch(pattern, name))

def check_email_format(email):
    
    '''
    Description: 
        Checks if the email follows a valid email format.
    Parameters:
        email (str): The email to validate.
    Return:
        bool: True if the email is valid, False otherwise.
    '''
    
    pattern=r"^[a-z0-9A-Z]+(?:[._%+-][a-zA-Z0-9]+)*@[a-z0-9-A-Z]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$"
    return bool(re.fullmatch(pattern, email))

def main():
    
    first_name = validate_input(
        "Enter your First name (Eg- 'Rahul'): ", 
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
        "Enter your valid email (Eg - 'rahul637@gmail.com'): ", 
        check_email_format, 
        "Invalid email."
    )
    
    if not email:
        logger.warning("Registration expired, Register again!!!")
        return

    logger.info(f'Hi! {first_name} {last_name} you are registered successfully!!!')

if __name__ == "__main__":
    main()