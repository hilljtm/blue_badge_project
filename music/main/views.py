from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from main.models import our_picks


def home(request):
    song_title = models.CharField('Title', max_length=30)
    return render(request, 'pages/home.html', {'our_picks': our_picks.objects.all()})


def about(request):
    return HttpResponse("ABOUT PAGE")


def contact(request):
    return HttpResponse("CONTACT PAGE")
