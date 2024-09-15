'''
@Author: Rahul 
@Date: 2024-08-29
@Last Modified by: Rahul 
@Last Modified time: 2024-08-29
@Title: Employee wages - Python program to validate user input for registration by test cases

'''


import pytest
from User_Registration import check_name_format


def test_First_name():
    
    '''
    Description: 
        The function tests the `check_name_format()` function by checking 
        various name inputs for valid and invalid formats. It asserts that 
        names starting with a capital letter followed by at least two lowercase 
        letters return True, while invalid formats return False.
    Parameters:
        None
    Return:
        None
    '''
    
    assert check_name_format('Rahul')
    assert check_name_format('Rah')
    assert check_name_format('Rahugl')
    assert not check_name_format('ra')
    assert not check_name_format('rahul')
    assert not check_name_format('RAHUL')

def main():
    pytest.main()
    
if __name__=="__main__":
    main()