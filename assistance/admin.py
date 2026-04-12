from django.contrib import admin
from .models import Ayudantia, Tutoria, SolicitudAcademica

admin.site.register(Ayudantia)
admin.site.register(Tutoria)

@admin.register(SolicitudAcademica)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('ramo', 'cantidad_estudiantes', 'is_approved')
    list_editable = ('is_approved',)