# Generated by Django 3.0.6 on 2020-05-15 03:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0003_todo_tasktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tasktime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
