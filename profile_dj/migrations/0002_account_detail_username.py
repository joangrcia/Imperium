# Generated by Django 5.0 on 2023-12-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_dj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_detail',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]