# Generated by Django 4.2.1 on 2023-05-31 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0005_carga_horaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas_estudiantes_curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nota', models.CharField(default='', max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True, max_length=50)),
                ('id_asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.asignatura')),
                ('id_carga_horaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.carga_horaria')),
                ('id_matriculados_estudiante_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.matriculados_estudiante')),
            ],
        ),
    ]
