# Generated by Django 5.0.3 on 2024-04-29 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_page', '0002_pet_image_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_path',
        ),
    ]