
from django.urls import path
from .views import Indiv_vid_view

urlpatterns = [
    path('', Indiv_vid_view, name='indiv_vid'),
    path('new/', Indiv_vid_view, name='new_comment'),
]
