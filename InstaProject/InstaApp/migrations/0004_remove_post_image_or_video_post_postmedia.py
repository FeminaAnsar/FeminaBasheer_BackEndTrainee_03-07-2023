# Generated by Django 4.1.7 on 2023-07-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstaApp', '0003_rename_user_comment_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_or_video',
        ),
        migrations.AddField(
            model_name='post',
            name='postmedia',
            field=models.FileField(null=True, upload_to='uploads/post_media'),
        ),
    ]
