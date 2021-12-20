import json
import re

from django.http   import JsonResponse
from django.views  import View

from users.models  import User

email_validator    = re.compile('^[\w]+@[\w]+\.[\w]+$')

password_validator = re.compile('^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$')

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if email_validator.match(data['email']) == None:
                return JsonResponse({"message": "INVALID EMAIL"}, status=400)

            if password_validator.match(data['password']) == None:
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