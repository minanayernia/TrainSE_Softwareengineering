# Generated by Django 2.2.1 on 2022-01-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0018_reportcomment_reportresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notiftype',
            field=models.CharField(choices=[('CR', 'commentReply'), ('LC', 'likeComment'), ('R', 'Request')], max_length=2),
        ),
    ]
