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
    return re.fullmatch(pattern, name)

def check_email_format(email):
    
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
    
    pattern=r"^[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)?@[A-Za-z0-9]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?$"
    return re.match(pattern,email)

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

def get_valid_email(msg):
    
    '''
    Description: 
        Prompts the user to input a name and validates it using the check_name_format 
        function. The user gets up to 3 attempts to input a valid name.
    Parameters:
        prompt (str): The input prompt message for the user.
    Return:
        str or None: Returns the valid name if successful, otherwise None if validation fails after 3 attempts.
    '''
    
    attempts=1
    
    while attempts<=3:
        email=input(msg)
        
        if check_email_format(email):
            return email
        
        else:
            print(f'{attempts} out of 3 attempts used.')
            attempts+=1
            
def main():
    first_name = get_valid_name("Enter your First name (First letter Capital): ")
    
    if first_name:
        last_name = get_valid_name("Enter your Last name (First letter Capital): ")
    
        if last_name:
            email=get_valid_email("Enter the valid email: ")
            
            if email:
                logger_init(email).info("User registered successfull!!")
            
            else:
                logger_init(email).warning("Registration expired, Register again!!!")    
        
        else:
            logger_init(last_name).warning("Registration expired, Register again!!!")
                 
    else:
        logger_init(first_name).warning("First name invalid, Registration failed")
    
if __name__ == "__main__":
    main()
