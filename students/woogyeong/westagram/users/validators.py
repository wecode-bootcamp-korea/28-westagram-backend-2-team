import re


def validate_email(email):
    email_regex = r"^[a-zA-Z]+[\w!#$%&'*+-/=?^_`(){|}~]+@[\w]+\.[a-zA-Z0-9-]+[.]*[a-zA-Z0-9]+$"
    return re.match(email_regex, email)
    
            
def validate_password(password):
    password_regex = r'([\w!@#$%^&*(),.?\":{}|<>]+){8}'
    return re.match(password_regex, password)