# Generated by Django 4.2.2 on 2023-10-12 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilizacion_buses_cargadores_app', '0002_alter_estadobus_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identificador Único de Cada Bus')),
                ('placa', models.CharField(db_index=True, max_length=6, verbose_name='Placa del Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Cargador',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identificador Único de Cada Cargador')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCargador',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identificador de cada estado que puede tener Cargador')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Tipos Estados que puede tener un Cargador')),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identificador de Cada Hora')),
                ('descripcion', models.CharField(max_length=4, verbose_name='Descripcion de Hora')),
                ('hora_pico', models.BooleanField(verbose_name='Define si la Hora es Pico o No')),
            ],
        ),
        migrations.AlterField(
            model_name='estadobus',
            name='descripcion',
            field=models.CharField(max_length=30, verbose_name='Tipo de estado que puede tener un bus'),
        ),
        migrations.AlterField(
            model_name='estadobus',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identificador de cada estado que puede tener un bus'),
        ),
        migrations.CreateModel(
            name='UtilizacionCargadorBus',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identificador del Historial')),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.bus')),
                ('cargador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.cargador')),
                ('hora_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.hora')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialUtilizacionCargadorHora',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identiicador Unico del Historial')),
                ('cargador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.cargador')),
                ('hora_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.hora')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialUtilizacionBusHora',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Identiicador Unico del Historial')),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.bus')),
                ('hora_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.hora')),
            ],
        ),
        migrations.AddField(
            model_name='cargador',
            name='estado_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.estadocargador'),
        ),
        migrations.AddField(
            model_name='bus',
            name='estado_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilizacion_buses_cargadores_app.estadobus'),
        ),
    ]