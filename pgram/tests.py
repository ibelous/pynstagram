import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import UserModel, PostModel
from django.contrib.auth.models import User


def create_user(username='admin', password='admin', email='admin@admin.admin'):
    return User.objects.create_user(username, password, email)


def create_post(author='white', image='media/photos/testphoto', days=0, desc=''):
    time = timezone.now() + datetime.timedelta(days=days)
    return PostModel.objects.create(author=author, image=image, pub_date=time, desc=desc)


