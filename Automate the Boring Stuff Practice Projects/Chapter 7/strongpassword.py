#This function checks if a given password is valid according to the criteria below

import re

def is_valid(password):
    upperlower = re.compile(r'((.*[A-Z].*)(.*[a-z].*)|(.*[a-z].*)(.*[A-Z].*))') # Must contain both uppercase and lowercase characters
    min_length = re.compile(r'.{8,}') #Must be at least eight characters long
    has_digit = re.compile(r'.*\d.*') #Must have at least one digit
    if upperlower.search(password) != None and min_length.search(password) != None and has_digit.search(password) != None:
        return True
    else:
        return False

user_pass = input('Please enter a password\n')
if is_valid(user_pass):
    print('Valid password')
else:
    print('Invalid password')