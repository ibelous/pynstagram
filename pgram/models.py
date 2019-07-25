from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Select Image', upload_to='photos')
    pub_date = models.DateTimeField(verbose_name='Publish date', default=timezone.now())
    desc = models.TextField(verbose_name='Description', max_length=2000, blank=True)


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
