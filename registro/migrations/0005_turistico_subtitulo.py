# Generated by Django 2.1.2 on 2018-11-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20181112_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='turistico',
            name='subtitulo',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
    ]
