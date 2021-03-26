# Generated by Django 3.0.6 on 2020-07-15 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200715_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 18, 45, 37, 855582)),
        ),
        migrations.AlterField(
            model_name='authors',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 18, 45, 37, 833315)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 18, 45, 37, 857085)),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 18, 45, 37, 857820)),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
