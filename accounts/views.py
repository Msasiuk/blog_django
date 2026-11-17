from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroForm, UsuarioForm, PerfilForm
from .models import Perfil


def registro(request):
    """Crea un usuario nuevo, le crea su perfil y lo deja con la sesión iniciada."""
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(user=usuario)
            login(request, usuario)
            return redirect("accounts:perfil")
    else:
        form = RegistroForm()

    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    """Muestra el perfil del usuario que inició sesión."""
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil})


@login_required
def editar_perfil(request):
    """Edita los datos del usuario y de su perfil (incluido el avatar)."""
    perfil, creado = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            return redirect("accounts:perfil")
    else:
        usuario_form = UsuarioForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    context = {
        "usuario_form": usuario_form,
        "perfil_form": perfil_form,
    }
    return render(request, "accounts/editar_perfil.html", context)