# Generated by Django 3.1.4 on 2020-12-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_animal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='img/'),
        ),
    ]