# Generated by Django 3.1.4 on 2021-04-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_jobdescription_company_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='industryexperience',
            name='role_id',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]