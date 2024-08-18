# Generated by Django 5.0.4 on 2024-07-25 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
