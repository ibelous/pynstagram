# Generated by Django 2.2.3 on 2019-07-29 17:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pgram', '0005_auto_20190725_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='image',
            new_name='<django.db.models.fields.related.ForeignKey>2019-07-29 17:21:31.639208+00:00',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='all_posts_count',
            field=models.IntegerField(default=0, verbose_name='Posts count(All time)'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='current_posts_count',
            field=models.IntegerField(default=0, verbose_name='Posts count'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 17, 21, 31, 639208, tzinfo=utc), verbose_name='Publish date'),
        ),
    ]
