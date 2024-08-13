from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_detail, name='post_detail'),
    path('detail/', views.post_list, name='post_list'),
    path('create/', views.post_add, name='post_create'),
    path('update/', views.post_update, name='post_update'),
    path('delete/', views.post_delete, name='post_delete'),
]
