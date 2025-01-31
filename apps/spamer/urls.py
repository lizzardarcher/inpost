# -*- encoding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.BaseSpamerView.as_view(), name='index'),

    path('accs/', views.AccountListView.as_view(), name='accs'),
    path('accs/<int:pk>/', views.AccountDetailView.as_view(), name='acc detail'),
    path('accs/create/', views.AccountCreateView.as_view(), name='acc create'),
    path('accs/<int:pk>/update/', views.AccountUpdateView.as_view(), name='acc edit'),
    # path('accs/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='acc delete'),
    path('accs/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='acc delete'),

    path('chat/', views.ChatListView.as_view(), name='chats'),
    path('chat/<int:pk>/', views.ChatDetailView.as_view(), name='chat detail'),
    path('chat/create/', views.ChatCreateView.as_view(), name='chat create'),
    path('chat/upload/', views.ChatUploadView.as_view(), name='chat upload'),
    path('chat/<int:pk>/update/', views.ChatUpdateView.as_view(), name='chat edit'),
    # path('chat/<int:pk>/delete/', views.ChatDeleteView.as_view(), name='chat delete'),
    path('chat/<int:id>/delete/', views.ChatDeleteView.delete_view, name='chat delete'),

    path('channel/', views.ChannelToSubscribeListView.as_view(), name='channels'),
    path('channel/create/', views.ChannelToSubscribeCreateView.as_view(), name='channel create'),
    path('channel/<int:pk>/update/', views.ChannelToSubscribeUpdateView.as_view(), name='channel edit'),
    path('channel/<int:pk>/delete/', views.ChannelToSubscribeDeleteView.as_view(), name='channel delete'),

    path('statistics/', views.StatisticsDetailView.as_view(), name='statistics'),
    path('msg/', views.MessageListView.as_view(), name='msg'),
    path('client/', views.ClientListView.as_view(), name='client'),
    path('logging/', views.AccountLoggingListView.as_view(), name='logging'),
    path('settings/', views.GeneralSettingsListView.as_view(), name='settings'),

]
