# Generated by Django 3.0.2 on 2020-01-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campdata',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
