# Generated by Django 4.2.1 on 2023-05-28 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Basquet1', '0011_alter_articulos_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='descriptivo',
        ),
        migrations.RemoveField(
            model_name='clubes',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='entrenadores',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='jugadores',
            name='imagen',
        ),
    ]
