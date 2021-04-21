# Generated by Django 3.1.4 on 2021-04-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20210413_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardHeaders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200, verbose_name='Role / Certification')),
                ('role_id', models.CharField(max_length=200, null=True, unique=True, verbose_name='Role / Certification id')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.cvsectionheader')),
            ],
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='job_role',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='IndustryExperience',
        ),
    ]
