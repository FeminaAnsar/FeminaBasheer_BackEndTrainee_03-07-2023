# Generated by Django 4.1.7 on 2023-07-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstaApp', '0002_alter_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(upload_to='uploads/profile_pictures'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
