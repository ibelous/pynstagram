# Generated by Django 2.2.3 on 2019-07-24 23:19

import datetime
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pgram', '0002_auto_20190725_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='', verbose_name='Select Image')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 24, 23, 19, 49, 504821, tzinfo=utc), verbose_name='Publish date')),
                ('desc', models.TextField(max_length=2000, verbose_name='Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
