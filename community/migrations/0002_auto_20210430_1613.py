# Generated by Django 3.0.7 on 2021-04-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='desc',
            new_name='full_desc',
        ),
        migrations.AddField(
            model_name='post',
            name='short_desc',
            field=models.CharField(default='In less than 250 words', max_length=255),
        ),
    ]