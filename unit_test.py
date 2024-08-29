'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration by test cases
'''

import unittest 
from User_Registration import check_name_format

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
         self.assertTrue(check_name_format('Rahugl'),"Should be valid")
         self.assertFalse(check_name_format('ra'),"Should not be valid due invalid length and 1st character lower case")
         self.assertFalse(check_name_format('rahul'),"Should not be valid due to 1st character lower case")
         self.assertFalse(check_name_format('RAHUL'),"Should not be valid due to all characters are upper case")
         self.assertFalse(check_name_format('r'),"Should not be valid due to invalid size and invalid 1st character")
         self.assertFalse(check_name_format('rAH'),"Should not be valid dur to invalid all characters")
    
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
         self.assertFalse(check_name_format('rahul'),"Should not be valid due to 1st character lower case")
         self.assertFalse(check_name_format('RAHUL'),"Should not be valid due to all characters arer upper case")
         self.assertFalse(check_name_format('r'),"Should not be valid due to invalid size") 

def main():
    obj=ValidatingUserCredentials
    obj.test_First_name()
    
if __name__=="__main__":
    unittest.main()