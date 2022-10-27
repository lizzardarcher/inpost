# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


class PostPhotoAdmin(admin.StackedInline):
    model = PostPhoto


class PostMusicAdmin(admin.StackedInline):
    model = PostMusic


class PostVideoAdmin(admin.StackedInline):
    model = PostVideo


class PostDocumentAdmin(admin.StackedInline):
    model = PostDocument


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostPhotoAdmin, PostMusicAdmin, PostVideoAdmin, PostDocumentAdmin]

    class Meta:
        model = Post


@admin.register(PostPhoto)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostMusic)
class PostMusicAdmin(admin.ModelAdmin):
    pass


@admin.register(PostVideo)
class PostVideoAdmin(admin.ModelAdmin):
    pass


@admin.register(PostDocument)
class PostDocumentAdmin(admin.ModelAdmin):
    pass


class UserStatusInline(admin.StackedInline):
    model = UserStatus
    can_delete = False
    verbose_name_plural = 'Статус оплаты'


class UserAdmin(BaseUserAdmin):
    inlines = (UserStatusInline,)


admin.site.register(Bot)
admin.site.register(Button)
admin.site.register(Chat)
admin.site.register(Media)
admin.site.register(PostSchedule)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
