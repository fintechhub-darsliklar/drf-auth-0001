from api.users.views.login_view import LoginView
from django.urls import path


urlpatterns = [
    path('auth/login/', LoginView.as_view()),
]
