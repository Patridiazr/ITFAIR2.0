# Generated by Django 2.1.2 on 2018-11-14 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_auto_20181113_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='celu',
            new_name='telefono',
        ),
    ]
