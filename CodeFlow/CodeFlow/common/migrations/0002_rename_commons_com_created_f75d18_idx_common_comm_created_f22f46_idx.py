# Generated by Django 5.1.3 on 2024-11-29 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='comment',
            new_name='common_comm_created_f22f46_idx',
            old_name='commons_com_created_f75d18_idx',
        ),
    ]
