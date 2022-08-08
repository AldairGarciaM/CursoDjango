from django.contrib import admin
from .models import Cursos
from .models import CursoComentario
from .models import comentarioContacto
from .models import documentos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('creacion', 'update')
    list_display= ('nombre', 'creador', 'requisitos', 'descripcion', 'creacion', 'imagen')
    search_fields= ('nombre', 'creador', 'requisitos', 'descripcion', 'creacion', 'imagen')
    date_hierarchy= 'creacion'
    list_filter= ('nombre', 'creador')

class ModeloComentario(admin.ModelAdmin):
    list_display= ('id', 'coment')
    search_fields= ('id', 'created')
    date_hierarchy= 'created'
    readonly_fields= ('created', 'id')

class ComentarioCurso(admin.ModelAdmin):
    list_display=('id', 'correo')
    search_fields= ('nombre', 'correo')
    date_hierarchy= 'created'
    readonly_fields= ('created', 'id')


admin.site.register(Cursos, AdministrarModelo)

admin.site.register(CursoComentario, ModeloComentario)

admin.site.register(comentarioContacto, ComentarioCurso)
