import re

from django.core.exceptions import ValidationError

def email_regex_match(email):
    EMAIL_REGEX = "^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError('INVALID_EMAIL')
    
def password_regex_match(password):
    PASSWORD_REGEX = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"
    
    if not re.match(PASSWORD_REGEX, password):
        raise ValidationError('INVALID_PASSWORD')