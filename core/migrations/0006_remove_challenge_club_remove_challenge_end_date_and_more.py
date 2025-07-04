# Generated by Django 5.2.3 on 2025-07-02 15:49

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_club_admins_alter_club_created_at_alter_club_members_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='club',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='read',
        ),
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.RemoveField(
            model_name='user',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
        migrations.AddField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='publications/'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='clubs',
            field=models.ManyToManyField(blank=True, related_name='club_members', to='core.club'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='club',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='joined_clubs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clubmessage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publication',
            name='disliked_by',
            field=models.ManyToManyField(related_name='disliked_publications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publication',
            name='domain',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_publications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publication',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='medias/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='type',
            field=models.CharField(blank=True, choices=[('NEWS', 'News'), ('EVENT', 'Event')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
