# Generated by Django 4.0.3 on 2022-04-04 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_imagen_libros_imagen_libro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libros',
            old_name='imagen_libro',
            new_name='imagen',
        ),
    ]
