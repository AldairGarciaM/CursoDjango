# Generated by Django 4.0.5 on 2022-08-05 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0013_alter_cursocomentario_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursocomentario',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Cursos'),
        ),
    ]
