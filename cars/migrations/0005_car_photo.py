# Generated by Django 5.1.7 on 2025-03-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
