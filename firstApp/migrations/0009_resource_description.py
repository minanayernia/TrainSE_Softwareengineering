# Generated by Django 2.2.1 on 2021-12-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0008_auto_20211207_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]