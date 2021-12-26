# python built-in module
import json
import bcrypt
import jwt

# 외부 module
from django.http  import JsonResponse
from django.views import View

# 사용자 module (직접 작성한 module)
from users.models       import User
from users.validators   import validate_email, validate_password
from westagram.settings import SECRET_KEY, algorithm

class SignUpView(View):
    def post(self, request):        
        try:
            data            = json.loads(request.body)
            email           = data['email']
            password        = data['password']
            
            if not validate_email(email):
                return JsonResponse({'MESSAGE': 'Email format is not valid'}, status=400)
            
            if not validate_password(password):
                return JsonResponse({'MESSAGE': 'Password format is not valid'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE': 'USER_EXISTS'}, status=409)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                email     = email,
                password  = hashed_password,
                mobile    = data['mobile'],
                user_name = data['user_name'],
                user_id   = data['user_id'],
            )
            return JsonResponse({'MESSAGE': "CREATED"}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSONDecodeError'}, status=404)
        
class LogInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            
            if User.objects.get(email=email) and bcrypt.checkpw(password.encode('utf-8'), User.objects.get(email=email).password.encode('utf-8')):
                user  = User.objects.get(email=email)
                token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm=algorithm)
                result = {
                    'id'      : user.id,
                    'user_id' : user.user_id,
                    'name'    : user.user_name,
                }
                return JsonResponse({'result': result, 'token': token}, status=200)
            
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSONDecodeError'}, status=404)
