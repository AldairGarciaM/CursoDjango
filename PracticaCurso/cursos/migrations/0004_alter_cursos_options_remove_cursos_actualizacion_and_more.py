# Generated by Django 4.0.5 on 2022-06-28 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_cursos_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={},
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='actualizacion',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='creacion',
        ),
    ]
