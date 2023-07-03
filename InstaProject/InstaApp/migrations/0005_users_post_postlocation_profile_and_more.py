# Generated by Django 4.1.7 on 2023-07-03 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InstaApp', '0004_remove_post_image_or_video_post_postmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('profile_picture', models.ImageField(upload_to='uploads/profile_pictures')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='postlocation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('bio', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='InstaApp.users')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstaApp.users'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='InstaApp.users'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='InstaApp.users'),
        ),
        migrations.AlterField(
            model_name='like',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstaApp.users'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstaApp.users'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
