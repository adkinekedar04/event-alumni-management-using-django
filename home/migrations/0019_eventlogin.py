# Generated by Django 4.0.4 on 2022-06-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_profile_profilecollege'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(default='', max_length=122)),
                ('collegeemail', models.CharField(default='', max_length=122)),
                ('mis', models.CharField(default='', max_length=12)),
                ('branch', models.CharField(default='', max_length=122)),
                ('mobile', models.CharField(default='', max_length=10)),
                ('eventreg', models.CharField(default='', max_length=122)),
            ],
        ),
    ]