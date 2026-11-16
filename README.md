# blog_django

Blog web desarrollado con Django en el curso de Python de Coderhouse.

## Descripción

Este repositorio contiene el blog web. Es la continuación del blog por consola de las preentregas anteriores, ahora como aplicación web con Django.

En esta versión (Preentrega 10) se agregó la gestión de publicaciones desde el propio sitio (CRUD completo) e imagen opcional para cada post.

## Requisitos

- Python 3.12 o superior (Django 6.1 no funciona con versiones anteriores).
- Git, para clonar el repositorio.

## Instalación

1. Clonar el repositorio:

   ```
   git clone https://github.com/Msasiuk/blog_django.git
   ```

2. Entrar a la carpeta del proyecto:

   ```
   cd blog_django
   ```

3. Crear el entorno virtual:

   ```
   python -m venv venv
   ```

4. Activar el entorno virtual:

   - En Windows (CMD):

     ```
     venv\Scripts\activate
     ```

   - En Windows (PowerShell):

     ```
     .\venv\Scripts\Activate.ps1
     ```

   - En Linux o macOS:

     ```
     source venv/bin/activate
     ```

   Si se activó bien, el inicio de la línea de la terminal muestra `(venv)`.

5. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```
   Esto instala Django y **Pillow**, la librería que Django necesita para trabajar con imágenes (`ImageField`).

## Base de datos

Antes del primer uso hay que crear la base de datos:

```
python manage.py migrate
```

Esto genera el archivo `db.sqlite3` con todas las tablas. Ese archivo no se sube al repositorio: cada persona lo crea en su computadora.

Para cargar los posts de ejemplo (opcional, incluye un post con imagen):

```
python manage.py loaddata posts
```

## Cómo ejecutarlo

1. Con el entorno virtual activo, levantar el servidor de desarrollo:

   ```
   python manage.py runserver
   ```

2. Abrir en el navegador:

   | Página | URL |
   |---|---|   
   | Inicio | http://127.0.0.1:8000/ |
   | Posts | http://127.0.0.1:8000/posts/ |
   | Nuevo post | http://127.0.0.1:8000/posts/crear/ |
   | Detalle de un post | http://127.0.0.1:8000/posts/1/ |   
   | Acerca de | http://127.0.0.1:8000/acerca/ |
   | Panel admin | http://127.0.0.1:8000/admin/ |

   Desde el menú superior se puede navegar entre las páginas.

3. Para detener el servidor, presionar `Ctrl + C` en la terminal.

## Operaciones CRUD

Desde el sitio, sin entrar al admin, se puede:

| Operación | URL | Cómo |
|---|---|---|
| **Crear** | `/posts/crear/` | Menú → "Nuevo post". |
| **Listar** | `/posts/` | Menú → "Posts". Muestra solo los posts con estado "Publicado". |
| **Ver detalle** | `/posts/<id>/` | Clic en el título de un post. Muestra título, contenido, autor, estado e imagen. |
| **Editar** | `/posts/<id>/editar/` | Botón "Editar" en el detalle. Permite cambiar o quitar la imagen. |
| **Eliminar** | `/posts/<id>/eliminar/` | Botón "Eliminar" en el detalle. Pide confirmación antes de borrar. |

Después de crear o editar un post, el sitio redirige a su detalle. Así se puede ver y editar aunque se haya guardado como borrador.

Las vistas son funciones en `posts/views.py`. Las de crear y editar usan el formulario `PostForm` y procesan `request.POST` (textos) y `request.FILES` (imagen).

## Manejo de imágenes

Cada post puede tener una imagen opcional.

- **Modelo:** `imagen = models.ImageField(upload_to='posts/', null=True, blank=True)`.
- **Dependencia:** `ImageField` requiere **Pillow** (incluida en `requirements.txt`).
- **Configuración** en `blog_project/settings.py`:

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

  Las imágenes subidas se guardan en `media/posts/` y se acceden desde `/media/posts/<archivo>`.
- **Servir las imágenes en desarrollo:** en `blog_project/urls.py` se agrega `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` cuando `DEBUG` es `True`.
- **Formulario:** `PostForm` (un `ModelForm`, en `posts/forms.py`) incluye los campos `titulo`, `contenido`, `autor`, `estado` e `imagen`. El `<form>` de `post_form.html` usa `enctype="multipart/form-data"`, necesario para enviar archivos.
- **Templates:** la imagen se muestra solo si existe (`{% if post.imagen %}`). Si no hay imagen, el detalle muestra un mensaje.

### Cómo probar la carga de imágenes

1. Levantar el servidor y entrar a http://127.0.0.1:8000/posts/crear/.
2. Completar el formulario, elegir una imagen y el estado "Publicado", y tocar **Publicar**.
3. El sitio redirige al detalle del post, donde se ve la imagen.
4. La imagen queda guardada en la carpeta `media/posts/`.
5. Para cambiarla: **Editar** → elegir otra imagen → **Guardar cambios**. Para quitarla: tildar **Limpiar**.

## Panel de administración

1. Crear un usuario administrador:

   ```
   python manage.py createsuperuser
   ```

   Pide nombre de usuario, email (opcional) y contraseña. La contraseña no se ve mientras se escribe.

2. Levantar el servidor y entrar a http://127.0.0.1:8000/admin/ con ese usuario.

3. En **Posts** se pueden crear, editar y eliminar publicaciones, incluidos los borradores y los archivados.

## Estructura del proyecto

```
blog_django/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   └── posts/
│       └── herramientas-programacion-rrss.png
│
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── fixtures/
    │   └── posts.json
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   ├── 0002_alter_post_titulo.py
    │   └── 0003_post_imagen.py
    ├── models.py
    ├── tests.py
    ├── urls.py    
    ├── views.py
    │
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── acerca.html
    │       ├── lista_posts.html
    │       ├── detalle_post.html
    │       ├── post_form.html
    │       └── post_confirm_delete.html
    │
    └── static/
        └── posts/
            └── css/
                └── estilos.css
