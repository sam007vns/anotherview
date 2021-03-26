# Generated by Django 3.0.6 on 2020-07-15 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200715_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='myfield',
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_type',
            field=models.CharField(choices=[('Trending News', 'Trending News'), ('Science', 'Science'), ('Technology', 'Technology'), ('Social Media', 'Social Media'), ('Sports', 'Sports'), ('Automobile', 'Automobile'), ('Worldwide', 'Worldwide'), ('Reviews', 'Reviews')], max_length=30),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 19, 28, 2, 134671)),
        ),
        migrations.AlterField(
            model_name='authors',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 19, 28, 2, 111111)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 19, 28, 2, 136264)),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 19, 28, 2, 136998)),
        ),
    ]
