# Generated by Django 4.2.9 on 2024-02-20 19:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_alter_ateendee_newsletter_alter_event_status_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Post',
        ),
    ]
