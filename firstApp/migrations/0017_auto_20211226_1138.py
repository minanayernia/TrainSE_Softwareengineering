# Generated by Django 2.2.1 on 2021-12-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0016_notification_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentquality',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='coursedepthandcovergae',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='coursepace',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='likecomment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='qualifiedinstructor',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
        migrations.AlterField(
            model_name='videoquality',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create date'),
        ),
    ]
