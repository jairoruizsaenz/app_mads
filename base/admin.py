from django.contrib import admin
from .models import Solicitud
from import_export.admin import ImportExportModelAdmin

class RegistroSolicitud(ImportExportModelAdmin, admin.ModelAdmin):
    model = Solicitud

# admin.site.register(Solicitud)
admin.site.register(Solicitud, RegistroSolicitud)