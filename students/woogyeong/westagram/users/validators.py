import re

def validate_email(email):
    REGEX_EMAIL = r"^[a-zA-Z]+[\w!#$%&'*+-/=?^_`(){|}~]+@[\w]+\.[a-zA-Z0-9-]+[.]*[a-zA-Z0-9]+$"
    return re.match(REGEX_EMAIL, email)
              
def validate_password(password):
    REGEX_PASSWORD = r'([\w!@#$%^&*(),.?\":{}|<>]+){8}'
    return re.match(REGEX_PASSWORD, password)