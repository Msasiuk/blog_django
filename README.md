# blog_django

Blog web desarrollado con Django en el curso de Python de Coderhouse.

## Descripción

Este repositorio contiene el blog web. Es la continuación del blog por consola de las preentregas anteriores, ahora como aplicación web con Django.

En esta versión (Preentrega 9) el blog se conecta con una base de datos SQLite usando el ORM de Django. Se agregaron:

- El modelo `Post` (título, contenido, autor, fecha de creación y estado).
- El registro del modelo en el panel de administración, con columnas, filtros y búsqueda.
- La página `/posts/`, que lista las publicaciones con estado "Publicado" obtenidas desde la base de datos.
- Las últimas 3 publicaciones en la página de inicio.

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
   | Acerca de | http://127.0.0.1:8000/acerca/ |
   | Panel admin | http://127.0.0.1:8000/admin/ |


   Desde el menú superior se puede navegar entre las páginas.

3. Para detener el servidor, presionar `Ctrl + C` en la terminal.

## Base de datos

Antes del primer uso hay que crear la base de datos:

```
python manage.py migrate
```

Esto genera el archivo `db.sqlite3` con todas las tablas. Ese archivo no se sube al repositorio: cada persona lo crea en su computadora.

Para cargar los posts de ejemplo (opcional):

```
python manage.py loaddata posts
```

## Panel de administración

1. Crear un usuario administrador:

   ```
   python manage.py createsuperuser
   ```

   Pide nombre de usuario, email (opcional) y contraseña. La contraseña no se ve mientras se escribe.

2. Levantar el servidor y entrar a http://127.0.0.1:8000/admin/ con ese usuario.

3. En **Posts** se pueden crear, editar y eliminar publicaciones. Solo las que tienen estado **Publicado** se muestran en el sitio.

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
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── fixtures/
    │   └── posts.json
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   └── 0002_alter_post_titulo.py
    ├── models.py
    ├── tests.py
    ├── urls.py    
    ├── views.py
    │
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── lista_posts.html
    │       └── acerca.html
    │
    └── static/
        └── posts/
            └── css/
                └── estilos.css
```

| Archivo o carpeta | Para qué sirve |
|---|---|
| `manage.py` | Herramienta de Django para ejecutar comandos del proyecto (`runserver`, `startapp`, `migrate`). |
| `blog_project/` | Configuración general del proyecto. |
| `blog_project/settings.py` | Configuración: aplicaciones instaladas, idioma, zona horaria, base de datos. |
| `blog_project/urls.py` | Rutas (URLs) del proyecto. |
| `posts/` | Aplicación principal del blog. |
| `requirements.txt` | Dependencias del proyecto, generadas con `pip freeze > requirements.txt`. |
| `.gitignore` | Archivos y carpetas que Git no sube al repositorio. |
| `posts/urls.py` | Rutas de la app: inicio (`''`), posts (`posts/`) y acerca de (`acerca/`). |
| `posts/views.py` | Vistas `inicio()`, `lista_posts()` y `acerca()`Las dos primeras consultan la base con el ORM. |
| `posts/templates/posts/base.html` | Layout común: estructura HTML5, menú, pie y enlace al CSS. Define el bloque `content`. |
| `posts/templates/posts/inicio.html` | Página de inicio. Extiende de `base.html`. |
| `posts/templates/posts/acerca.html` | Página "Acerca de". Extiende de `base.html`. |
| `posts/static/posts/css/estilos.css` | Estilos del sitio. |
| `posts/models.py` | Modelo `Post`: define la tabla de publicaciones en la base de datos. |
| `posts/admin.py` | Registro del modelo en el panel admin (`PostAdmin`). |
| `posts/migrations/` | Migraciones que crean y actualizan la tabla de posts. |
| `posts/templates/posts/lista_posts.html` | Listado de posts publicados, recorridos con `{% for %}`. |
| `posts/fixtures/posts.json` | Posts de ejemplo para cargar con `loaddata`. |

## Aplicaciones

- **posts**: aplicación inicial para manejar las publicaciones del blog. Está registrada en `INSTALLED_APPS` como `'posts.apps.PostsConfig'`.

## Configuración

En `blog_project/settings.py` se configuró:

- **Idioma:** `LANGUAGE_CODE = 'es-ar'` (español de Argentina).
- **Zona horaria:** `TIME_ZONE = 'America/Argentina/Buenos_Aires'`.

## Archivos que no se suben al repositorio

El `.gitignore` excluye:

- `venv/`: el entorno virtual. Cada persona lo crea en su computadora con `requirements.txt`.
- `__pycache__/` y `*.pyc`: archivos que Python genera automáticamente.
- `.env`: archivo para variables privadas (contraseñas, claves).
- `db.sqlite3`: la base de datos local que genera Django.
- `db.sqlite3`: la base de datos local que genera Django. Se recrea con `migrate`, y los posts de ejemplo con `loaddata posts`.

## Dependencias

- Django 6.1.2
- asgiref, sqlparse y tzdata (dependencias que Django instala automáticamente)