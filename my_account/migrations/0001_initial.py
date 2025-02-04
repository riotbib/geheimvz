# Generated by Django 5.1.2 on 2024-11-13 16:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def create_notification_settings_for_existing_users(apps, schema_editor):
    User = apps.get_model("core", "User")
    NotificationSettings = apps.get_model("account", "NotificationSettings")
    for u in User.objects.all():
        s = NotificationSettings(owner=u)
        s.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_new_pinboard_message', models.BooleanField(default=True, verbose_name='On new pinboard message')),
                ('on_new_friend_request', models.BooleanField(default=True, verbose_name='On new friend request')),
                ('on_new_group_invitation', models.BooleanField(default=True, verbose_name='On new group invitation')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notification_settings', to=settings.AUTH_USER_MODEL)),
                ('on_new_private_message', models.BooleanField(default=True, verbose_name='On new private message')),
            ],
        ),
        migrations.RunPython(create_notification_settings_for_existing_users),
    ]
