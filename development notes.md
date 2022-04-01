# Notas de desarrollo

A continuación se presentan notas generales utilizadas para el desarrollo de aplicaciones utilizando el framework Django.

1. Crear un ambiente virtual para aislar la instalación de dependencias
```
python virtualenv env
```

2. Activar ambiente virtual
- Windows
    ```
    env\Scripts\activate
    ```

- Linux
    ```
    source env/bin/activate
    ```

3. Instalar dependencias y exportar archivo requirements.txt
- Se puede mandetener manualmente para tener mejor control
```
python -m pip install Django
pip freeze > requirements.txt
```

4. Crear el proyecto
```
django-admin startproject django_project
```

5. Crear la aplicación
```
python manage.py startapp aplicacion
```

6. Incluir la nueva app en archivo settings.py del proyecto
```
apregar aplicacion.apps.AplicacionConfig' en INSTALLED_APPS 
```
```
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
ALLOWED_HOSTS = ['*']
modificar configuración de base de datos (si se requiere) en archivo settings.py del proyecto
```

7. Ejecutar migración inicial de base de datos
```
python manage.py migrate
```

8. Crear un usuario de administración (por ejemplo user: admin, password: admin)
```
python manage.py createsuperuser
```

9. crear modelo
10. crear archivo urls.py de la aplicación
11. ajustar archivo views.py de la aplicación
12. ajustar archivo urls.py del proyecto > incluir archivo urls.py de la aplicación
13. ajustar archivo urls.py de la aplicación > redirección a views.py y funciones de la app, no ovlidar incluir app_name = 'nombre'

14. crear carpeta templates >> aplicacion/templates/aplicacion
15. crear archivos HTML correspondientes a las views.py 

16. Iterar
  - ajustar urls.py, views.py, .html
  - models.py (actualizar bases de datos después de modificar los atributos/variables)
    - python manage.py makemigrations
    - python manage.py migrate

17. Customize the admin form
como mínimo incluir:
```
from django.contrib import admin
from .models import Choice, Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```

18. static files
crea carpetas dentro de la app "static/aplicacion"
```
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'aplicacion/css/style.css' %}">
```
19. variables de apoyo, se puede usar el archivo de settings.py para almacenar información en variables 
```
from django.conf import settings
variable_temp = 'hola'
settings.variable_temp
```

20. Template general
crear carpeta templates al mismo nivel de la carpeta del proyecto
modificar variable Templates en archivo settings.py 
```
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
```
{% extends 'archivo_base.html' %}
{% block content %}
{% endblock %}
```
21. static files generales, se pueden tener archivos estaticos a nivel del proyecto

hacer ajustes en archivo settings.py
```
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = '/static/'
```
```
{% load static %}
<img src="{% static 'image/logo.gif' %}" alt="Smiley face" height="60" width="200">
```

22. Ejecutar servidor de desarrollo de Django
```
python manage.py runserver <ip>:<port>
python manage.py runserver 0:8000
```
