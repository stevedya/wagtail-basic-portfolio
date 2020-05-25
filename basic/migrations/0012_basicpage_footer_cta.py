# Generated by Django 2.2.12 on 2020-05-25 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cta', '0001_initial'),
        ('basic', '0011_auto_20200524_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicpage',
            name='footer_cta',
            field=models.ForeignKey(blank=True, help_text='Optional footer call to action for this page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cta.CallToAction'),
        ),
    ]