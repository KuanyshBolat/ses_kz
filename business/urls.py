from django.urls import path
from django.contrib import admin
from django.urls import path, include
from business import views

urlpatterns = [
    path('lk/', views.lk),
]
