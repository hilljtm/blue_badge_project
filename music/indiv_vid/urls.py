
from django.urls import path
from .views import Indiv_vid_view, newComment

urlpatterns = [
    path('', Indiv_vid_view, name='indiv_vid'),
    path('new/', newComment.as_view(), name='new_comment'),
]
