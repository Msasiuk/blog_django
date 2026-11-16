from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Formulario para crear y editar posts, generado a partir del modelo Post."""

    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 8}),
        }