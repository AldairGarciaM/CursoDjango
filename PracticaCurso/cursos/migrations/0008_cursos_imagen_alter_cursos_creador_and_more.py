# Generated by Django 4.0.5 on 2022-06-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_alter_cursos_options_cursos_creacion_cursos_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='creador',
            field=models.TextField(default=True, verbose_name='crea'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='descripcion',
            field=models.TextField(default=True, verbose_name='desc'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nombre',
            field=models.TextField(default=True, verbose_name='Nam'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='precio',
            field=models.TextField(default=True, verbose_name='prec'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='requisitos',
            field=models.TextField(default=True, verbose_name='req'),
        ),
    ]