
from django.contrib import admin
from django.urls import path
from first import views

urlpatterns = [
    path('insert/', views.insert),
    path('load/', views.load),
]