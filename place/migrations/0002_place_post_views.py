# Generated by Django 3.0.7 on 2021-05-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='post_views',
            field=models.IntegerField(default=1),
        ),
    ]
