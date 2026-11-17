from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    """Información extra de cada usuario: biografía, sitio web y avatar."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    biografia = models.TextField("Biografía", blank=True)
    link_web = models.URLField("Sitio web", blank=True)
    avatar = models.ImageField(upload_to="avatares/", null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"