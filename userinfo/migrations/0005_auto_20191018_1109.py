# Generated by Django 2.2.6 on 2019-10-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_auto_20191018_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
