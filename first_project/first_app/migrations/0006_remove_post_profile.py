# Generated by Django 4.2.1 on 2023-05-16 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_alter_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]
