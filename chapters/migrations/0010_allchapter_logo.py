# Generated by Django 4.2.3 on 2023-09-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0009_allchapter_selected_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allchapter',
            name='logo',
            field=models.ImageField(default='', upload_to='ch_logo'),
        ),
    ]
