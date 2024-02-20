# Generated by Django 4.2.10 on 2024-02-20 15:45

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('slot', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_event', models.DateField()),
                ('created_on', models.DateTimeField()),
                ('registration_expires', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('banner', cloudinary.models.CloudinaryField(default='placeholder3', max_length=255, verbose_name='image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberAteendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('newsletter', models.IntegerField(choices=[(0, 'True'), (1, 'False')], default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiled_member_attendees', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Ateendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('newsletter', models.IntegerField(choices=[(0, 'True'), (1, 'False')], default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anonymous_attendees', to='events.event')),
            ],
        ),
    ]
