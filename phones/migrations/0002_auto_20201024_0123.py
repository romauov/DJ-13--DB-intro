# Generated by Django 3.1.2 on 2020-10-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]