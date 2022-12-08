from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from room.views import add_room

urlpatterns = [
    path('', views.login_redirect, name="login-user"),
    path('register/', views.register, name='register'),
    path("auth/login/", LoginView.as_view(template_name="registration/login.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('addroom/', add_room, name='addroom')
]
