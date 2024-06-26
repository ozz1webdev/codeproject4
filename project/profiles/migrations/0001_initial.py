# Generated by Django 5.0.6 on 2024-05-30 10:14

import django.db.models.deletion
import django_resized.forms
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.jpg', force_format='webp', keep_meta=True, null=True, quality=75, scale=None, size=[300, 300], upload_to='profileImages/')),
                ('bio', models.TextField(blank=True, max_length=2500)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('hobbys', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
