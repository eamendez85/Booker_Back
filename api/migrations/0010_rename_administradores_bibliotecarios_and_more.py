# Generated by Django 4.0.3 on 2022-05-12 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_usuario_usuario_administrador_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Administradores',
            new_name='Bibliotecarios',
        ),
        migrations.RenameField(
            model_name='bibliotecarios',
            old_name='doc_administrador',
            new_name='doc_bibliotecario',
        ),
        migrations.RenameField(
            model_name='bibliotecarios',
            old_name='id_administrador',
            new_name='id_bibliotecario',
        ),
        migrations.AlterModelTable(
            name='bibliotecarios',
            table='bibliotecarios',
        ),
    ]
