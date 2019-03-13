
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
