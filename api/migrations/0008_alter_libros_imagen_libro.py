# Generated by Django 4.0.3 on 2022-04-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_tipoinfraccion_id_tipo_infraccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='imagen_libro',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='images/libros/', verbose_name='Imagen del libro'),
        ),
    ]