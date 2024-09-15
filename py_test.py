'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration by test cases
'''

import pytest
import User_Registration as ur

    
def test_First_name():
    
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
    
        assert ur.check_name_format('Rahul'),"Should be valid"
        assert ur.check_name_format('Rah'),"Should be valid"
        assert ur.check_name_format('Rahugl'),"Should be valid"
        assert not ur.check_name_format('ra'),"Should not be valid due invalid length and 1st character lower case"
        assert not ur.check_name_format('rahul'),"Should not be valid due to 1st character lower case"
        assert not ur.check_name_format('RAHUL'),"Should not be valid due to all characters are upper case"

def test_last_name():
    
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
    
        assert ur.check_name_format('Jag'),"Should be valid"
        assert ur.check_name_format('Jaganathan'),"Should be valid"
        assert not ur.check_name_format('ja'),"Should not be valid due to invalid size and 1st character"
        assert not ur.check_name_format('jaH'),"Should not be valid due to 1st character lower case"


def main():
    pytest.main()
    
if __name__=="__main__":
    main()