from django.contrib import admin

from .models import PostModel, UserModel
# Register your models here.
admin.site.register(PostModel)
admin.site.register(UserModel)
