# Generated by Django 4.0.4 on 2022-06-14 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_eventlogin_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlogin',
            name='event_name',
        ),
    ]