# Generated by Django 5.0.6 on 2024-05-30 12:47

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='defaultProfile.png', force_format='webp', keep_meta=True, null=True, quality=75, scale=None, size=[300, 300], upload_to='profileImages/'),
        ),
    ]
