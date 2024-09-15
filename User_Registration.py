'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration
'''

from MyLogging import logger_init
import re 


log = logger_init("UC_1")

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
         The function checks if the given name follows the specified format, 
         where the first character must be an uppercase letter followed by at 
         least two lowercase letters.
         
     Parameters:
         name (str): The name to be checked.
         
     Return:
         re.Match object or None: Returns a match object if the name follows 
         the format, or None if it doesn't.
     '''
    
     pattern="^[A-Z][a-z]{2,}"
     return re.match(pattern,name)
  

def main():
    
    first_name = validate_input(
        "Enter your First name (Eg - 'Rahul'): ",
        check_name_format,
        "Invalid first name."
    )
    
    if not first_name:
        log.info("First name invalid, Registration failed")
        return
    
    log.info("Registered successfull!!!")  
           
if __name__=="__main__":
    main()