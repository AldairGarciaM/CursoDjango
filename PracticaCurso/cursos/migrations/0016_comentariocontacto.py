# Generated by Django 4.0.5 on 2022-08-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0015_alter_cursos_creador_alter_cursos_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarioContacto',
            fields=[
                ('update', models.DateTimeField(auto_created=True, verbose_name='Actualizacion')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('curos', models.CharField(max_length=50, verbose_name='Curso')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
            ],
            options={
                'verbose_name': 'Comentario Contacto',
                'verbose_name_plural': 'Comentarios Contacto',
                'ordering': ['-created'],
            },
        ),
    ]
