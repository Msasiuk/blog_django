from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class RegistroForm(UserCreationForm):
    """Formulario de registro: usuario y contraseña (de UserCreationForm) más email, nombre y apellido."""

    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=150, required=False)
    last_name = forms.CharField(label="Apellido", max_length=150, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class UsuarioForm(forms.ModelForm):
    """Datos del usuario que se pueden editar desde el perfil."""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class PerfilForm(forms.ModelForm):
    """Datos del perfil: biografía, sitio web y avatar."""

    class Meta:
        model = Perfil
        fields = ["biografia", "link_web", "avatar"]
        widgets = {
            "biografia": forms.Textarea(attrs={"rows": 5}),
        }