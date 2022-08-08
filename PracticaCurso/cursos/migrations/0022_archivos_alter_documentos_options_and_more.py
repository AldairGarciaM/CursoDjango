# Generated by Django 4.0.5 on 2022-08-08 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0021_alter_documentos_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'ordering': ['-create'],
            },
        ),
        migrations.AlterModelOptions(
            name='documentos',
            options={},
        ),
        migrations.RemoveField(
            model_name='documentos',
            name='archivo',
        ),
        migrations.RemoveField(
            model_name='documentos',
            name='created',
        ),
        migrations.RemoveField(
            model_name='documentos',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='documentos',
            name='update',
        ),
    ]
