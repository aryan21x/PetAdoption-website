# Generated by Django 5.0.3 on 2024-04-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('shelter_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('pets', models.IntegerField(default=0)),
                ('phoneNumber', models.DecimalField(decimal_places=0, max_digits=10)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]