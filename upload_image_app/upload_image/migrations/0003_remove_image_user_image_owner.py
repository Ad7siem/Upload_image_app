# Generated by Django 4.1.7 on 2023-02-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_image', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Image Owner'),
        ),
    ]
