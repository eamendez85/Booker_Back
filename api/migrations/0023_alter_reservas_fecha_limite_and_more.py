# Generated by Django 4.0.3 on 2022-06-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_deprestamos_id_bibliotecario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='fecha_limite',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fecha_reserva',
            field=models.DateTimeField(null=True),
        ),
    ]
