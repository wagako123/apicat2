# Generated by Django 3.2.7 on 2021-09-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0002_carowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
