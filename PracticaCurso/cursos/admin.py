from django.contrib import admin
from .models import Cursos

# Register your models here.

class Fechas(admin.ModelAdmin):
    readonly_fields= ('creacion', 'update')

admin.site.register(Cursos, Fechas)