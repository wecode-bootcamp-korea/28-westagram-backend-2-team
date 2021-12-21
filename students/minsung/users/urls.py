from django.urls import path 

from users.views import UserView, LoginView

app_name = 'users'

urlpatterns = [
    path('/sign_in', UserView.as_view()),
    path('/log_in', LoginView.as_view()),
]
