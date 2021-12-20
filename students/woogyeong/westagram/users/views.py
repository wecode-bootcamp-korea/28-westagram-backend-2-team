# python built-in module
import json

# 외부 module
from django.http  import JsonResponse
from django.views import View

# 사용자 module (직접 작성한 module)
from users.models import User
from users.validators import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not validate_email(data['email']):
                return JsonResponse({'message': 'Email format is not valid'}, status=400)
            elif not validate_password(data['password']):
                return JsonResponse({'message': 'Password format is not valid'}, status=400)
            elif User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'USER_EXISTS'}, status=400)
            elif validate_email(data['email']) and validate_password(data['password']):
                User.objects.create(
                    email         = data['email'],
                    mobile        = data['mobile'],
                    user_name     = data['user_name'],
                    user_id       = data['user_id'],
                    password      = data['password'],
                )
                return JsonResponse({'message': "CREATED"}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)