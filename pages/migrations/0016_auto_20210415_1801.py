# Generated by Django 3.1.4 on 2021-04-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20210413_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvsectionheader',
            name='section_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='company_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
