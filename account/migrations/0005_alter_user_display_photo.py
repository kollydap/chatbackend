# Generated by Django 4.0.4 on 2022-06-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_timestaamp_friendrequest_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
