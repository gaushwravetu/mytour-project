# Generated by Django 3.0.7 on 2021-04-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0012_auto_20210415_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='one_strong_point_for_recommendations',
            field=models.CharField(default='In 2-3 words', max_length=100),
        ),
    ]