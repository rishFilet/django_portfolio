# Generated by Django 3.1.4 on 2021-04-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20210415_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdescription',
            name='job_role',
        ),
        migrations.AddField(
            model_name='description',
            name='logos',
            field=models.FileField(blank=True, default='', null=True, upload_to='cv_logos'),
        ),
        migrations.DeleteModel(
            name='JobAccomplishment',
        ),
        migrations.DeleteModel(
            name='JobDescription',
        ),
    ]
