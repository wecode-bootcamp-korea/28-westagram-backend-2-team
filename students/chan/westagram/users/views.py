import json
import bcrypt

from django import views

from django.http      import JsonResponse, request
from django.views     import View

from users.models     import User
from users.validators import check_email, check_password

class UsersView(View):
    def post(self, request):
        data = json.loads(request.body)

        password = data['password']

        try:
            if not check_email(data['email']):
                return JsonResponse({'Message' : 'INVALID_EMAIL'}, status=400)

            if not check_password(data['password']):
                return JsonResponse({'Message' : 'INVALID_PASSWORD'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'Message' : 'EMAIL_EXISTS'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password.decode('utf-8'),
                phone_number = data['phone_number'],
                address      = data['address'],
            )

            return JsonResponse({'Message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'Message' : 'KEY_ERROR'}, status=400)

class LogInView(View):
    def post(self, request):
        
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'Message' : 'INVALID_USER'}, status=401)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'Message' : 'INVALID_USER'}, status=401)

            return JsonResponse({'Message' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'Message' : 'KEY_ERROR'}, status=400)