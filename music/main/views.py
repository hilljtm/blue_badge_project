from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from main.models import *


def home(request):
    picks = our_picks.objects.all()

    context = {
        'html_picks': picks
    }

    return render(request, 'pages/home.html', context=context)


def about(request):
    return HttpResponse("ABOUT PAGE")


def contact(request):
    return HttpResponse("CONTACT PAGE")
