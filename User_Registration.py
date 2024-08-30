'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration
'''

from MyLogging import logger_init
import re 


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
    name=prompt
    while attempts <= 3:
        if check_name_format(name):
            return name
        else:
            print(f'{attempts} out of 3 attempts used.')
            attempts += 1
            name = input("Enter the valid name: ")

    return None

def main():
    
    first_name=input("Enter your first name (1st character should capital): ")
    valid_name=get_valid_name(first_name)
    
    if valid_name:
        logger_init(valid_name).info("User registration  successfull")
    
    else:
        logger_init(valid_name).warning("User registration expired, Register again")    
           
        
if __name__=="__main__":
    main()