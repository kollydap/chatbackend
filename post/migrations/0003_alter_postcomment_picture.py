# Generated by Django 4.0.4 on 2022-06-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_reaction_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
