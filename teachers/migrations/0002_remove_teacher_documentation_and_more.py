# Generated by Django 5.0 on 2023-12-10 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='documentation',
        ),
        migrations.AddField(
            model_name='teacherdocumentation',
            name='teacher',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='teachers.teacher'),
            preserve_default=False,
        ),
    ]