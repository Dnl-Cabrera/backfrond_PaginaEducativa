# Generated by Django 4.2.1 on 2023-06-01 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0006_notas_estudiantes_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculados_estudiante',
            name='estado_lista_estudiante',
            field=models.CharField(default='Activo', max_length=50),
        ),
    ]
