# Generated by Django 4.0.4 on 2022-06-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220605_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deprestamos',
            name='fec_prestamo',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='fec_devolucion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fecha_limite',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='fecha_reserva',
            field=models.DateField(null=True),
        ),
    ]
