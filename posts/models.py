from django.db import models

class Post(models.Model):
    """Representa una publicación del blog."""

    # Opciones para el campo estado: (valor que se guarda en la base, texto que se muestra)
    ESTADOS = [
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
        ("archivado", "Archivado"),
    ]

    titulo = models.CharField("Título", max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="borrador")
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.titulo
