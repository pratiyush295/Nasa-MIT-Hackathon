
from django.contrib import admin
from django.urls import path,include
from app1 import urls
import app1
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('test/',views.test,name='test'),
    path('login/',views.login,name="login"),
    path('login_validation/',views.login_validation,name='login_validation'),
    path('addNumber/',views.addNumber,name='addNumber'),
    path('register_validation/',views.register_validation,name='register_validation'),
    path('raiseConcern/',views.raiseConcern,name="raiseConcern")
]
