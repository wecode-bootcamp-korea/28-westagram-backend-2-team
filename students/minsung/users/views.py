import json
import re
import bcrypt
import jwt

from django.http   import JsonResponse
from django.views  import View
from django.conf   import settings

from users.models  import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        regex_email    = re.match('^[\w]+@[\w]+\.[\w]+$', data['email'])
        regex_password = re.match('^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$', data['password'])
        
        try:            
            if not regex_email: 
                return JsonResponse({"message": "INVALID EMAIL"}, status=400)

            if not regex_password:
                return JsonResponse({"message": "INVALID PASSWORD"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "DUPLICATED EMAIL"}, status=409)

            if User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({"message": "DUPLICATED PHONE_NUMBER"}, status=409)
            
            User.objects.create(
                username      = data['username'],
                email         = data['email'],
                password      = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                phone_number  = data['phone_number'],
                date_of_birth = data.get('date_of_birth', None)
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data["password"].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            token = jwt.encode({'user_id': User.objects.get(email=data["email"]).id}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
            return JsonResponse({"token": token}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status=404)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)