# Generated by Django 2.2.1 on 2021-12-20 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0010_contentquality_coursedepthandcovergae_coursepace_qualifiedinstructor_videoquality'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='about',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
