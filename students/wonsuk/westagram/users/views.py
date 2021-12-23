import json
import bcrypt
import jwt

from json.decoder import JSONDecodeError

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View

from users.models           import User
from users.validators       import email_regex_match, password_regex_match
from my_settings            import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            email_regex_match(data['email'])
            password_regex_match(data['password'])
            
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode()
            
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'EMAIL_ALREADY_EXISTS'}, status=400)

            User.objects.create(
                username     = data['username'],
                email        = data['email'],
                password     = hashed_password,
                phone_number = data['phone_number'],
                age          = data['age']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status=400)
        
class LogInView(View):
    def post(self, request):
        try:
            user_info = json.loads(request.body)
            
            email    = user_info['email']
            password = user_info['password']
            
            if not User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401)
            
            user = User.objects.get(email=email)    
                        
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
                return JsonResponse({'access_token' : token}, status=200)
            
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)