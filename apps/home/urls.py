# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('post', views.PostListView.as_view(), name='posts'),
    # path('post_create', views.PostCreateView.as_view(), name='create post'),
    path('post_create', views.PostCreateView.as_view(), name='create post'),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(), name='update post'),
    path('post_delete/<int:pk>', views.PostDeleteView.as_view(), name='delete post'),

    path('bot', views.BotListView.as_view(), name='bot'),
    path('bot_create', views.BotCreateView.as_view(), name='create bot'),
    path('bot_update/<int:pk>', views.BotUpdateView.as_view(), name='update bot'),
    path('bot_delete/<int:pk>', views.BotDeleteView.as_view(), name='delete bot'),

    path('chat', views.ChatListView.as_view(), name='chat'),
    path('chat_create', views.ChatCreateView.as_view(), name='create chat'),
    path('chat_update/<int:pk>', views.ChatUpdateView.as_view(), name='update chat'),
    path('chat_delete/<int:pk>', views.ChatDeleteView.as_view(), name='delete chat'),


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
