
from django.contrib import admin
from django.urls import path,include
from app1 import urls
import app1
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('test/',views.test,name='test')
]
