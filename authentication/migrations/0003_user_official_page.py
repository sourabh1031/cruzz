# Generated by Django 2.0.6 on 2018-11-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20181106_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='official_page',
            field=models.NullBooleanField(default=False),
        ),
    ]
