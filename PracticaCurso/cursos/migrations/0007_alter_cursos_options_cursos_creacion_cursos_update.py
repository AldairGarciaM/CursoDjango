# Generated by Django 4.0.5 on 2022-06-28 02:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_cursos_creador_cursos_descripcion_cursos_nombre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['-creacion'], 'verbose_name': 'Cursos', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='cursos',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursos',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]