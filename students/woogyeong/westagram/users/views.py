# python built-in module
import json
import bcrypt

# 외부 module
from django.http  import JsonResponse
from django.views import View

# 사용자 module (직접 작성한 module)
from users.models     import User
from users.validators import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            email     = data['email']
            password  = data['password']
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            if not validate_email(email):
                return JsonResponse({'message': 'Email format is not valid'}, status=400)
            
            if not validate_password(password):
                return JsonResponse({'message': 'Password format is not valid'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': 'USER_EXISTS'}, status=409)
            
            User.objects.create(
                email     = data['email'],
                password  = hashed_pw,
                mobile    = data['mobile'],
                user_name = data['user_name'],
                user_id   = data['user_id'],
            )
            return JsonResponse({'message': "CREATED"}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        
class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']
            
            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401)
            
            user = User.objects.get(email=email)
            result = {
                'id'      : user.id,
                'user_id' : user.user_id,
                'name'    : user.user_name,
            }
            return JsonResponse({'result': result}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
