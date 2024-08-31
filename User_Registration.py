'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration
'''

import re 
from MyLogging import logger_init


def check_name_format(name):
    '''
    Description: 
        The function checks if the given name follows the specified format, 
        where the first character must be an uppercase letter followed by at 
        least two lowercase letters.
    Parameters:
        name (str): The name to be checked.
    Return:
        re.Match object or None: Returns a match object if the name follows 
        the format, or None if it doesn't.
    '''
    pattern = "^[A-Z][a-z]{2,}"
    return re.match(pattern, name)

def get_valid_name(prompt):
    
    '''
    Description: 
        Prompts the user to input a name and validates it using the check_name_format 
        function. The user gets up to 3 attempts to input a valid name.
    Parameters:
        prompt (str): The input prompt message for the user.
    Return:
        str or None: Returns the valid name if successful, otherwise None if validation fails after 3 attempts.
    '''
    
    attempts = 1
    
    while attempts <= 3:
        name = input(prompt)
        if check_name_format(name):
            return name
        
        else:
            print(f'{attempts} out of 3 attempts used.')
            attempts += 1

    return None

def main():
    first_name = get_valid_name("Enter your First name (Eg- 'Rah'): ")
    
    if first_name:
        last_name = get_valid_name("Enter your Last name (Eg- 'Jag'): ")
        
        if last_name:
            logger_init("UC_2").info("User Registered successfully")
        else:
            logger_init("UC_2").warning("User Registration Expired")
    else:
        logger_init('UC_2').warning("First name invalid, Registration failed")

if __name__ == "__main__":
    main()
