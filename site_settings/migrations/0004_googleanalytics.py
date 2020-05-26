# Generated by Django 2.2.12 on 2020-05-26 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('site_settings', '0003_socialmediasettings_social_media_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.CharField(blank=True, help_text='Enter in your google analytics tracking ID to enable analytics', max_length=20)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]