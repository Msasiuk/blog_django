from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def inicio(request):
    """Muestra la página de inicio con los últimos 3 posts publicados."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    context = {
        "posts": ultimos_posts
    }
    return render(request, "posts/inicio.html", context)

def acerca(request):
    """Muestra la página 'Acerca de'."""
    return render(request, "posts/acerca.html")

# ---------- CRUD de posts ----------
def lista_posts(request):
    """READ: muestra todos los posts publicados, del más nuevo al más viejo."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)

def detalle_post(request, pk):
    """READ: muestra un post completo."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


@login_required
def crear_post(request):
    """CREATE: muestra el formulario vacío (GET) o guarda el post nuevo (POST)."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("posts:detalle_post", pk=post.pk)
    else:
        form = PostForm(initial={"autor": request.user.username})

    context = {
        "form": form,
        "titulo_pagina": "Nuevo post",
        "texto_boton": "Publicar",
    }
    return render(request, "posts/post_form.html", context)

@login_required
def editar_post(request, pk):
    """UPDATE: muestra el formulario con los datos del post (GET) o guarda los cambios (POST)."""
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post,
        "titulo_pagina": "Editar post",
        "texto_boton": "Guardar cambios",
    }
    return render(request, "posts/post_form.html", context)

@login_required
def eliminar_post(request, pk):
    """DELETE: pide confirmación (GET) y borra el post (POST)."""
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("posts:lista_posts")

    return render(request, "posts/post_confirm_delete.html", {"post": post})