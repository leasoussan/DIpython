# Generated by Django 3.1.4 on 2020-12-10 13:27

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_date_created', models.DateField()),
                ('vehicle_real_cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('vehicle_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehiclesize')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='RentalRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_daily_rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('rental_vehicle_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehiclesize')),
                ('rental_vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehicletype')),
            ],
        ),
    ]
