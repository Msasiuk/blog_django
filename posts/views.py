from django.shortcuts import render
from .models import Post

def inicio(request):
    """Muestra la página de inicio con los últimos 3 posts publicados."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    context = {
        "posts": ultimos_posts
    }
    return render(request, "posts/inicio.html", context)

def acerca(request):
    """Muestra la página 'Acerca de'."""
    return render(request, 'posts/acerca.html')

def lista_posts(request):
    """Muestra todos los posts publicados, del más nuevo al más viejo."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)