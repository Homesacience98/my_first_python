# Generated by Django 4.2.1 on 2023-05-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_remove_post_post_img_post_user_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_img', verbose_name='Post Image'),
        ),
    ]
