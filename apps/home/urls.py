# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

      path('', views.index, name='home'),

      # path('post', views.post),

      path('user_profile', views.UserUpdateView.user_profile, name='user profile fast kostyl'),
      path('user_profile/<int:pk>', views.UserUpdateView.as_view(), name='user profile'),

      path('post', views.PostListView.as_view(), name='posts'),
      path('post_create', views.PostCreateView.as_view(), name='create post'),
      # path('post_create', views.post, name='create post'),
      # path('post_update/<int:pk>', views.post_update, name='update post'),
      path('post_update/<int:pk>', views.PostUpdateView.as_view(), name='update post'),
      path('post_delete/<int:pk>', views.PostDeleteView.as_view(), name='delete post'),

      path('post_photo_update/<int:pk>', views.PostPhotoUpdateView.as_view(), name='post photo update'),
      path('post_photo_delete/<int:pk>', views.PostPhotoDeleteView.as_view(), name='post photo update'),

      path('post_video_update/<int:pk>', views.PostVideoUpdateView.as_view(), name='post video update'),
      path('post_video_delete/<int:pk>', views.PostVideoDeleteView.as_view(), name='post video delete'),

      path('post_music_update/<int:pk>', views.PostMusicUpdateView.as_view(), name='post music update'),
      path('post_music_delete/<int:pk>', views.PostMusicDeleteView.as_view(), name='post music delete'),

      path('post_documet_update/<int:pk>', views.PostDocumentUpdateView.as_view(), name='post document update'),
      path('post_documet_delete/<int:pk>', views.PostDocumentDeleteView.as_view(), name='post document delete'),

      path('bot', views.BotListView.as_view(), name='bot'),
      path('bot_create', views.BotCreateView.as_view(), name='create bot'),
      path('bot_update/<int:pk>', views.BotUpdateView.as_view(), name='update bot'),
      path('bot_delete/<int:pk>', views.BotDeleteView.as_view(), name='delete bot'),

      path('chat', views.ChatListView.as_view(), name='chat'),
      path('chat_create', views.ChatCreateView.as_view(), name='create chat'),
      path('chat_update/<int:pk>', views.ChatUpdateView.as_view(), name='update chat'),
      path('chat_delete/<int:pk>', views.ChatDeleteView.as_view(), name='delete chat'),

      path('calendar/<int:year>/<int:month>/', views.CalendarView.as_view(), name='calendar'),
      # path('calendar_event/<int:year>/<int:month>/<int:day>/', views.calendar_event, name='calendar event'),
      path('calendar_event_create/<int:year>/<int:month>/<int:day>/', views.CalendarEventCreate.as_view(), name='calendar event create'),

      path('schedule_update/<int:pk>', views.ScheduleUpdateView.as_view(), name='update schedule'),
      path('schedule_delete/<int:pk>', views.ScheduleDeleteView.as_view(), name='delete schedule'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
