# Generated by Django 4.2.2 on 2023-10-13 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilizacion_buses_cargadores_app', '0005_rename_estado_id_bus_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargador',
            old_name='estado_id',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='historialutilizacionbushora',
            old_name='bus_id',
            new_name='bus',
        ),
        migrations.RenameField(
            model_name='historialutilizacionbushora',
            old_name='hora_id',
            new_name='hora',
        ),
        migrations.RenameField(
            model_name='historialutilizacioncargadorhora',
            old_name='bus_id',
            new_name='bus',
        ),
        migrations.RenameField(
            model_name='historialutilizacioncargadorhora',
            old_name='cargador_id',
            new_name='cargador',
        ),
        migrations.RenameField(
            model_name='historialutilizacioncargadorhora',
            old_name='hora_id',
            new_name='hora',
        ),
    ]