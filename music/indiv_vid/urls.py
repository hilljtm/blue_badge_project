
from django.urls import path
from .views import Indiv_vid_view, PostCreateView

urlpatterns = [
    path('', Indiv_vid_view, name='indiv_vid'),
    path('new/', PostCreateView, name='new_comment'),
]
