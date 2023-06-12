# Generated by Django 4.2.1 on 2023-05-31 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('academico', '0002_asignatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id_usuario_director_curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuario.usuario')),
                ('curso', models.CharField(default='', max_length=50)),
                ('estado_curso', models.CharField(default='Activo', max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True, max_length=50)),
                ('id_grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.grado')),
            ],
        ),
    ]
