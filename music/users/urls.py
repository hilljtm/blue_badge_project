
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from users import views as user_views


urlpatterns = [
    path('signup/', views.signUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
]
