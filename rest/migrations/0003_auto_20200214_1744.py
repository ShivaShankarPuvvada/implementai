# Generated by Django 3.0.3 on 2020-02-14 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20200214_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='rack_obj',
            new_name='rack',
        ),
        migrations.RemoveField(
            model_name='rack',
            name='student_object',
        ),
    ]