# Generated by Django 3.0.7 on 2021-04-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0009_auto_20210415_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]