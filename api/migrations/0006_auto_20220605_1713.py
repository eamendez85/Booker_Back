# Generated by Django 3.2.1 on 2022-06-05 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_deprestamos_fec_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deprestamos',
            name='estado',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='deprestamos',
            name='id_bibliotecario',
            field=models.ForeignKey(db_column='id_bibliotecario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.bibliotecarios'),
        ),
    ]
