
from django.urls import path
from .views import Indiv_vid_view, PostCreateCommentView, PostListView

urlpatterns = [
    path('', PostListView, name='indiv_vid'),
    path('new/', PostCreateCommentView.as_view(), name='new_comment'),
]
