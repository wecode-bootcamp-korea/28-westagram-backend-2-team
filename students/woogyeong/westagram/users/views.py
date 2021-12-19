# python built-in module
import json
import re

# 외부 module
from django.http  import JsonResponse
from django.views import View

# 사용자 module (직접 작성한 module)
from users.models import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        def validate_email(email=data['email']):
            email_regex      = re.compile(r"^[a-zA-Z]+[!#$%&'*+-/=?^_`(){|}~]*[a-zA-Z0-9]*@[\w]+\.[a-zA-Z0-9-]+[.]*[a-zA-Z0-9]+$")
            email_validation = email_regex.match(email)
            
            if email_validation:
                return True
            else:
                return False
        
        def validate_password(password=data['password']):
            password_regex = re.compile(r'([\w!@#$%^&*(),.?\":{}|<>]+){8}')
            password_valid = password_regex.match(password)
            
            if password_valid:
                return True
            else:
                return False
        
        try:
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'USER_EXISTS'}, status=409)
            else:
                if validate_email() == True and validate_password() == True:
                    pass
                elif validate_email() == False:
                    return JsonResponse({'message': 'INVALID_EMAIL'}, status=409)
                elif validate_password() == False:
                    return JsonResponse({'message': 'INVALID_PASSWORD'}, status=409)
                
                user = User.objects.create(
                    email         = data['email'],
                    mobile        = data['mobile'],
                    user_name     = data['user_name'],
                    user_id       = data['user_id'],
                    password      = data['password'],
                )
                return JsonResponse({'message': "CREATED"}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
