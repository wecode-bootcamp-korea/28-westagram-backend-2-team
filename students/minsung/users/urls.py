from django.urls import path 

from users.views import UserView, LoginView

app_name = 'users'

urlpatterns = [
    path('/signin', UserView.as_view()),
    path('/login', LoginView.as_view()),
]
