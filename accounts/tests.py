from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from posts.models import Post
from .models import Perfil


class RegistroTests(TestCase):

    def test_registro_crea_usuario_y_perfil(self):
        """Al registrarse se crea el usuario, su perfil y queda con la sesión iniciada."""
        respuesta = self.client.post(reverse("accounts:registro"), {
            "username": "lector",
            "email": "lector@ejemplo.com",
            "password1": "ClaveSegura123!",
            "password2": "ClaveSegura123!",
        })
        self.assertRedirects(respuesta, reverse("accounts:perfil"))
        usuario = User.objects.get(username="lector")
        self.assertTrue(Perfil.objects.filter(user=usuario).exists())


class ProteccionTests(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(username="autora", password="ClaveSegura123!")
        self.post = Post.objects.create(
            titulo="Post de prueba", contenido="Contenido", autor="autora", estado="publicado"
        )

    def test_anonimo_no_puede_crear_editar_ni_borrar(self):
        """Sin sesión iniciada, crear/editar/borrar redirigen al login."""
        urls = [
            reverse("posts:crear_post"),
            reverse("posts:editar_post", args=[self.post.pk]),
            reverse("posts:eliminar_post", args=[self.post.pk]),
        ]
        for url in urls:
            respuesta = self.client.get(url)
            self.assertRedirects(respuesta, f"{reverse('accounts:login')}?next={url}")

    def test_listado_y_detalle_son_publicos(self):
        """El listado y el detalle se ven sin iniciar sesión."""
        self.assertEqual(self.client.get(reverse("posts:lista_posts")).status_code, 200)
        self.assertEqual(self.client.get(reverse("posts:detalle_post", args=[self.post.pk])).status_code, 200)

    def test_usuario_logueado_puede_crear(self):
        """Con sesión iniciada, se puede entrar al formulario de crear post."""
        self.client.login(username="autora", password="ClaveSegura123!")
        self.assertEqual(self.client.get(reverse("posts:crear_post")).status_code, 200)

    def test_perfil_requiere_login(self):
        """El perfil redirige al login si no hay sesión."""
        url = reverse("accounts:perfil")
        respuesta = self.client.get(url)
        self.assertRedirects(respuesta, f"{reverse('accounts:login')}?next={url}")