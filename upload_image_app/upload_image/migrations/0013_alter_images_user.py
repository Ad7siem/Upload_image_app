# Generated by Django 4.1.7 on 2023-02-20 16:07

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_image', '0012_alter_images_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='user',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]