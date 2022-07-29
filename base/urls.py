from django.urls import path
from .views import *
# from django.views.generic import TemplateView

# https://cosasdedevs.com/posts/como-crear-urls-amigables-con-slug-en-django/

app_name = 'baseApp'
urlpatterns = [
    path('solicitudes/', ListSolicitudes, name='solicitudes'),
    path('crear-solicitud/', CreateSolicitud, name='crear_solicitud'),
    path('solicitud/<int:solicitud_pk>/', DetailsSolicitud, name='detalles_solicitud'),
    path('editar-solicitud/<int:solicitud_pk>/', UpdateSolicitud, name='editar_solicitud'),
    path('borrar-solicitud/<int:solicitud_pk>/', DeleteSolicitud, name='borrar_solicitud'),
    path('generate_PDF_document/<int:solicitud_pk>/', generate_PDF_document, name='generate_PDF_document'),
]
