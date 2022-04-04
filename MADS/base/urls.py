from django.urls import path
from .views import *
# from django.views.generic import TemplateView

# https://cosasdedevs.com/posts/como-crear-urls-amigables-con-slug-en-django/

app_name = 'baseApp'
urlpatterns = [
    path('solicitudes/', Home, name='solicitudes'),
    path('crear-solicitud/', CreateMapa, name='crear_solicitud'),
]
