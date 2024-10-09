# Generated by Django 5.0.7 on 2024-10-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0002_employee_load_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='load_tasks',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('New Task', 'New Task'), ('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=50),
        ),
    ]
