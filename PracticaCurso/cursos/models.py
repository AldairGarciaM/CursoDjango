from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Cursos(models.Model):
    imagen= models.ImageField(null=True, upload_to="fotos",verbose_name="Imagen")
    nombre= models.TextField(default=True, verbose_name="Nam")
    creador= models.TextField(default=True, verbose_name="crea")
    requisitos= models.TextField(default=True, verbose_name="req")
    descripcion= models.TextField(default=True, verbose_name="desc")
    precio= models.TextField(default=True, verbose_name="prec")
    creacion= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name= "Cursos"
        verbose_name_plural= "Cursos"
        ordering= ["-creacion"]

    def __str__(self):
        return self.nombre