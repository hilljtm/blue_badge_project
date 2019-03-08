
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='blogPage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    path('post/new/', PostCreateView.as_view(), name='postCreate'),
]
