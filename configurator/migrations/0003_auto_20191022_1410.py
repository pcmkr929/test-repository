# Generated by Django 2.2.6 on 2019-10-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0002_auto_20191022_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instanceconfig',
            name='interval_ialarm',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='instanceconfig',
            name='interval_replicator',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=4),
        ),
    ]
