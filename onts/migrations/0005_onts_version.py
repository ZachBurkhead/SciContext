# Generated by Django 5.0.6 on 2024-07-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onts', '0004_onts_trmcnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='onts',
            name='version',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
