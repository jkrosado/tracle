# Generated by Django 3.0.7 on 2020-06-27 14:54

import backend.models
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('channel_id', models.CharField(blank=True, editable=False, max_length=11)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='UNTITLED VIDEO', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('watch_id', models.CharField(blank=True, max_length=11, null=True)),
                ('visibility', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public'), ('UNLISTED', 'Unlisted')], default='PUBLIC', max_length=8)),
                ('views', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploaded_file', models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/danjo/Projects/tracle/uploads'), upload_to=backend.models.get_video_location)),
                ('thumbnail', models.CharField(max_length=255, null=True)),
                ('video_status', models.CharField(choices=[('queued', 'Queued'), ('draft', 'Draft'), ('started', 'Processing'), ('finished', 'Done'), ('failed', 'Error')], db_column='video_status', default='draft', max_length=255)),
                ('job_id', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Category')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='backend.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Channel')),
                ('to_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='backend.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Channel')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='backend.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Channel')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='backend.Video')),
            ],
        ),
    ]
