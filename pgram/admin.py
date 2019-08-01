from django.contrib import admin

from .models import PostModel, UserModel, CommentModel
# Register your models here.
admin.site.register(PostModel)
admin.site.register(UserModel)
admin.site.register(CommentModel)
