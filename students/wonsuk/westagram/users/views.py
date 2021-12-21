import json

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View

from users.models           import User
from users.validators       import email_regex_match, password_regex_match

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            email_regex_match(data['email'])
            password_regex_match(data['password'])
            
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'EMAIL_ALREADY_EXISTS'}, status=400)

            User.objects.create(
                username     = data['username'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
                age          = data['age']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status=400)