# Generated by Django 3.0.2 on 2020-01-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_auto_20200126_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campdata',
            name='installs',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
