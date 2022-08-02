from django.contrib import admin
from django.urls import path,include
from authentication import views as authentication_views

urlpatterns = [
    path('',authentication_views.home, name='home'),
    path('signup',authentication_views.signup, name='signup'),
    path('signin',authentication_views.signin, name='signin'),
    path('signout',authentication_views.signout, name='signout'),
]
