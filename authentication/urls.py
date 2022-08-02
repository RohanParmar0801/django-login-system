from django.contrib import admin
from django.urls import path,include
from authentication import views as authentication_views

urlpatterns = [
    path('',authentication_views.home, name='home'),
]
