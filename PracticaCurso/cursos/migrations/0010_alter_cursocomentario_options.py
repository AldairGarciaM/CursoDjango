# Generated by Django 4.0.5 on 2022-07-01 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0009_cursocomentario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursocomentario',
            options={'ordering': ['-created'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
    ]
