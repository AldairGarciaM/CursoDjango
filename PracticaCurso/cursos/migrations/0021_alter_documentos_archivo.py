# Generated by Django 4.0.5 on 2022-08-07 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0020_alter_documentos_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archivos'),
        ),
    ]