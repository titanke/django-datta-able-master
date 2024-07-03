# Generated by Django 4.2.9 on 2024-07-02 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estu',
            fields=[
                ('dni', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('apeliidoP', models.CharField(max_length=35)),
                ('apeliidoM', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('feNac', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechmat', models.DateField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estu')),
            ],
        ),
    ]
