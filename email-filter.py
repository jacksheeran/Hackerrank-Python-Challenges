# Checks if an email address is valid according to the rules:
#  -It must have the username@websitename.extension format type. 
#  -The username can only contain letters, digits, dashes and underscores.
#  -The website name can only have letters and digits.
#   -The maximum length of the extension is 3.
# Challenge created by harsh_beria93."""

import re

def fun(s):
    """returns True if s is a valid email, else return False"""
    return bool(re.match(r'^([\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3})$', s))
