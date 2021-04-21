# Generated by Django 3.1.4 on 2021-04-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20210415_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='month_ended',
            field=models.IntegerField(default=0, verbose_name='Month Ended (enter 0 if not available)'),
        ),
        migrations.AlterField(
            model_name='description',
            name='year_ended',
            field=models.IntegerField(default=0, verbose_name='Year Ended (enter 0 if not available)'),
        ),
    ]
