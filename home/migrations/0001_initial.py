# Generated by Django 4.2.9 on 2024-02-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=60)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
