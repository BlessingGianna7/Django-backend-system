# Generated by Django 5.1.2 on 2024-10-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
        ('guiders', '0002_alter_guider_age_alter_guider_service_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='health_status',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='location',
        ),
        migrations.AddField(
            model_name='animal',
            name='guiders',
            field=models.ManyToManyField(related_name='animals', to='guiders.guider'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
