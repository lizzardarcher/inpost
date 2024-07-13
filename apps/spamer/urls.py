# -*- encoding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.AccountListView.as_view(), name='accs'),
    path('<int:pk>/', views.AccountDetailView.as_view(), name='acc detail'),
    path('create/', views.AccountCreateView.as_view(), name='acc create'),
    path('<int:pk>/update/', views.AccountUpdateView.as_view(), name='acc edit'),
    path('<int:pk>/delete/', views.AccountDeleteView.as_view(), name='acc delete'),
]
