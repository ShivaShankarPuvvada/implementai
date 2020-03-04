# Generated by Django 3.0.3 on 2020-03-04 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('experience_from', models.CharField(default='00', max_length=2)),
                ('experience_to', models.CharField(default='00', max_length=2)),
                ('educational_qualification', models.CharField(blank=True, max_length=25, null=True)),
                ('certifications', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('notice_period_in_days', models.CharField(default='0', max_length=3)),
                ('job_type', models.CharField(choices=[('PE', 'Permanent'), ('CO', 'Contract')], default='PE', max_length=2)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Skill')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
