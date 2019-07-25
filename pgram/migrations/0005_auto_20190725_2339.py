# Generated by Django 2.2.3 on 2019-07-25 20:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pgram', '0004_auto_20190725_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos', verbose_name='Select Image')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 25, 20, 39, 20, 180167, tzinfo=utc), verbose_name='Publish date')),
                ('desc', models.TextField(blank=True, max_length=2000, verbose_name='Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
