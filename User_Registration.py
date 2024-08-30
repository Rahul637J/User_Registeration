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

def check_phone_number_format(phone_number):
    
    '''
    Description: 
        The function checks if the given phone number follows the specified format, 
        where the format start's with contry code followed by space and 10 digits.
    Parameters:
        name (str): The name to be checked.
    Return:
        re.Match object or None: Returns a match object if the name follows 
        the format, or None if it doesn't.
    '''
    
    pattern="^[0-9]{2} [0-9]{10}$"
    return re.fullmatch(pattern,phone_number)

def check_password_format(password):
    
    '''
    Description: 
        The function checks if the given password follows the specified format, 
        where the format is atleast 8 characters and atleast 1 upper case.
    Parameters:
        name (str): The name to be checked.
    Return:
        re.Match object or None: Returns a match object if the name follows 
        the format, or None if it doesn't.
    '''
    
    pattern="^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}$"
    return re.fullmatch(pattern,password)

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
        Prompts the user to input a email and validates it using the check_eamil_format 
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

def get_valid_phone_number(msg):
    
    '''
    Description: 
        Prompts the user to input a phone number and validates it using the check_phone_number_format 
        function. The user gets up to 3 attempts to input a valid name.
    Parameters:
        prompt (str): The input prompt message for the user.
    Return:
        none
    '''
    
    attempts=1
    
    while attempts<=3:
        phone_number=input(msg)
        
        if check_phone_number_format(phone_number):
            return phone_number
        
        else:
            print(f'{attempts} out of 3 attempts used.')
            attempts+=1

def get_valid_password(msg):
    
    '''
    Description: 
        Prompts the user to input a name and validates it using the check_name_format 
        function. The user gets up to 3 attempts to input a valid name.
    Parameters:
        prompt (str): The input prompt message for the user.
    Return:
        none
    '''
    
    attempts=1
    
    while attempts<=3:
        password=input(msg)
        
        if check_password_format(password):
            return password
        
        else:
            print(f'{attempts} out of 3 attempts used.')
            attempts+=1
                
                
def main():
    first_name = get_valid_name("Enter your First name (First letter Capital): ")
    
    if first_name:
        last_name = get_valid_name("Enter your Last name (First letter Capital): ")
    
        if last_name:
            email=get_valid_email("Enter the email: ")
            
            if email:
                phone_number=get_valid_phone_number("Enter your phone number: ")

                if phone_number:
                    password=get_valid_password("Enter the password (minimum 8 characters): ")
                    
                    if password:
                        logger_init(password).info("User registered successfull!!")
                    
                    else:
                        logger_init(password).warning("Session expired, Register again!!!")    
                
                else:
                    logger_init(phone_number).warning("Session Expired, Register again!!!") 
            
            else:
                logger_init(email).warning("Session expired, Register again!!!")    
        
        else:
            logger_init(last_name).warning("Session expired, Register again!!!")
                 
    else:
        logger_init(first_name).warning("Session expired, Registration failed")
    
if __name__ == "__main__":
    main()
