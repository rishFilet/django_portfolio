# Generated by Django 3.1.4 on 2021-04-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20210415_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomplishment',
            name='include_title',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'no')], default='yes', max_length=200, null=True, verbose_name='Show short title?'),
        ),
    ]
