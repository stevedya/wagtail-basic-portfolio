# Generated by Django 2.2.12 on 2020-05-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_socialmediasettings_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='social_media_header',
            field=models.CharField(default='Other ways to stalk me', max_length=255),
        ),
    ]
