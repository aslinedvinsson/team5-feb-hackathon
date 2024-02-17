# Generated by Django 5.0.2 on 2024-02-17 11:09

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desciption', models.TextField(max_length=10000)),
                ('category', models.CharField(choices=[('fodd_and_drink', 'Food & Drink'), ('art_and_culture', 'Art & Culture'), ('single_and_ready_to_mingle', 'Single & ready to mingle'), ('adventure', 'Adventure')], default='Adventure', max_length=50)),
                ('location', models.CharField(blank=True, max_length=300)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('image_alt', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
