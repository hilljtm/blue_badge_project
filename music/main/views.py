from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from main.models import *


def home(request):
    picks = our_picks.objects.all()

    context = {
        'html_picks': picks
    }

    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')
