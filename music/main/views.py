from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return HttpResponse("ABOUT PAGE")


def contact(request):
    return HttpResponse("CONTACT PAGE")
