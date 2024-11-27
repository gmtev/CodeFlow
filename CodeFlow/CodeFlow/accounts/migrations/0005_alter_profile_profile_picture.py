# Generated by Django 5.1.3 on 2024-11-27 11:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]