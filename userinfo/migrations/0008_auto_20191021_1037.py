# Generated by Django 2.2.6 on 2019-10-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_auto_20191021_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
