# Generated by Django 4.0.4 on 2022-06-14 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_eventlogin_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='clubname',
        ),
    ]