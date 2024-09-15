'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration by test cases
'''

import pytest, User_Registration as ur

    
def test_First_name():
    
        '''
    Description: 
        The function tests the `check_name_format()` function by checking 
        various name inputs for valid and invalid formats. It asserts that 
        names starting with a capital letter followed by at least two lowercase 
        letters return True, while invalid formats return False.
    Parameters:
         (unittest.TestCase): The instance of the test case class 
        containing the test methods.
    Return:
        None
    '''
    
        assert  ur.check_name_format('Rahul'),"Should be valid"
        assert  ur.check_name_format('Rah'),"Should be valid"
        assert not ur.check_name_format('ra'),"Should not be valid due invalid length and 1st character lower case"
        assert not ur.check_name_format('rahul'),"Should not be valid due to 1st character lower case"

def test_last_name():
    
    '''
    Description: 
        The function tests the `check_name_format()` function by checking 
        various name inputs for valid and invalid formats. It asserts that 
        names starting with a capital letter followed by at least two lowercase 
        letters return True, while invalid formats return False.
        
    Parameters:
         (unittest.TestCase): The instance of the test case class 
        containing the test methods.
        
    Return:
        None
    '''
    
    assert  ur.check_name_format('Jag'),"Should be valid"
    assert  ur.check_name_format('Jaganathan'),"Should be valid"
    assert not ur.check_name_format('ja'),"Should not be valid due to invalid size and 1st character"
    assert not ur.check_name_format('jaH'),"Should not be valid due to 1st character lower case"

def test_email():
    
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
    
    assert  ur.check_email_format("abc@gmail.com"),"should be valid"
    assert  ur.check_email_format("abc.xyz@co.in"),"should be valid"
    assert not ur.check_email_format("abc.@com"),"should not be valid"
    assert not ur.check_email_format("abc.com.co"),"should not be valid"
    
def test_phone_number():
    
    '''
    Description: 
        The function tests the `check_phone_number_format()` function by checking 
        various phone number inputs for valid and invalid formats. return True, while 
        sinvalid formats return False.
        
    Parameters:
        None
        
    Return:
        None
    '''
    
    assert  ur.check_phone_number_format("91 1234567890"),"should be valid"
    assert  ur.check_phone_number_format("65 1234567890"),"should be valid"
    assert not ur.check_phone_number_format("1234567890"),"should not be valid because not having country code"
    assert not ur.check_phone_number_format("91 567890"),"should not be valid because invalid length"

def test_password_number():
    
    '''
    Description: 
        The function tests the `check_password_format()` function by checking 
        various password inputs for valid and invalid formats. return True, while 
        sinvalid formats return False.
        
    Parameters:
        None
        
    Return:
        None
    '''
    
    assert  ur.check_password_format("Abc4@657bge"),"should be valid"
    assert  ur.check_password_format("R@hul637"),"should be valid"
    assert  ur.check_password_format("12345@Rah"),"should be valid"
    assert not ur.check_password_format("R@h*l15"),"should not be valid because not having 8 characters and has multiple special character"
    assert not ur.check_password_format("@#$Rahul637"),"should not be valid because it has multiple special character"
    assert not ur.check_password_format("R@#ul6347"),"should not be valid because it has multiple special character" 
        
    
if __name__=="__main__":
    pytest.main()