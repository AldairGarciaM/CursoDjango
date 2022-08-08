from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Cursos(models.Model):
    imagen= models.ImageField(null=True, upload_to="fotos",verbose_name="Imagen")
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    creador= models.CharField(max_length=50, verbose_name="Creador")
    requisitos= models.TextField(verbose_name="Requisitos")
    descripcion= models.TextField(verbose_name="Descripcion")
    precio= models.CharField(max_length=50, verbose_name="Precio")
    creacion= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name= "Cursos"
        verbose_name_plural= "Cursos"
        ordering= ["-creacion"]

    def __str__(self):
        return self.nombre

class CursoComentario(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Llave")
    creador= models.ForeignKey(Cursos, on_delete=models.CASCADE,verbose_name="Cursos")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Registro")
    coment= RichTextField(default=False, verbose_name="Comentarios")
    class Meta:
        verbose_name= "Comentario"
        verbose_name_plural= "Comentarios"
        ordering= ["-created"]

    def __str__(self):
        return self.coment

class comentarioContacto(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    correo=models.CharField(max_length=50, verbose_name="Correo")
    curos= models.CharField(max_length=50, verbose_name="Curso")
    comentario= models.TextField(verbose_name="Comentario")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    update= models.DateTimeField(auto_now_add=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name= "Comentario Contacto"
        verbose_name_plural= "Comentarios Contacto"
        ordering= ["-created"]

    def __str__(self):
        return self.correo

class documentos(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    titulo= models.CharField (max_length=50, verbose_name="Titulo")


class Archivos(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    titulo= models.CharField(max_length=50, verbose_name="Titulo")
    descripcion= models.CharField(max_length=50, verbose_name="Descripcion")
    archivo= models.FileField(upload_to="archivos", null=True, blank=True)
    create=models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    update=models.DateTimeField(auto_now_add=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name="Archivo"
        verbose_name_plural="Archivos"
        ordering=["-create"]

    def __str__(self):
        return self.titulo