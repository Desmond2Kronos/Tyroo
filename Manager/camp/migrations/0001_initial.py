# Generated by Django 3.0.2 on 2020-01-27 05:28

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
            name='CampData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(max_length=50)),
                ('campaigns', models.CharField(max_length=50)),
                ('schedule_start', models.DateTimeField(auto_now_add=True)),
                ('schedule_stop', models.DateTimeField(auto_now_add=True)),
                ('impressions', models.IntegerField(blank=True, default=0)),
                ('clicks', models.IntegerField(blank=True, default=0)),
                ('spend', models.IntegerField(blank=True, default=0)),
                ('eCPM', models.IntegerField(blank=True, default=0)),
                ('eCPC', models.IntegerField(blank=True, default=0)),
                ('installs', models.IntegerField(blank=True, default=0)),
                ('eCPI', models.IntegerField(blank=True, default=0)),
                ('status', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CampGatheredData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=50)),
                ('schedule_start', models.TimeField(blank=True)),
                ('schedule_stop', models.TimeField(blank=True)),
                ('impressions', models.IntegerField(blank=True, default=0)),
                ('clicks', models.IntegerField(blank=True, default=0)),
                ('spend', models.IntegerField(blank=True, default=0)),
                ('installs', models.IntegerField(blank=True, default=0)),
                ('status', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
