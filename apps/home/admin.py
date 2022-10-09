# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *

admin.site.register(Bot)
# admin.site.register(Post)
admin.site.register(Button)
admin.site.register(Chat)
admin.site.register(Media)


class PostPhotoAdmin(admin.StackedInline):
    model = PostPhoto


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostPhotoAdmin]

    class Meta:
        model = Post


@admin.register(PostPhoto)
class PostImageAdmin(admin.ModelAdmin):
    pass