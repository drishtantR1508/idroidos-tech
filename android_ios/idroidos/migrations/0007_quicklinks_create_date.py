# Generated by Django 3.0.3 on 2020-06-20 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('idroidos', '0006_quicklinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='quicklinks',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
