# Generated by Django 4.2.1 on 2023-05-25 22:10

import Basquet1.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basquet1', '0004_rename_imagen_articulos_descriptivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='descriptivo',
            field=models.ImageField(blank=True, null=True, upload_to='articulos', validators=[Basquet1.validators.validate_image_size]),
        ),
    ]
