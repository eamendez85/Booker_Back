# Generated by Django 4.0.3 on 2022-06-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_merge_20220609_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='fec_devolucion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
