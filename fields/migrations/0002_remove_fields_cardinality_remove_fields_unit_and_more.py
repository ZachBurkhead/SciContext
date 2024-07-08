# Generated by Django 5.0.6 on 2024-07-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fields',
            name='cardinality',
        ),
        migrations.RemoveField(
            model_name='fields',
            name='unit',
        ),
        migrations.AddField(
            model_name='fields',
            name='newname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
