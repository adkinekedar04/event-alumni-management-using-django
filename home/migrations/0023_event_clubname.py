# Generated by Django 4.0.4 on 2022-06-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_event_clubname'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='clubname',
            field=models.CharField(default='', max_length=122),
        ),
    ]