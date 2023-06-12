# Generated by Django 4.2.1 on 2023-05-31 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_usuario_jefe_area', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuario.usuario')),
                ('area', models.CharField(default='', max_length=50)),
                ('estado_area', models.CharField(default='Activo', max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(default='', max_length=50)),
                ('estado_grado', models.CharField(default='Activo', max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True, max_length=50)),
            ],
        ),
    ]