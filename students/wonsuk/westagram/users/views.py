import json

from django.http     import JsonResponse
from django.views    import View

from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            
            
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
        