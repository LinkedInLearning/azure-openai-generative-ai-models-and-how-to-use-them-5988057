#function to validate an email address
import re

def validate_email(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
    return False

#function to validate a phone number
def validate_phone(phone):
    if len(phone) > 7:
        if re.match("^[0-9-]*$", phone) != None:
            return True
    return False
