from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from Users.forms import UserRegisterForm, UserEditForm
from Users.models import Avatar
from django.contrib.auth import update_session_auth_hash


# Create your views here.


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")

            clave = form.cleaned_data.get("password")

            nombre_usuario = authenticate(request, username=usuario, password=clave)

            if usuario is not None:
                login(request, nombre_usuario)

                return render(
                    request,
                    "Blog/index.html",
                    {"name": usuario, "mensaje": f" Has iniciado sesión"},
                )

        else:
            return render(
                request,
                "Blog/index.html",
                {"mensaje": "Error, datos incorrectos"},
            )

    form = AuthenticationForm()

    return render(request, "Users/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            update_session_auth_hash(request, request.user)
            return render(
                request,
                "Blog/index.html",
                {"mensaje": f"El nuevo usuario '{username}' ha sido creado"},
            )
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def edit(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            if data["password1"] != data["password2"]:
                data = {
                    "username": user.username,
                    "email": user.email,
                    "password1": user.password,
                }
                form = UserEditForm(initial=data)

            else:
                user.email = data["email"]
                user.username = data["username"]
                user.set_password(data["password1"])
                user.save()

                update_session_auth_hash(request, request.user)

                try:
                    avatar = Avatar.objects.get(user=user)

                except Avatar.DoesNotExist:
                    avatar = Avatar(user=user, imagen=data["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = data["imagen"]
                    avatar.save()
                    update_session_auth_hash(request, request.user)

                return render(request, "Blog/index.html")

    else:
        form = UserEditForm(initial={"username": user.username, "email": user.email})

    return render(request, "Users/edit.html", {"form": form, "usuario": user.username})


@login_required
def profile(request):
    user = request.user
    return render(request, "Users/profile.html", {"user": user})
