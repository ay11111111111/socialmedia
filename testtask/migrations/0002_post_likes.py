# Generated by Django 3.0.6 on 2020-10-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
