# Generated by Django 5.0.7 on 2024-10-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_remove_employee_load_tasks_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='additional_info',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]