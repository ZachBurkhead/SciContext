# Generated by Django 5.0.6 on 2024-07-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='type',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
