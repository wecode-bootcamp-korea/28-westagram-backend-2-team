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
        
        def valid_email(email=data['email']):
            email_regex = r'^[\w+-.]+@[\w]+\.[a-zA-Z0-9.-]+$'
            valid       = re.search(email_regex, email)
            if valid:
                return True
            else:
                return False
        
        def valid_password(password=data['password']):
            password_regex = r'([\w!@#$%^&*(),.?\":{}|<>]+){8}'
            valid          = re.search(password_regex, password)
            if valid:
                return True
            else:
                return False
        
        try:
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'USER_EXISTS'}, status=409)
            else:
                if valid_email() == True and valid_password() == True:
                    pass
                elif valid_email() == False:
                    return JsonResponse({'message': 'INVALID_EMAIL'}, status=409)
                elif valid_password() == False:
                    return JsonResponse({'message': 'INVALID_PASSWORD'}, status=409)
                
                user = User.objects.create(
                    email         = data['email'],
                    mobile        = data['mobile'],
                    user_name     = data['user_name'],
                    user_id       = data['user_id'],
                    password      = data['password'],
                )
                return JsonResponse({'message': "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
