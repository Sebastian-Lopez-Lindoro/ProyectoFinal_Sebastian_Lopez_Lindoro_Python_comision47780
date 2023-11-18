from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from Users.views import login_request, register, edit, profile

app_name = "Users"


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
        ),
        name="Login",
    ),
    path("register/", register, name="Register"),
    path("profile/", profile, name="Profile"),
    path(
        "logout/", LogoutView.as_view(template_name="users/logout.html"), name="Logout"
    ),
    path("edit/", edit, name="Edit"),
]
