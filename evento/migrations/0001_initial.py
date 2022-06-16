# Generated by Django 3.2.7 on 2021-09-29 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_evento', models.CharField(max_length=10, verbose_name='Codigo de evento')),
                ('descripcion_evento', models.CharField(max_length=500, verbose_name='Descripcion de evento')),
            ],
            options={
                'db_table': 'codigo_evento',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificacion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Justificacion')),
                ('autorizado_por', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autorizado por')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='Fecha de finalizacion')),
                ('fecha_registro', models.DateField(blank=True, null=True, verbose_name='Fecha de registro')),
                ('usuario_registro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Usuario que registró')),
                ('codigo_evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evento.codigoevento', verbose_name='Codigo del evento')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado', verbose_name='Empleado')),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
