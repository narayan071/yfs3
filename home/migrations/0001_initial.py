# Generated by Django 4.2.3 on 2023-08-28 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('feedback', models.TextField()),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Time submitted')),
            ],
        ),
    ]
