# Generated by Django 5.0 on 2023-12-10 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('type', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]