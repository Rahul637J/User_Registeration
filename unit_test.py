'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration by test cases
'''

import unittest 
from User_Registration import check_name_format,check_email_format

class ValidatingUserCredentials(unittest.TestCase):
    
    def test_First_name(self):
        
         '''
        Description: 
            The function tests the `check_name_format()` function by checking 
            various name inputs for valid and invalid formats. It asserts that 
            names starting with a capital letter followed by at least two lowercase 
            letters return True, while invalid formats return False.
        Parameters:
            self (unittest.TestCase): The instance of the test case class 
            containing the test methods.
        Return:
            None
        '''
        
         self.assertTrue(check_name_format('Rahul'),"Should be valid")
         self.assertTrue(check_name_format('Rah'),"Should be valid")
         self.assertFalse(check_name_format('ra'),"Should not be valid due invalid length and 1st character lower case")
         self.assertFalse(check_name_format('rahul'),"Should not be valid due to 1st character lower case")
    
    def test_last_name(self):
        
        '''
        Description: 
            The function tests the `check_name_format()` function by checking 
            various name inputs for valid and invalid formats. It asserts that 
            names starting with a capital letter followed by at least two lowercase 
            letters return True, while invalid formats return False.
            
        Parameters:
            self (unittest.TestCase): The instance of the test case class 
            containing the test methods.
            
        Return:
            None
        '''
        
        self.assertTrue(check_name_format('Jag'),"Should be valid")
        self.assertTrue(check_name_format('Jaganathan'),"Should be valid")
        self.assertFalse(check_name_format('ja'),"Should not be valid due to invalid size and 1st character")
        self.assertFalse(check_name_format('jaH'),"Should not be valid due to 1st character lower case")

    def test_email(self):
        
        '''
        Description: 
            The function tests the `check_email_format()` function by checking 
            various email inputs for valid and invalid formats. It asserts that 
            email starting with a lower cases letters optionally followed with '.' 
            and upper case letters with '@' followed by 2 optional (xyz & in) with
            precise @ and . positions return True, while invalid formats return False.
            
        Parameters:
            None
            
        Return:
            None
        '''
        
        self.assertTrue(check_email_format("abc@gmail.com"),"should be valid")
        self.assertTrue(check_email_format("abc.xyz@co.in"),"should be valid")
        self.assertFalse(check_email_format("abc.@com"),"should not be valid")
        self.assertFalse(check_email_format("abc.com.co"),"should not be valid")
        
def main():
    obj=ValidatingUserCredentials
    obj.test_First_name()
    
if __name__=="__main__":
    unittest.main()