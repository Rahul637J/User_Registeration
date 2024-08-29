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
        
         self.assertTrue(check_name_format('Rahul'))
         self.assertTrue(check_name_format('Rah'))
         self.assertTrue(check_name_format('Rahugl'))
         self.assertFalse(check_name_format('ra'))
         self.assertFalse(check_name_format('rahul'))
         self.assertFalse(check_name_format('RAHUL'))
         self.assertFalse(check_name_format('r'))
         self.assertFalse(check_name_format('rAH'))

def main():
    obj=ValidatingUserCredentials
    obj.test_First_name()
    
if __name__=="__main__":
    unittest.main()