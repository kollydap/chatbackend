# Generated by Django 4.0.4 on 2022-06-08 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_friendrequest_friendlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='timestaamp',
            new_name='timestamp',
        ),
    ]