'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration
'''

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

def main():
    
    attempts=1
    
    while attempts<=3:
        first_name=input("Enter your name First name (First letter Capital): ")
        result=check_name_format(first_name)

        if result:
            print("Name is Valid") 
        else:
            print("Invalids Name")    
            print(f'{attempts} out of 3')
            attempts+=1
            
    if attempts>3:
        print("Registration Expired start new registration!!")        
        
if __name__=="__main__":
    main()