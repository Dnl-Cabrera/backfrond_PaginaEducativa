# Generated by Django 4.2.1 on 2023-05-31 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(default='', max_length=50)),
                ('estado_asignatura', models.CharField(default='Activo', max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True, max_length=50)),
                ('id_Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.area')),
                ('id_grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.grado')),
            ],
        ),
    ]
