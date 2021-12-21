import json
import re

from django.http   import JsonResponse
from django.views  import View

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
                password      = data['password'],
                phone_number  = data['phone_number'],
                date_of_birth = data['date_of_birth']
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not User.objects.filter(username=data['username']).exists() or not User.objects.filter(password=data['password']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            elif User.objects.get(username=data['username']) == User.objects.get(password=data['password']):
                return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)