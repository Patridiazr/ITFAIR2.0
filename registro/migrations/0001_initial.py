# Generated by Django 2.2.dev20180621213648 on 2018-11-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=100)),
                ('orga', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=100)),
                ('celu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=100)),
                ('contra', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]