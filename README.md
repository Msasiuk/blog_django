# blog_django

Blog web desarrollado con Django en el curso de Python de Coderhouse.

## Descripción

Este repositorio contiene la estructura inicial del blog web. Es la continuación del blog por consola de las preentregas anteriores, ahora como aplicación web con Django.

En esta versión (Preentrega 8) se agregaron templates con herencia (`base.html`), las páginas de inicio y “Acerca de”, rutas propias de la app y estilos CSS.

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
   | Acerca de | http://127.0.0.1:8000/acerca/ |


   Desde el menú superior se puede navegar entre las dos páginas.

3. Para detener el servidor, presionar `Ctrl + C` en la terminal.

Al levantar el servidor aparece un aviso en rojo: *"You have 18 unapplied migration(s)"*. No es un error: indica que todavía no se creó la base de datos. Para crearla se puede ejecutar `python manage.py migrate`, que genera el archivo `db.sqlite3` (ese archivo no se sube al repositorio).

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
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py    
    ├── views.py
    │
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
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
| `posts/urls.py` | Rutas de la app: inicio (`''`) y acerca de (`acerca/`). |
| `posts/views.py` | Vistas `inicio()` y `acerca()`, que devuelven templates con `render()`. |
| `posts/templates/posts/base.html` | Layout común: estructura HTML5, menú, pie y enlace al CSS. Define el bloque `content`. |
| `posts/templates/posts/inicio.html` | Página de inicio. Extiende de `base.html`. |
| `posts/templates/posts/acerca.html` | Página "Acerca de". Extiende de `base.html`. |
| `posts/static/posts/css/estilos.css` | Estilos del sitio. |

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

## Dependencias

- Django 6.1.2
- asgiref, sqlparse y tzdata (dependencias que Django instala automáticamente)