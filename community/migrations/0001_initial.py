# Generated by Django 3.0.7 on 2021-04-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('place_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
