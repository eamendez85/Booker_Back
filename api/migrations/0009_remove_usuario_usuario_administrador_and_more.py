# Generated by Django 4.0.3 on 2022-05-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_libros_imagen_libro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuario_administrador',
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(default='E', max_length=1, verbose_name='Tipo usuario'),
            preserve_default=False,
        ),
    ]
