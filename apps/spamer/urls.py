# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from django.views.static import serve

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AccountListView.as_view(), name='accs'),
    path('<int:pk>/', views.AccountDetailView.as_view(), name='acc detail'),
    path('<int:pk>/create/', views.AccountCreateView.as_view(), name='acc create'),
    path('<int:pk>/edit/', views.AccountUpdateView.as_view(), name='acc edit'),
    path('<int:pk>/delete/', views.AccountDeleteView.as_view(), name='acc delete'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = "apps.home.views.page_not_found_view"