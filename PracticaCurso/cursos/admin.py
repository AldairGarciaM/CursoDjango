from django.contrib import admin
from .models import Cursos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('creacion', 'update')
    list_display= ('imagen', 'nombre', 'creador', 'requisitos', 'descripcion', 'creacion')
    search_fields= ('imagen', 'nombre', 'creador', 'requisitos', 'descripcion', 'creacion')
    date_hierarchy= 'creacion'
    list_filter= ('nombre', 'creador')

admin.site.register(Cursos, AdministrarModelo)