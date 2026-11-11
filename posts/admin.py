from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Columnas que se ven en el listado de posts
    list_display = ("titulo", "autor", "estado", "fecha_creacion")
    # Filtros en la barra lateral derecha
    list_filter = ("estado", "fecha_creacion")
    # Cuadro de búsqueda (busca en estos campos)
    search_fields = ("titulo", "contenido", "autor")


admin.site.register(Post, PostAdmin)
