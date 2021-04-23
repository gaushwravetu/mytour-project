# Generated by Django 3.0.7 on 2021-04-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0024_auto_20210417_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='features_to_mention',
            new_name='Explain_each_feature',
        ),
        migrations.AddField(
            model_name='place',
            name='feature1',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='place',
            name='feature2',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='place',
            name='feature3',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='place',
            name='feature4',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='place',
            name='feature5',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]