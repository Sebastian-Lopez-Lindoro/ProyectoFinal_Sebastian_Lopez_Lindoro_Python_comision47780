from django import forms
from django.contrib.auth.forms import UserCreationForm


class FormularioRedactor(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    edad = forms.IntegerField()


class FormularioComentador(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    edad = forms.IntegerField()


class FormularioModerador(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)


class Buscar(forms.Form):
    nombre = forms.CharField()
