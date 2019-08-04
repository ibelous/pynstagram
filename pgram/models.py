from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


app_name = 'pgram'


class PostModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author', on_delete=models.CASCADE,
                               related_name='posts')
    image = models.ImageField(verbose_name='Select Image', upload_to='photos')
    pub_date = models.DateTimeField(verbose_name='Publish date', default=timezone.now())
    desc = models.TextField(verbose_name='Description', max_length=2000, blank=True)

    def get_comments(self):
        return self.comments.all()


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to='profile_pics', blank=True)
    all_posts_count = models.IntegerField(verbose_name='Posts count(All time)', default=0)
    current_posts_count = models.IntegerField(verbose_name='Posts count', default=0)

    def __str__(self):
        return self.user.username

    def get_all_posts_count(self):
        return self.all_posts_count


class CommentModel(models.Model):
    post = models.ForeignKey('pgram.PostModel', on_delete=models.CASCADE, verbose_name='Post', related_name='comments')
    author = models.ForeignKey('pgram.UserModel', on_delete=models.CASCADE, verbose_name='Author',
                               related_name='comments')
    text = models.TextField(verbose_name='Comment', max_length=500)
    pub_date = models.DateTimeField(verbose_name='Publish Date', default=timezone.now())
