# Generated by Django 3.1.4 on 2021-04-13 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_industryexperience_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVSectionHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='industryexperience',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.cvsectionheader'),
        ),
    ]