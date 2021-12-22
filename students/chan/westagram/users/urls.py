from django.urls import path

from users.views import UsersView, LogInView

urlpatterns = [
    path('', UsersView.as_view()),
    path('/login', LogInView.as_view()),
]