```

| Archivo o carpeta | Para qué sirve |
|---|---|
| `manage.py` | Herramienta de Django para ejecutar comandos del proyecto (`runserver`, `migrate`, `createsuperuser`). |
| `blog_project/settings.py` | Configuración: aplicaciones instaladas, idioma, zona horaria, base de datos y archivos media. |
| `blog_project/urls.py` | Rutas del proyecto: admin, rutas de la app `posts` y archivos media en desarrollo. |
| `media/posts/` | Imágenes subidas desde el sitio. |
| `posts/models.py` | Modelo `Post`: define la tabla de publicaciones, incluida la imagen. |
| `posts/forms.py` | `PostForm`: formulario basado en el modelo `Post` (`ModelForm`). |
| `posts/views.py` | Vistas del sitio: inicio, acerca de y el CRUD de posts (listar, detalle, crear, editar, eliminar). |
| `posts/urls.py` | Rutas de la app: inicio, acerca de y las 5 rutas del CRUD de posts. |
| `posts/admin.py` | Registro del modelo en el panel admin (`PostAdmin`). |
| `posts/migrations/` | Migraciones que crean y actualizan la tabla de posts. |
| `posts/fixtures/posts.json` | Posts de ejemplo para cargar con `loaddata`. |
| `posts/templates/posts/base.html` | Layout común: estructura HTML5, menú, pie y enlace al CSS. Define el bloque `content`. |
| `posts/templates/posts/inicio.html` | Página de inicio con las últimas publicaciones. |
| `posts/templates/posts/acerca.html` | Página "Acerca de". |
| `posts/templates/posts/lista_posts.html` | Listado de posts publicados, recorridos con `{% for %}`. |
| `posts/templates/posts/detalle_post.html` | Detalle de un post, con su imagen y los botones Editar y Eliminar. |
| `posts/templates/posts/post_form.html` | Formulario para crear y editar posts (con `enctype="multipart/form-data"`). |
| `posts/templates/posts/post_confirm_delete.html` | Confirmación antes de eliminar un post. |
| `posts/static/posts/css/estilos.css` | Estilos del sitio. |
| `requirements.txt` | Dependencias del proyecto. |
| `.gitignore` | Archivos y carpetas que Git no sube al repositorio. |

## Configuración

En `blog_project/settings.py` se configuró:

- **Aplicación:** `posts` registrada en `INSTALLED_APPS` como `'posts.apps.PostsConfig'`.
- **Idioma:** `LANGUAGE_CODE = 'es-ar'` (español de Argentina).
- **Zona horaria:** `TIME_ZONE = 'America/Argentina/Buenos_Aires'`.
- **Archivos media:** `MEDIA_URL` y `MEDIA_ROOT` (ver "Manejo de imágenes").

## Archivos que no se suben al repositorio

El `.gitignore` excluye:

- `venv/`: el entorno virtual. Cada persona lo crea en su computadora con `requirements.txt`.
- `__pycache__/` y `*.pyc`: archivos que Python genera automáticamente.
- `.env`: archivo para variables privadas (contraseñas, claves).
- `db.sqlite3`: la base de datos local que genera Django. Se recrea con `migrate`, y los posts de ejemplo con `loaddata posts`.

La carpeta `media/posts/` **sí** se sube, porque contiene la imagen del post de ejemplo del fixture.

## Dependencias

- Django 6.1.2
- Pillow 13.0.0 (manejo de imágenes)
- asgiref, sqlparse y tzdata (dependencias que Django instala automáticamente)