# Generated by Django 2.2.6 on 2019-10-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20191018_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
