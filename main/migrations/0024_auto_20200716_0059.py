# Generated by Django 3.0.6 on 2020-07-15 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200715_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_page_views',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='articles',
            name='author_url',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='articles',
            name='main_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 0, 59, 41, 843876), editable=False),
        ),
        migrations.AlterField(
            model_name='authors',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 0, 59, 41, 841797)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 0, 59, 41, 845952)),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 0, 59, 41, 847054)),
        ),
    ]
