import re

def check_email(email):
    regex_email = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9.]+$'
    return re.match(regex_email, email)

def check_password(password):
    regex_password = '((?=.*[0-9])(?=.*[a-z|A-Z])(?=.*[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\\\|\;\:\'\"\,\<\.\>\/\?]).{8,})'
    return re.match(regex_password, password)