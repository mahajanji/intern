from django.contrib import admin
from django.urls import path,include
from appname import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('add-not/', views.nots, name='nots'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('success/', views.success, name='success'),
]