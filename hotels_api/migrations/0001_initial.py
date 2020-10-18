# Generated by Django 3.1.2 on 2020-10-18 02:23

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
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
                ('slug', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('pets', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('extras', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('hotel_name', models.ForeignKey(default='auth.user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='hotels_api.room')),
            ],
        ),
    ]
