# Generated by Django 5.1.4 on 2025-02-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='volunteer',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
